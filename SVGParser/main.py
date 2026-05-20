from typeguard import typechecked
from pathlib import Path
import sys

import flags
import help_command


@typechecked
def main(argv: list[str]):
  if(len(argv) < 1): raise Exception("No path provided") 

  enabled_flags: flags.Flags = flags.parseFlags(argv[:-1])
  
  if(enabled_flags & flags.Flags.HELP): 
    help_command.printHelp()
    sys.exit(0)
  
  path_to_file: str = str(Path(argv[-1]).resolve())

  print(path_to_file)


main(sys.argv[1:])
