from utils.static_typing import typechecked
from rich import print
import sys

from App.app import App
from App.flags import parseArgv, Flags
from App.help_command import printHelp



@typechecked
def main(argv: list[str]) -> None:
  try:
    path_to_file, enabled_flags = parseArgv(argv)
  except (FileNotFoundError, ValueError) as e:
    print(f"[red]{e}[/red]")
    printHelp()
    sys.exit(0)

  if(enabled_flags & Flags.HELP): 
    printHelp()
    sys.exit(0)

  app: App = App(path_to_file, enabled_flags)
  app.run()



main(sys.argv[1:])
