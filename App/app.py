from utils.static_typing import typechecked
from pathlib import Path
import arcade

from App.config import WINDOW_SIZE, TITLE, BACKGROUND_COLOR, FIXED_UPDATE_INTERVAL
from App.flags import Flags



@typechecked
class App(arcade.Window):
  @typechecked
  def __init__(self, path_to_file: Path, enabled_flags: Flags) -> None:
    super().__init__(WINDOW_SIZE[0], WINDOW_SIZE[1], TITLE)
    arcade.set_background_color(BACKGROUND_COLOR)
    arcade.schedule(self.fixed_update, FIXED_UPDATE_INTERVAL)
    self._path_to_file: Path = path_to_file
    self._enabled_flags: Flags = enabled_flags

  def on_draw(self) -> None:
    self.clear()
  
  def on_update(self, delta_time) -> None:
    pass
  
  def fixed_update(self, delta_time) -> None:
    pass

  @typechecked
  def run(self) -> None:
    arcade.run()
