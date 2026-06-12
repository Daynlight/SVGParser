from utils.static_typing import typechecked
from rich import print
import arcade
import re

from App.shapes.shape import Shape

@typechecked

class Elipse(Shape):

    @typechecked
    def __init__(self, position: tuple[int, int] = (0, 0), x_radius: int = 0, y_radius: int = 0):
        super().__init__()

        self._position: tuple[int, int] = position
        self._x_radius: int = x_radius
        self._y_radius: int = y_radius
        self._color: arcade.color = arcade.color.AZURE

    @typechecked
    def render(self) -> None:
        arcade.draw_ellipse_filled(self._position[0], self._position[1], self._x_radius, self._y_radius, self._color)
        
    @typechecked
    def parse(self, data: str, entry: int) -> bool:
        pairs = dict(re.findall(r"([xy]|rx|ry)\s*=\s*([+-]?\d+(?:\.\d+)?)", data))

        required_keys = {'x', 'y', 'rx', 'ry'}
        if not required_keys.issubset(pairs.keys()):
            missing = required_keys - pairs.keys()
            print(f"[yellow]On entry {entry}: Missing parameters [/yellow][blue]{missing}[/blue][yellow] in: {data}[/yellow]")
            return False
        
        self._position = (float(pairs['x']), float(pairs['y']))
        self._x_radius = float(pairs['rx'])
        self._y_radius = float(pairs['ry'])

        return True
    
    @typechecked
    @classmethod
    def validate(self, data: str) -> bool:
        pattern: str = r"[Ee]lipse"
        return bool(re.search(pattern, data))
