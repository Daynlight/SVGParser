from utils.static_typing import typechecked
import sys

from App.app import App
from App.flags import parseArgv



@typechecked
def main(argv: list[str]) -> None:
  path_to_file, enabled_flags = parseArgv(argv)

  app: App = App(path_to_file, enabled_flags)
  app.run()



main(sys.argv[1:])
