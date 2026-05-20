from typeguard import typechecked
from enum import IntFlag, auto 


class Flags(IntFlag):
  HELP = auto()
  DEBUG = auto()


@typechecked
def parseFlags(argv: list[str]) -> Flags:
  flags: Flags = Flags(0)

  for i in range(len(argv)):
    if(argv[i] == "--help" or argv[i] == "-h"): flags |= Flags.HELP
    if(argv[i] == "--debug" or argv[i] == "-d"): flags |= Flags.DEBUG

  return flags
