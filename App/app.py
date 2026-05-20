from utils.static_typing import typechecked
from pathlib import Path
import sys

import App.help_command
import App.flags
import App.renderer


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
def app(argv: list[str]):
  if(argv is None or len(argv) <= 0):
    raise Exception("No path provided") 

  enabled_flags: App.flags.Flags = App.flags.parseFlags(argv)
  if(enabled_flags & App.flags.Flags.HELP): 
      App.help_command.printHelp()
      sys.exit(0)

  if(argv[-1][0] == '-'):
    raise Exception("No path provided") 
  
  path_to_file: str = str(Path(argv[-1]).resolve())

  window: App.renderer.Renderer = App.renderer.Renderer()
  window.setUpdateFunction(update)
  window.setFixedFunction(fixed_update)
  window.setRenderFrame(render_frame)
  window.run()
