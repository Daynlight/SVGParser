from utils.static_typing import typechecked
from enum import IntFlag, auto
from pathlib import Path
import numpy as np
import arcade

from App.config import WINDOW_SIZE, TITLE, BACKGROUND_COLOR, FIXED_UPDATE_INTERVAL, MOVE_VELOCITY, ZOOM_SPEED, ZOOM_BOUND, MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT, MOVE_ZOOM_IN, MOVE_ZOOM_OUT
from App.flags import Flags
from App.parser.parser import Parser
from App.shapes.shape import Shape
import App.shapes.shapes_register



@typechecked
class KEYS_DOWN(IntFlag):
  NONE = 0
  UP = auto()
  DOWN = auto()
  LEFT = auto()
  RIGHT = auto()
  ZOOM_IN = auto()
  ZOOM_OUT = auto()



@typechecked
class App(arcade.Window):
  @typechecked
  def __init__(self, path_to_file: Path, enabled_flags: Flags) -> None:
    super().__init__(WINDOW_SIZE[0], WINDOW_SIZE[1], TITLE)
    arcade.set_background_color(BACKGROUND_COLOR)
    
    self._camera: arcade.camera = arcade.camera.Camera2D()
    self._keys: KEYS_DOWN = KEYS_DOWN.NONE

    arcade.schedule(self.fixed_update, FIXED_UPDATE_INTERVAL)
    
    self._enabled_flags: Flags = enabled_flags

    self._parser: Parser = Parser(path_to_file)
    self._shapes: list[Shape] = []


  @typechecked
  def run(self) -> None:
    arcade.run()


  @typechecked
  def on_draw(self) -> None:
    self.clear()
    self._camera.use()

    for shape in self._shapes:
      shape.render()


  @typechecked
  def fixed_update(self, delta_time: float) -> None:
    self._cameraMovement(delta_time)
    self._zoomUpdate(delta_time)
    if(self._parser.observe()):
      self._shapes.clear()
      self._shapes = self._parser.getShapes()


  @typechecked
  def on_key_press(self, key: arcade.key, modifiers: any) -> None:
    if key == MOVE_UP:
      self._keys |= KEYS_DOWN.UP
    if key == MOVE_DOWN:
      self._keys |= KEYS_DOWN.DOWN
    if key == MOVE_LEFT:
      self._keys |= KEYS_DOWN.LEFT
    if key == MOVE_RIGHT:
      self._keys |= KEYS_DOWN.RIGHT
    if key == MOVE_ZOOM_IN:
      self._keys |= KEYS_DOWN.ZOOM_IN
    if key == MOVE_ZOOM_OUT:
      self._keys |= KEYS_DOWN.ZOOM_OUT


  @typechecked
  def on_key_release(self, key: arcade.key, modifiers: any) -> None:
    if key == MOVE_UP:
      self._keys &= ~KEYS_DOWN.UP
    if key == MOVE_DOWN:
      self._keys &= ~KEYS_DOWN.DOWN
    if key == MOVE_LEFT:
      self._keys &= ~KEYS_DOWN.LEFT
    if key == MOVE_RIGHT:
      self._keys &= ~KEYS_DOWN.RIGHT
    if key == MOVE_ZOOM_IN:
      self._keys &= ~KEYS_DOWN.ZOOM_IN
    if key == MOVE_ZOOM_OUT:
      self._keys &= ~KEYS_DOWN.ZOOM_OUT


  @typechecked
  def _cameraMovement(self, delta_time: float) -> None:
    move_vector: np.ndarray = np.array([0, 0], dtype=float)

    if self._keys & KEYS_DOWN.UP:
      move_vector[1] += 1
    if self._keys & KEYS_DOWN.DOWN:
      move_vector[1] -= 1
    if self._keys & KEYS_DOWN.LEFT:
      move_vector[0] -= 1
    if self._keys & KEYS_DOWN.RIGHT:
      move_vector[0] += 1

    move_vector_norm: float = np.linalg.norm(move_vector)
    if(move_vector_norm != 0):
      move_vector: np.ndarray = (move_vector / move_vector_norm) * MOVE_VELOCITY * delta_time
      camera_pos: np.ndarray = np.array([self._camera.position.x, self._camera.position.y], dtype=float)
      camera_pos: np.ndarray = camera_pos + move_vector
      self._camera.position = (camera_pos[0], camera_pos[1])


  @typechecked
  def _zoomUpdate(self, delta_time: float) -> None:
    if(self._keys & KEYS_DOWN.ZOOM_OUT):
      self._camera.zoom -= ZOOM_SPEED * delta_time
      if self._camera.zoom < ZOOM_BOUND[0]:
        self._camera.zoom = ZOOM_BOUND[0]

    if(self._keys & KEYS_DOWN.ZOOM_IN):
      self._camera.zoom += ZOOM_SPEED * delta_time
      if self._camera.zoom > ZOOM_BOUND[1]:
        self._camera.zoom = ZOOM_BOUND[1]
