from utils.static_typing import typechecked
from rich import print
import arcade
import re

from App.shapes.shape import Shape
from App.shapes.colors import ColorParser

@typechecked
class Rectangle(Shape):
    @typechecked
    def __init__(self, position: tuple[int, int] = (0, 0), width: int = 0, height: int = 0) -> None:
        super().__init__()

        self._position: tuple[int, int] = position
        self._width: int = width
        self._height: int = height
        self._color: arcade.color = arcade.color.AZURE

    @typechecked
    def render(self) -> None:
        arcade.draw_lbwh_rectangle_filled(self._position[0], self._position[1], self._width, self._height, self._color)
    

    @typechecked
    def parse(self, data: str, entry: int) -> bool:
        data = re.sub(r"^[Rr]ectangle\s*\(\s*", "", data)
        data = re.sub(r"\)\s*;?\s*$", "", data)
        pattern = r'^\s*(?:(?:[xywhc]|color)\s*=\s*[\w#\'".+-]+\s*,\s*)*(?:[xywhc]|color)\s*=\s*[\w#\'".+-]+\s*;?\s*$'

        if not re.fullmatch(pattern, data, re.VERBOSE):
            print(f"[yellow]On entry {entry}: invalid format[/yellow] [blue]{data}[/blue]")
            return False
    
        pairs = dict(re.findall(r'([xywhc]|color)\s*=\s*([\w#\'".+-]+)', data))

        required_keys = {'x', 'y', 'w', 'h'}
        allowed_keys = {'x', 'y', 'w', 'h', 'c', 'color'}

        if not required_keys.issubset(pairs.keys()):

            missing = required_keys - pairs.keys()
            print(f"[yellow]On entry {entry}: Missing parameters [/yellow][blue]{missing}[/blue][yellow] in: {data}[/yellow]")
            return False
        
        invalid_keys = set(pairs.keys()) - allowed_keys
        if invalid_keys:
            print(f"[yellow]On entry {entry}: Unrecognized parameters [/yellow][red]{invalid_keys}[/red][yellow] in: {data}[/yellow]")
            return False
        
        self._position = (float(pairs['x']), float(pairs['y']))
        self._width = float(pairs['w'])
        self._height = float(pairs['h'])

        if 'color' in pairs:
            self._color = ColorParser.parse(pairs['color'])
        elif 'c' in pairs:
            self._color = ColorParser.parse(pairs['c'])

        return True
    


    @typechecked
    @classmethod

    def validate(self, data:str) -> bool:
        pattern: str = r"[Rr]ectangle"
        return bool(re.search(pattern, data))
