from utils.static_typing import typechecked
from rich import print
import arcade
import re

from App.shapes.shape import Shape

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
        pattern = r"^\s*(?:[xywh]\s*=\s*[+-]?\d+(?:\.\d+)?\s*,\s*)*[xywh]\s*=\s*[+-]?\d+(?:\.\d+)?\s*;?\s*$"

        if not re.fullmatch(pattern, data, re.VERBOSE):
            print(f"[yellow]On entry {entry}: invalid format[/yellow] [blue]{data}[/blue]")
            return False
    
        pairs = dict(re.findall(r"([xywh])\s*=\s*([+-]?\d+(?:\.\d+)?)", data))

        required_keys = {'x', 'y', 'w', 'h'}

        if not required_keys.issubset(pairs.keys()):

            missing = required_keys - pairs.keys()

            print(f"[yellow]On entry {entry}: Missing parameters [/yellow][blue]{missing}[/blue][yellow] in: {data}[/yellow]")
            return False
        
        self._position = (float(pairs['x']), float(pairs['y']))
        self._width = float(pairs['w'])
        self._height = float(pairs['h'])

        return True
    


    @typechecked
    @classmethod

    def validate(self, data:str) -> bool:
        pattern: str = r"[Rr]ectangle"
        return bool(re.search(pattern, data))
