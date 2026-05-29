from abc import ABC, abstractmethod
from utils.static_typing import typechecked



@typechecked
class Shape(ABC):
  @classmethod
  def getAllShapes(cls) -> list[type['Shape']]:
    return cls.__subclasses__()
  
  
  @typechecked
  def __init__(self) -> None:
    pass


  @typechecked
  @abstractmethod
  def render(self) -> None:
    pass


  @typechecked
  @abstractmethod
  def parse(self, data: str, entry: int) -> bool:
    return False


  @typechecked
  @classmethod
  @abstractmethod
  def validate(self, data: str) -> bool:
    return False
