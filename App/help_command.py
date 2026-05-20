from utils.static_typing import typechecked
from rich import print


@typechecked
def printHelp():
  print("""[green]
===================
==== SVDParser ====
===================[/green]
[blue]# Commands[/blue]
* -h/--help - show this info.
* -d/--debug - turns debug mode

[blue]# Requirements[/blue]
* typeguard: 4.5.2 - static typing.
* arcade: 3.3.3 - visuals.
* pyinstaller: 6.20.0 - executable builder.
* rich: 15.0.0 - terminal colors.

[blue]# Authors[/blue]
* Martyna Plenzer
* Daniel Stodulski
  """)
