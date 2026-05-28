from abc import ABC, abstractmethod
from utils.static_typing import typechecked



@typechecked
class Shape(ABC):
  @typechecked
  def __init__(self) -> None:
    pass

  @typechecked
  @abstractmethod
  def render(self) -> None:
    pass

  @typechecked
  @abstractmethod
  def parse(self, data: str) -> None:
    pass
