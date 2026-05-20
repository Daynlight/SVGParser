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
    - [Parsing file](#parsing-file)
    - [Integrity](#integrity)
    - [Implementation](#implementation)
  - [Prerequisites requirements](#prerequisites-requirements)
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
1. Create your **file.svl** or use one of [**Examples**](/Example)
2. Run [```main.py```](SVDParser/main.py) with path to **file.svl**.



## Language Syntaxes
1. Each object is separated via ```;```;
2. Each object is created via keyword of struct ```Circle``` and parameters like ```x=25, y = 30``` separated by ```,```.
3. Example:
```cpp
Circle(r=45, x=25, y=30, fill=#5524FF);
```



### Supported Objects
- ```Circle(x, y, r);```
- ```Rect(x, y, w, h);```
- ```Oval(x, y, a, b);```



## Architecture
### Start up
1. On start we provide path to **file.svl**.
2. We then check if ```path``` is correct and file exist.
3. We parsee **file.svl** and create objects in register.
4. Every implemented object is inherit from interface. 
5. We initialize renderer and window.
6. We render our objects.

### Parsing file
1. We parse entries in file and create object on scene.
2. If entry is invalid we print error and skip object.
3. We save this objects in register.

### Integrity
3. We check ```last time write``` of file.
4. If something had changed then.
   1. We remove all objects.
   2. We parse **file.svl**.

### Implementation
1. We use typeguard for hard typing.
2. We always use strict absolute **PATH** to project.



## Prerequisites [requirements](requirements.txt)
- **typeguard**: 4.5.2
- **arcade**: 3.3.3



## Tasks
- [x] Setup repo (Daniel)
- [x] Architecture (Daniel)
- [x] Language design (Martyna)
- [ ] Basic Classes (Daniel)
