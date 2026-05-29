from utils.static_typing import typechecked
from rich import print
import arcade
import re

from App.shapes.shape import Shape



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
    pairs = dict(re.findall(r"([xyr])\s*=\s*([+-]?\d+(?:\.\d+)?)", data))
  
    required_keys = {'x', 'y', 'r'}
    if not required_keys.issubset(pairs.keys()):
      missing = required_keys - pairs.keys()
      print(f"[yellow]On entry {entry}: Missing parameters [/yellow][blue]{missing}[/blue][yellow] in: {data}[/yellow]")
      return False

    self._position = (float(pairs['x']), float(pairs['y']))
    self._radius = float(pairs['r'])
    return True


  @typechecked
  @classmethod
  def validate(self, data: str) -> bool:
    pattern: str = r"[Cc]ircle"
    return bool(re.search(pattern, data))
