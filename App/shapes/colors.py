import arcade
import re
from utils.static_typing import typechecked

@typechecked
class ColorParser:
    _colors_map: arcade.color = {
        "red": arcade.color.RED,
        "blue": arcade.color.BLUE,
        "green": arcade.color.GREEN,
        "azure": arcade.color.AZURE,
        "black": arcade.color.BLACK,
        "white": arcade.color.WHITE,
        "yellow": arcade.color.YELLOW,
        "pink": arcade.color.PINK,
        "purple": arcade.color.PURPLE,
        "orange": arcade.color.ORANGE,
        "brown": arcade.color.BROWN,
        "gray": arcade.color.GRAY
    }
    @classmethod
    def hex_to_rgb(self, value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


    @classmethod
    def parse(self, color_str: str) -> arcade.color:

        clean_color = color_str.strip().lower().strip('\'"')

        if clean_color in self._colors_map:
            return self._colors_map[clean_color]
        
        if re.match(r"^#(?:[0-9a-fA-F]{3}){1,2}$", clean_color):
            return self.hex_to_rgb(clean_color)
        else:
            return None
