from static_typing import typechecked
from pathlib import Path
import sys

import flags
import renderer


@typechecked
def update(dt: float):
  print("Update:", dt)

@typechecked
def fixed_update(dt: float):
  print("Fixed:", dt)

@typechecked
def render_frame():
  print("Render Frame")


@typechecked
def main(argv: list[str]):
  if(argv is None or len(argv) <= 0):
    raise Exception("No path provided") 

  enabled_flags: flags.Flags = flags.parseFlags(argv)

  if(argv[-1][0] == '-'):
    raise Exception("No path provided") 
  
  path_to_file: str = str(Path(argv[-1]).resolve())

  window: renderer.Renderer = renderer.Renderer()
  window.setUpdateFunction(update)
  window.setFixedFunction(fixed_update)
  window.setRenderFrame(render_frame)
  window.run()


main(sys.argv[1:])
