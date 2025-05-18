from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import io
import os
import requests
from typing import Optional, Tuple, Literal, List
from dataclasses import dataclass
import numpy as np
import textwrap

GOOGLE_FONTS_API_KEY = "AIzaSyAvxH7Zf0G6Mhmnqx9k5K8UFnDEjemC_40"
UNSPLASH_API_KEY = "93RAiDPJfQ_p_YZY5UeoG-QXEoouD-zr4Nugi8O2Cts"
FONTS_DIR = Path(__file__).parent / "fonts"
FONTS_DIR.mkdir(exist_ok=True)

def get_random_unsplash_image(query: str = "nature,abstract,texture") -> Optional[Image.Image]:
    """Get a random image from Unsplash API."""
    try:
        headers = {
            "Authorization": f"Client-ID {UNSPLASH_API_KEY}",
            "Accept-Version": "v1"
        }
        
        # Clean and format the query
        formatted_query = query.replace(" ", "+")
        
        # Make the API request
        url = "https://api.unsplash.com/photos/random"
        params = {
            "query": formatted_query,
            "orientation": "squarish",
            "content_filter": "high"
        }
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        image_url = data['urls']['regular']
        
        # Download the image
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        # Open the image from bytes and convert to RGB
        image = Image.open(io.BytesIO(image_response.content))
        if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
            image = image.convert('RGB')
        return image
    except Exception as e:
        print(f"Error fetching Unsplash image: {str(e)}")
        return None

def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> List[str]:
    """Wrap text to fit within a given width."""
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        # Try adding the word to the current line
        test_line = current_line + [word]
        test_text = ' '.join(test_line)
        bbox = font.getbbox(test_text)
        width = bbox[2] - bbox[0]
        
        if width <= max_width:
            current_line = test_line
        else:
            if current_line:  # If there are words in the current line
                lines.append(' '.join(current_line))
                current_line = [word]
            else:  # If the word itself is longer than max_width
                lines.append(word)
                current_line = []
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines

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
    unsplash_query: str
    background_color: Optional[Tuple[int, int, int]] = None
    background_gradient: Optional[Tuple[Tuple[int, int, int], Tuple[int, int, int]]] = None

class PosterThemes:
    MINIMAL = ThemeConfig(
        font_family="Roboto",
        font_size=60,
        text_color=(255, 255, 255),
        unsplash_query="minimal white background",
        background_color=(255, 255, 255)
    )
    
    ELEGANT = ThemeConfig(
        font_family="Playfair Display",
        font_size=65,
        text_color=(255, 255, 255),
        unsplash_query="elegant dark background",
        background_gradient=((48, 16, 255), (100, 115, 255))
    )
    
    BOLD = ThemeConfig(
        font_family="Oswald",
        font_size=70,
        text_color=(255, 255, 255),
        unsplash_query="vibrant colorful background",
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
        else:
            # Try to get an Unsplash image first
            unsplash_image = get_random_unsplash_image(self.theme.unsplash_query)
            if unsplash_image:
                # Convert to RGB if necessary
                if unsplash_image.mode in ('RGBA', 'LA') or (unsplash_image.mode == 'P' and 'transparency' in unsplash_image.info):
                    unsplash_image = unsplash_image.convert('RGB')
                self._init_image(unsplash_image)
                return
            
            # Fallback to gradient or solid color
            if self.theme.background_gradient:
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
        
        if blur_background:
            self._image = self._image.filter(ImageFilter.GaussianBlur(5))

        # Add a dark overlay to ensure text readability
        overlay = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 127))
        self._image = Image.alpha_composite(self._image.convert('RGBA'), overlay)
        self._image = self._image.convert('RGB')
        self._draw = ImageDraw.Draw(self._image)

        # Load fonts
        quote_font = self._get_font(self.theme.font_size)
        watermark_font = self._get_font(20)

        # Calculate maximum width for text (80% of image width)
        max_text_width = int(self.width * 0.8)

        # Wrap quote text
        quote_lines = wrap_text(quote, quote_font, max_text_width)
        
        # Calculate total height needed
        line_spacing = int(self.theme.font_size * 0.3)  # 30% of font size for spacing
        quote_height = len(quote_lines) * (self.theme.font_size + line_spacing)
        author_bbox = self._draw.textbbox((0, 0), f"- {author}", font=quote_font)
        author_height = author_bbox[3] - author_bbox[1]
        
        total_height = quote_height + author_height + 40  # 40px padding between quote and author
        
        # Calculate vertical position
        if text_position == "top":
            y = self.height * 0.15
        elif text_position == "bottom":
            y = self.height * 0.85 - total_height
        else:  # middle
            y = (self.height - total_height) / 2

        # Draw quote lines
        for line in quote_lines:
            bbox = self._draw.textbbox((0, 0), line, font=quote_font)
            line_width = bbox[2] - bbox[0]
            x = (self.width - line_width) / 2
            self._draw.text((x, y), line, font=quote_font, fill=self.theme.text_color)
            y += self.theme.font_size + line_spacing
        
        # Draw author
        author_text = f"- {author}"
        author_bbox = self._draw.textbbox((0, 0), author_text, font=quote_font)
        author_width = author_bbox[2] - author_bbox[0]
        x = (self.width - author_width) / 2
        y += 20  # Add some padding before author
        self._draw.text((x, y), author_text, font=quote_font, fill=self.theme.text_color)
        
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