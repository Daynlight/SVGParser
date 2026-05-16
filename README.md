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
1. Each object is separated via ```;```;
2. We allows functions provided in ```{``` and closed via ```}```.
3. Main entry is provided via ```main``` function.
4. Includes of other file is operate via ```include``` and copies only once content of **included file** to main function.



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
3. We create map from function where it was created to object.

### Integrity
1. For each function we create unique hash.
2. We create dependency graph for functions.
3. We check ```last time write``` of file.
4. If something had changed we calculate new hashes and and compare with previous.
5. We use dependency graph for functions that contains changed functions.
6. We remove all object that was created via function hash.
7. We creates new objects that changed.

### Implementation
1. We use typeguard for hard typing.
2. We always use config strict **PATH**.



## Prerequisites
- typeguard



## Tasks
- [ ] Setup repo (Daniel)
- [ ] Language design (Daniel)
- [ ] Architecture (Daniel)
- [ ] Basic Classes (Daniel)
