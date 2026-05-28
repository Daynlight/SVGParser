from utils.static_typing import typechecked
from enum import IntFlag, auto 
from pathlib import Path
import re
import sys

from App.help_command import printHelp



class Flags(IntFlag):
  NONE = 0
  HELP = auto()
  DEBUG = auto()



@typechecked
def fetchFlags(argv: list[str]) -> Flags:
  help_pattern = re.compile(r'^(-h|--help)$')
  debug_pattern = re.compile(r'^(-d|--debug)$')
  
  flags = Flags.NONE
  for arg in argv:
    if help_pattern.match(arg):
      flags |= Flags.HELP
    if debug_pattern.match(arg):
      flags |= Flags.DEBUG
          
  return flags



@typechecked
def getPathFromArgs(argv: list[str]) -> Path:
  path_pattern = re.compile(r'^(?!-).+\.svl$')
  
  for arg in argv:
    if path_pattern.match(arg):
      path = Path(arg).resolve()

      if path.is_file():
        return path

      raise FileNotFoundError(f"{path} does not exist.")
          
  raise ValueError("No valid path found in arguments.")



@typechecked
def parseArgv(argv: list[str]) -> tuple[Path, Flags]:
  if(argv is None or len(argv) <= 0):
    raise ValueError("No path provided") 

  enabled_flags: Flags = fetchFlags(argv)
  if(enabled_flags & Flags.HELP): 
    printHelp()
    sys.exit(0)

  path_to_file: Path = getPathFromArgs(argv)

  return (path_to_file, enabled_flags)
