from utils.static_typing import typechecked
from rich import print
import arcade
import re

from App.shapes.shape import Shape
from App.shapes.colors import ColorParser


@typechecked
class Circle(Shape):
  @typechecked
  def __init__(self, position: tuple[int, int] = (0, 0), radius: int = 0) -> None:
    super().__init__()
    self._position: tuple[int, int] = position
    self._radius: int = radius
    self._color: arcade.color = arcade.color.AZURE


  @typechecked
  def render(self) -> None:
    arcade.draw_circle_filled(self._position[0], self._position[1], self._radius, self._color)


  @typechecked
  def parse(self, data: str, entry: int) -> bool:

    if not re.search(r"\)\s*;?\s*$", data):
      print(f"[yellow]On entry {entry}: missing closing bracket[/yellow] [blue]{data}[/blue]")
      return False
    
    data = re.sub(r"^[Cc]ircle\s*\(\s*", "", data)
    data = re.sub(r"\)\s*;?\s*$", "", data)
    pattern = r'^\s*(?:(?:[xyrc]|color)\s*=\s*[\w#\'".+-]+\s*,\s*)*(?:[xyrc]|color)\s*=\s*[\w#\'".+-]+\s*;?\s*$'

    if not re.fullmatch(pattern, data):
        print(f"[yellow]On entry {entry}: invalid format[/yellow] [blue]{data}[/blue]")
        return False
    pairs = dict(re.findall(r'([xyrc]|color)\s*=\s*([\w#\'".+-]+)', data))
  
    required_keys = {'x', 'y', 'r'}
    allowed_keys = {'x', 'y', 'r', 'c', 'color'}


    if not required_keys.issubset(pairs.keys()):
      missing = required_keys - pairs.keys()
      print(f"[yellow]On entry {entry}: Missing parameters [/yellow][blue]{missing}[/blue][yellow] in: {data}[/yellow]")
      return False
    
    invalid_keys = set(pairs.keys()) - allowed_keys
    if invalid_keys:
        print(f"[yellow]On entry {entry}: Unrecognized parameters [/yellow][red]{invalid_keys}[/red][yellow] in: {data}[/yellow]")
        return False

    try:
      self._position = (float(pairs['x']), float(pairs['y']))
      self._radius = float(pairs['r'])
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
    pattern: str = r"[Cc]ircle"
    return bool(re.search(pattern, data))
