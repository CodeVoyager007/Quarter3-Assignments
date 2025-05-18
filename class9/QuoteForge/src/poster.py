from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import io
import os
import requests
from typing import Optional, Tuple, Literal, List
from dataclasses import dataclass
import numpy as np

GOOGLE_FONTS_API_KEY = "AIzaSyAvxH7Zf0G6Mhmnqx9k5K8UFnDEjemC_40"
UNSPLASH_API_KEY = "93RAiDPJfQ_p_YZY5UeoG-QXEoouD-zr4Nugi8O2Cts"
FONTS_DIR = Path(__file__).parent / "fonts"
FONTS_DIR.mkdir(exist_ok=True)

# Handles background image retrieval and storage from Unsplash API
@dataclass
class ImageSource:
    url: str
    content: bytes
    
    @classmethod
    def from_unsplash(cls, query: str) -> Optional['ImageSource']:
        headers = {
            "Authorization": f"Client-ID {UNSPLASH_API_KEY}",
            "Accept-Version": "v1"
        }
        formatted_query = query.replace(" ", "+")
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
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        return cls(url=image_url, content=image_response.content)

# Configuration class for defining poster theme styles
@dataclass
class ThemeConfig:
    font_family: str
    font_size: int
    text_color: Tuple[int, int, int]
    unsplash_query: str
    background_color: Optional[Tuple[int, int, int]] = None
    background_gradient: Optional[Tuple[Tuple[int, int, int], Tuple[int, int, int]]] = None

# Manages font downloading and loading from Google Fonts API
class FontManager:
    def __init__(self, api_key: str, fonts_dir: Path):
        self.api_key = api_key
        self.fonts_dir = fonts_dir
        self.fonts_dir.mkdir(exist_ok=True)
    
    def get_font(self, family: str, size: int) -> ImageFont.FreeTypeFont:
        font_path = self._download_font(family)
        if font_path and os.path.exists(font_path):
            return ImageFont.truetype(font_path, size)
        return ImageFont.load_default()
    
    def _download_font(self, family: str) -> Optional[str]:
        api_url = f"https://www.googleapis.com/webfonts/v1/webfonts?key={self.api_key}&family={family}"
        response = requests.get(api_url)
        response.raise_for_status()
        font_data = response.json()
        
        if not font_data.get('items'):
            return None
            
        font_url = None
        for item in font_data['items']:
            if item['family'] == family:
                font_url = item['files'].get('regular')
                break
        
        if not font_url:
            return None
            
        font_path = self.fonts_dir / f"{family.replace(' ', '_')}.ttf"
        if not font_path.exists():
            font_response = requests.get(font_url)
            font_response.raise_for_status()
            with open(font_path, 'wb') as f:
                f.write(font_response.content)
        return str(font_path)
# Predefined theme configurations for different poster styles
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
# Handles text wrapping and rendering with proper alignment
class TextRenderer:
    def __init__(self, draw: ImageDraw.ImageDraw, font: ImageFont.FreeTypeFont, color: Tuple[int, int, int]):
        self.draw = draw
        self.font = font
        self.color = color
        
    def wrap_text(self, text: str, max_width: int) -> List[str]:
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = current_line + [word]
            test_text = ' '.join(test_line)
            bbox = self.font.getbbox(test_text)
            width = bbox[2] - bbox[0]
            
            if width <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(word)
                    current_line = []
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
# Main class for generating quote posters with various themes and customizations
class Poster:
    def __init__(self, width: int = 1080, height: int = 1080, theme: ThemeConfig = PosterThemes.MINIMAL):
        self.width = width
        self.height = height
        self.theme = theme
        self.font_manager = FontManager(GOOGLE_FONTS_API_KEY, FONTS_DIR)
        self._image = None
        self._draw = None
        
    def _create_gradient_background(self, color1: Tuple[int, int, int], color2: Tuple[int, int, int]) -> Image.Image:
        array = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        for y in range(self.height):
            r = int(color1[0] + (color2[0] - color1[0]) * y / self.height)
            g = int(color1[1] + (color2[1] - color1[1]) * y / self.height)
            b = int(color1[2] + (color2[2] - color1[2]) * y / self.height)
            array[y, :] = [r, g, b]
        return Image.fromarray(array)
    def _init_image(self, background_image: Optional[Image.Image] = None, unsplash_category: Optional[str] = None):
        if background_image:
            ratio = max(self.width/background_image.width, self.height/background_image.height)
            new_size = (int(background_image.width * ratio), int(background_image.height * ratio))
            background_image = background_image.resize(new_size, Image.Resampling.LANCZOS)
            
            left = (background_image.width - self.width)/2
            top = (background_image.height - self.height)/2
            self._image = background_image.crop((left, top, left + self.width, top + self.height))
        else:
            try:
                # Use category if provided, otherwise use theme's default query
                query = unsplash_category.lower() if unsplash_category else self.theme.unsplash_query
                image_source = ImageSource.from_unsplash(query)
                if image_source:
                    image = Image.open(io.BytesIO(image_source.content))
                    if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
                        image = image.convert('RGB')
                    self._init_image(image)
                    return
            except:
                pass
            
            if self.theme.background_gradient:
                self._image = self._create_gradient_background(*self.theme.background_gradient)
            else:
                self._image = Image.new('RGB', (self.width, self.height), self.theme.background_color or (255, 255, 255))
        
        self._draw = ImageDraw.Draw(self._image)

    def generate(
        self,
        quote: str,
        author: str = "Anonymous",
        background_image: Optional[Image.Image] = None,
        text_position: Literal["top", "middle", "bottom"] = "middle",
        blur_background: bool = False,
        watermark: bool = False,
        unsplash_category: Optional[str] = None
    ) -> Image.Image:
        self._init_image(background_image, unsplash_category)
        
        if blur_background:
            self._image = self._image.filter(ImageFilter.GaussianBlur(5))

        overlay = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 127))
        self._image = Image.alpha_composite(self._image.convert('RGBA'), overlay)
        self._image = self._image.convert('RGB')
        self._draw = ImageDraw.Draw(self._image)

        quote_font = self.font_manager.get_font(self.theme.font_family, self.theme.font_size)
        watermark_font = self.font_manager.get_font(self.theme.font_family, 20)
        
        text_renderer = TextRenderer(self._draw, quote_font, self.theme.text_color)
        max_text_width = int(self.width * 0.8)
        quote_lines = text_renderer.wrap_text(quote, max_text_width)
        
        line_spacing = int(self.theme.font_size * 0.3)
        quote_height = len(quote_lines) * (self.theme.font_size + line_spacing)
        author_bbox = self._draw.textbbox((0, 0), f"- {author}", font=quote_font)
        author_height = author_bbox[3] - author_bbox[1]
        
        total_height = quote_height + author_height + 40
        
        y = (self.height - total_height) / 2
        if text_position == "top":
            y = self.height * 0.15
        elif text_position == "bottom":
            y = self.height * 0.85 - total_height
        for line in quote_lines:
            bbox = self._draw.textbbox((0, 0), line, font=quote_font)
            line_width = bbox[2] - bbox[0]
            x = (self.width - line_width) / 2
            self._draw.text((x, y), line, font=quote_font, fill=self.theme.text_color)
            y += self.theme.font_size + line_spacing
        
        author_text = f"- {author}"
        author_bbox = self._draw.textbbox((0, 0), author_text, font=quote_font)
        author_width = author_bbox[2] - author_bbox[0]
        x = (self.width - author_width) / 2
        y += 20
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
        image.save(output, format=format)
        output.seek(0)
        return output 