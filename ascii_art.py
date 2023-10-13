from PIL import Image, ImageDraw, ImageFont
import numpy as np

__all__ = ["ASCIIArt"]

MAP = r"@#&8%WM*oaeqgcmunrxjftwyiszlvk-|. "

class ASCIIArt:
    def __init__(self, path_to_image: str, path_to_font: str = None, font_size: int = 10) -> None:
        self.font_size = font_size
        if path_to_font is not None:
            self.font = ImageFont.truetype(path_to_font, self.font_size)
        else:
            self.font = ImageFont.load_default()
        self.image = np.array(Image.open(path_to_image))
        self.ascii = Image.new("RGB", (self.image.shape[1] * font_size, self.image.shape[0] * font_size), (255, 255, 255))
        self.img_arr = np.zeros((self.image.shape[0], self.image.shape[1]))
        self.draw = ImageDraw.Draw(self.ascii)

    def __repr__(self):
        return self.image
    
    def _squash(self, x: float, lim: int, a: int) -> float:
        return lim / (1 + np.exp(-(1 / a) * x))

    def _convert(self) -> None:
        for y in range(self.image.shape[0]):
            for x in range(self.image.shape[1]):
                self.draw.text((x * self.font_size, y * self.font_size), MAP[round(self._squash(np.mean(self.image[y, x, :]), len(MAP) - 1, a=len(MAP)))], fill=(0, 0, 0), font=self.font)

    def save(self, path: str = None, format: str = 'PNG') -> None:
        self._convert()
        self.ascii.save(path, format)

    def show(self) -> None:
        self._convert()
        self.ascii.show()
