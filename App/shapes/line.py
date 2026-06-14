from utils.static_typing import typechecked
from rich import print
import arcade
import re

from App.shapes.shape import Shape
from App.shapes.colors import ColorParser

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

        if not re.search(r"\)\s*;?\s*$", data):
            print(f"[yellow]On entry {entry}: missing closing bracket[/yellow] [blue]{data}[/blue]")
            return False
        
        data = re.sub(r"^[Ll]ine\s*\(\s*", "", data)
        data = re.sub(r"\)\s*;?\s*$", "", data)

        pattern = r'^\s*(?:(?:x1|y1|x2|y2|w|c|color)\s*=\s*[\w#\'".+-]+\s*,\s*)*(?:x1|y1|x2|y2|w|c|color)\s*=\s*[\w#\'".+-]+\s*;?\s*$'


        pairs = dict(re.findall(r"(x1|y1|x2|y2|w|c|color)\s*=\s*([\w#'\".+-]+)", data))

        required_keys = {'x1', 'y1', 'x2', 'y2', 'w'}
        allowed_keys = {'x1', 'y1', 'x2', 'y2', 'w', 'c', 'color'}

        if not required_keys.issubset(pairs.keys()):
            missing = required_keys - pairs.keys()
            print(f"[yellow]On entry {entry}: Missing parameters [/yellow][blue]{missing}[/blue][yellow] in: {data}[/yellow]")
            return False
        
        invalid_keys = set(pairs.keys()) - allowed_keys
        if invalid_keys:
            print(f"[yellow]On entry {entry}: Unrecognized parameters [/yellow][red]{invalid_keys}[/red][yellow] in: {data}[/yellow]")
            return False
        
        try:
            self._start_position = (float(pairs['x1']), float(pairs['y1']))
            self._end_position = (float(pairs['x2']), float(pairs['y2']))
            self._line_width = float(pairs['w'])
        except ValueError:
            print(f"[yellow]On entry {entry}: Invalid numeric value in {data}[/yellow]")
            return False
        
        color_value = None
        if 'color' in pairs:
            color_value = ColorParser.parse(pairs['color'])
        elif 'c' in pairs:
            color_value = ColorParser.parse(pairs['c'])

        if 'color' in pairs or 'c' in pairs:
            if color_value is None:
                print(f"[yellow]On entry {entry}: Invalid color value[/yellow]")
                return False
            self._color = color_value

        return True
    
    @typechecked
    @classmethod
    def validate(self, data: str) -> bool:
        pattern: str = r"[Ll]ine"
        return bool(re.search(pattern, data))
