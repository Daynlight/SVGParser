from utils.static_typing import typechecked
from rich import print
import arcade
import re

from App.shapes.shape import Shape

@typechecked
class Line(Shape):
    @typechecked

    def __init__(self, start_position: tuple[int, int] = (0, 0), end_position: tuple[int, int] = (0, 0), line_width: int = 0):
        super().__init__()

        self._start_position: tuple[int, int] = start_position
        self._end_position: tuple[int, int] = end_position
        self._line_width: int = line_width
        self._color: arcade.color = arcade.color.AZURE

    @typechecked
    def render(self) -> None:
        arcade.draw_line(self._start_position[0], self._start_position[1], self._end_position[0], self._end_position[1],
                    self._color, self._line_width)
        
    @typechecked
    def parse(self, data: str, entry: int ) -> bool:
        pairs = dict(re.findall(r"(x1|y1|x2|y2|w)\s*=\s*([+-]?\d+(?:\.\d+)?)", data))

        required_keys = {'x1', 'y1', 'x2', 'y2', 'w'}
        if not required_keys.issubset(pairs.keys()):
            missing = required_keys - pairs.keys()
            print(f"[yellow]On entry {entry}: Missing parameters [/yellow][blue]{missing}[/blue][yellow] in: {data}[/yellow]")
            return False
        
        self._start_position = (float(pairs['x1']), float(pairs['y1']))
        self._end_position = (float(pairs['x2']), float(pairs['y2']))
        self._line_width = float(pairs['w'])

        return True
    
    @typechecked
    @classmethod
    def validate(self, data: str) -> bool:
        pattern: str = r"[L]ine"
        return bool(re.search(pattern, data))
