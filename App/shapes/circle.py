from utils.static_typing import typechecked
import arcade

from App.shapes.shape import Shape



@typechecked
class Circle(Shape):
  @typechecked
  def __init__(self, position: tuple[int, int], radius: int) -> None:
    self._position: tuple[int, int] = position
    self._radius: int = radius
    self._color: arcade.color = arcade.color.AZURE


  @typechecked
  def render(self) -> None:
    arcade.draw_circle_filled(self._position[0], self._position[1], self._radius, self._color)


  @typechecked
  def parse(self, data: str) -> None:
    pass
