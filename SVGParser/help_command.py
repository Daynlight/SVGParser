from typeguard import typechecked
import sys


@typechecked
def printHelp():
  print("""
===================
==== SVDParser ====
===================
# Commands
* -h/--help - show this info.
* -d/--debug - turns debug mode

# Requirements
* typeguard

# Authors
* Martyna Plenzer
* Daniel Stodulski
  """)
