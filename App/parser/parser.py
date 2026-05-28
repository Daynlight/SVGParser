from utils.static_typing import typechecked
from pathlib import Path
from rich import print

from App.shapes.shape import Shape



@typechecked
class Parser:
  @typechecked
  def __init__(self, path_to_file: Path) -> None:
    self._path_to_file: Path = path_to_file
    self._last_time_write: float = 0.0


  @typechecked
  def observe(self) -> bool:
    new_last_time_write: float = self._path_to_file.stat().st_mtime
    changed: bool = self._last_time_write != new_last_time_write
    self._last_time_write = new_last_time_write
    return changed
  

  @typechecked
  def getShapes(self) -> list[Shape]:
    content: str = self._getFileContent()
    shapes: list[Shape] = []

    for entry, shape_data in enumerate((s.strip() for s in content.split(";") if s.strip()), 1):
      found = False
      for cls in Shape.__subclasses__():
        if cls.validate(shape_data):
          instance = cls()
          instance.parse(shape_data, entry)
          shapes.append(instance)
          found = True
          break
      
      if not found:
        print(f"[red]Warning: No shape type matched data on entry {entry}: {shape_data}[/red]")

    return shapes


  @typechecked
  def _getFileContent(self):
    content: str = self._path_to_file.read_text(encoding='utf-8')
    return content
