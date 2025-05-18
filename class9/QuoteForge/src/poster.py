from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import io
import os
import requests
from typing import Optional, Tuple, Literal
from dataclasses import dataclass
import numpy as np

GOOGLE_FONTS_API_KEY = "AIzaSyAvxH7Zf0G6Mhmnqx9k5K8UFnDEjemC_40"
FONTS_DIR = Path(__file__).parent / "fonts"
FONTS_DIR.mkdir(exist_ok=True)

def download_google_font(font_family: str) -> Optional[str]:
    """Download a font from Google Fonts API and return the path to the font file."""
    try:
        # Get font information from Google Fonts API
        api_url = f"https://www.googleapis.com/webfonts/v1/webfonts?key={GOOGLE_FONTS_API_KEY}&family={font_family}"
        response = requests.get(api_url)
        response.raise_for_status()
        font_data = response.json()
        
        if not font_data.get('items'):
            return None
            
        # Get the regular variant download URL
        font_url = None
        for item in font_data['items']:
            if item['family'] == font_family:
                font_url = item['files'].get('regular')
                break
        
        if not font_url:
            return None
            
        # Download the font file
        font_path = FONTS_DIR / f"{font_family.replace(' ', '_')}.ttf"
        if not font_path.exists():
            font_response = requests.get(font_url)
            font_response.raise_for_status()
            with open(font_path, 'wb') as f:
                f.write(font_response.content)
                
        return str(font_path)
    except Exception as e:
        print(f"Error downloading font: {str(e)}")
        return None

@dataclass
class ThemeConfig:
    font_family: str
    font_size: int
    text_color: Tuple[int, int, int]
    background_color: Optional[Tuple[int, int, int]] = None
    background_gradient: Optional[Tuple[Tuple[int, int, int], Tuple[int, int, int]]] = None

class PosterThemes:
    MINIMAL = ThemeConfig(
        font_family="Roboto",
        font_size=60,
        text_color=(0, 0, 0),
        background_color=(255, 255, 255)
    )
    
    ELEGANT = ThemeConfig(
        font_family="Playfair Display",
        font_size=65,
        text_color=(255, 255, 255),
        background_gradient=((48, 16, 255), (100, 115, 255))
    )
    
    BOLD = ThemeConfig(
        font_family="Oswald",
        font_size=70,
        text_color=(255, 255, 255),
        background_gradient=((255, 59, 48), (255, 149, 0))
    )

class Poster:
    def __init__(
        self,
        width: int = 1080,
        height: int = 1080,
        theme: ThemeConfig = PosterThemes.MINIMAL
    ):
        self.width = width
        self.height = height
        self.theme = theme
        self._image = None
        self._draw = None
        
    def _create_gradient_background(self, color1: Tuple[int, int, int], color2: Tuple[int, int, int]) -> Image.Image:
        """Create a gradient background."""
        array = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        for y in range(self.height):
            r = int(color1[0] + (color2[0] - color1[0]) * y / self.height)
            g = int(color1[1] + (color2[1] - color1[1]) * y / self.height)
            b = int(color1[2] + (color2[2] - color1[2]) * y / self.height)
            array[y, :] = [r, g, b]
        return Image.fromarray(array)

    def _init_image(self, background_image: Optional[Image.Image] = None):
        """Initialize the image with background."""
        if background_image:
            # Resize and crop background image to fit
            ratio = max(self.width/background_image.width, self.height/background_image.height)
            new_size = (int(background_image.width * ratio), int(background_image.height * ratio))
            background_image = background_image.resize(new_size, Image.Resampling.LANCZOS)
            
            # Center crop
            left = (background_image.width - self.width)/2
            top = (background_image.height - self.height)/2
            self._image = background_image.crop((left, top, left + self.width, top + self.height))
        elif self.theme.background_gradient:
            self._image = self._create_gradient_background(*self.theme.background_gradient)
        else:
            self._image = Image.new('RGB', (self.width, self.height), self.theme.background_color or (255, 255, 255))
        
        self._draw = ImageDraw.Draw(self._image)

    def _get_font(self, size: int) -> ImageFont.FreeTypeFont:
        """Get the font, downloading from Google Fonts if necessary."""
        font_path = download_google_font(self.theme.font_family)
        if font_path and os.path.exists(font_path):
            return ImageFont.truetype(font_path, size)
        return ImageFont.load_default()

    def generate(
        self,
        quote: str,
        author: str = "Anonymous",
        background_image: Optional[Image.Image] = None,
        text_position: Literal["top", "middle", "bottom"] = "middle",
        blur_background: bool = False,
        watermark: bool = False
    ) -> Image.Image:
        """Generate the quote poster."""
        self._init_image(background_image)
        
        if blur_background and background_image:
            self._image = self._image.filter(ImageFilter.GaussianBlur(5))

        # Load fonts
        quote_font = self._get_font(self.theme.font_size)
        watermark_font = self._get_font(20)

        # Calculate text position
        quote_bbox = self._draw.textbbox((0, 0), quote, font=quote_font)
        author_bbox = self._draw.textbbox((0, 0), f"- {author}", font=quote_font)
        
        quote_width = quote_bbox[2] - quote_bbox[0]
        quote_height = quote_bbox[3] - quote_bbox[1]
        author_width = author_bbox[2] - author_bbox[0]
        
        total_height = quote_height + author_bbox[3] + 20  # 20px padding between quote and author
        
        if text_position == "top":
            y = self.height * 0.2
        elif text_position == "bottom":
            y = self.height * 0.6
        else:  # middle
            y = (self.height - total_height) / 2

        # Draw quote
        x = (self.width - quote_width) / 2
        self._draw.text((x, y), quote, font=quote_font, fill=self.theme.text_color)
        
        # Draw author
        x = (self.width - author_width) / 2
        y += quote_height + 20
        self._draw.text((x, y), f"- {author}", font=quote_font, fill=self.theme.text_color)
        
        if watermark:
            watermark_text = "QuoteForge"
            watermark_bbox = self._draw.textbbox((0, 0), watermark_text, font=watermark_font)
            watermark_width = watermark_bbox[2] - watermark_bbox[0]
            self._draw.text(
                (self.width - watermark_width - 10, self.height - 30),
                watermark_text,
                font=watermark_font,
                fill=(128, 128, 128, 128)
            )
        
        return self._image

    def save(self, image: Image.Image, output: io.BytesIO, format: str = "PNG"):
        """Save the image to a bytes buffer."""
        image.save(output, format=format)
        output.seek(0)
        return output 