# SVD Parser



## Język Opisu Prostych Scen 2D
Opis: Stworzenie prostego, własnego języka do opisu wektorowych obiektów graficznych na płaszczyźnie.
Zakres: Definiowanie komend typu CIRCLE x=10, y=20, r=5, color=red lub RECT w=100, h=50. Parsowanie do struktur reprezentujących kształty. Opcjonalnie: generowanie rysunku (np. z użyciem biblioteki turtle lub zapis do SVG).
Czego można się nauczyć: Obsługa i walidacja nazwanych parametrów, definiowanie struktury komend.



## TOC
- [SVD Parser](#svd-parser)
  - [Język Opisu Prostych Scen 2D](#język-opisu-prostych-scen-2d)
  - [TOC](#toc)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Language Syntaxes](#language-syntaxes)
    - [Supported Objects](#supported-objects)
  - [Architecture](#architecture)
    - [Start up](#start-up)
    - [Includes](#includes)
    - [Parsing file](#parsing-file)
    - [Integrity](#integrity)
    - [Implementation](#implementation)
  - [Prerequisites](#prerequisites)
  - [Tasks](#tasks)



## Installation
1. You have to install [python3](https://www.python.org/downloads/)

2. Create virtual environment
```bash
python3 -m venv .venv
```

3. Open virtual environment
   - Unix / macOS
   ```bash
   source .venv/bin/activate
   ```
   - Windows
    ```bash
    .venv\Scripts\activate.bat
    ```

4. Install ```requirements.txt```
```bash
pip install -r requirements.txt
```



## Usage
1. Create your **config file** or use one of [**Examples**](/Example)
2. Run [```main.py```](SVDParser/main.py) with path to **config file**.



## Language Syntaxes
1. Main entry is provided via ```main``` function.
2. Each object is separated via ```;```;
3. Includes of other file is operate via ```include``` and copies only once content of **included file** to main function.
```cpp
include "hello";
```
4. We allows functions.
```cpp
fun drawCircle(x, y){
  Circle(x, y, 5);
}
```
5. Support for arithmetic operations ```+```, ```-```, etc.
6. We calculate hash for each function and object.
7. Arithmetic operations works before generating graph.
8. We create dependency direct graph for functions and objects.



### Supported Objects
- ```Circle(x, y, r);```
- ```Rect(x, y, w, h);```
- ```Oval(x, y, a, b);```



## Architecture
### Start up
1. On start we provide path to **config file**.
2. We then check if ```path``` is correct and file exist.
3. We initialize renderer and window.

### Includes
1. Before parsing we include all outside files only once.
2. If multiple functions with the same name occurs we throw error.

### Parsing file
1. We parse entries in file and create object on scene.
2. If entry is invalid we print error and skip object.
3. We create map from object hash to real object.

### Integrity
1. For each function we create unique hash.
2. We create dependency directed graph for functions.
3. We check ```last time write``` of file.
4. If something had changed we calculate new hashes and and compare with previous.
5. We use dependency directed graph for functions and objects that contains changed.
6. We traverse through directed graph down to remove old object.
7. We creates new objects that changed.

### Implementation
1. We use typeguard for hard typing.
2. We always use strict absolute **PATH** to project.



## Prerequisites
- typeguard



## Tasks
- [x] Setup repo (Daniel)
- [x] Architecture (Daniel)
- [ ] Language design (Daniel)
- [ ] Basic Classes (Daniel)
