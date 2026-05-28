from utils.static_typing import typechecked
from rich import print



@typechecked
def printHelp() -> None:
  print("""[green]
===================
==== SVGParser ====
===================[/green]
[blue]# Usage[/blue]
[white]1. Prepare your file (.svl)[/white]
[white]2. Run the application:[/white]
        
[blue]## Compiled Binary[/blue]
  [yellow]./SVGParser <path_to_svl> <flags>[/yellow]

[blue]## Python Source[/blue]
  [yellow]python3 main.py <path_to_svl> <flags>[/yellow]

        
[blue]# Commands[/blue]
* -h/--help - show this info.
* -d/--debug - turns debug mode


[blue]# Camera Movement[/blue]
- Move up: W
- Move down: S
- Move left: A
- Move right: D 
- Move zoom in: P
- Move zoom out: I
        
        
[blue]# Requirements[/blue]
* typeguard: 4.5.2 - static typing.
* arcade: 3.3.3 - visuals.
* pyinstaller: 6.20.0 - executable builder.
* rich: 15.0.0 - terminal colors.
* numpy: 2.2.6 - mathematical operations.

        
[blue]# Authors[/blue]
* Martyna Plenzer
* Daniel Stodulski
  """)
