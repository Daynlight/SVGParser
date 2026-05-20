from static_typing import typechecked


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
* typeguard: 4.5.2
* arcade: 3.3.3

# Authors
* Martyna Plenzer
* Daniel Stodulski
  """)
