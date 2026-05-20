from typeguard import typechecked
from pathlib import Path
import sys

import flags


@typechecked
def main(argv: list[str]):
  if(len(argv) < 1):
    raise Exception("No path provided") 

  enabled_flags: flags.Flags = flags.parseFlags(argv)

  if(argv[-1][0] == '-'):
    raise Exception("No path provided") 
  
  path_to_file: str = str(Path(argv[-1]).resolve())

  print(path_to_file)


main(sys.argv[1:])
