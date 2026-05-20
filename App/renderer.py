from utils.static_typing import typechecked
from typing import Callable
import arcade

import App.config


@typechecked
class Renderer(arcade.Window):
  @typechecked
  def __init__(self):
    super().__init__(App.config.WINDOW_SIZE[0], App.config.WINDOW_SIZE[1], App.config.TITLE)
    arcade.set_background_color(App.config.BACKGROUND_COLOR)
    
    self._update_function: Callable[[float], None] = None
    self._fixed_update_function: Callable[[float], None] = None
    self._render_frame: Callable[[], None] = None

    arcade.schedule(self._fixed_update, App.config.FIXED_UPDATE_INTERVAL)


  def on_draw(self):
    self.clear()
    if self._render_frame is not None:
      self._render_frame()
  
  def on_update(self, delta_time):
    if self._update_function is not None:
      self._update_function(delta_time)
  
  def _fixed_update(self, delta_time):
    if self._fixed_update_function is not None:
      self._fixed_update_function(delta_time)
  

  @typechecked
  def run(self):
    arcade.run()

  @typechecked
  def setUpdateFunction(self, update_function: Callable[[float], None]):
    self._update_function = update_function 

  @typechecked
  def setFixedFunction(self, fixed_update_function: Callable[[float], None]):
    self._fixed_update_function = fixed_update_function

  @typechecked
  def setRenderFrame(self, render_frame_function: Callable[[], None]):
    self._render_frame = render_frame_function
