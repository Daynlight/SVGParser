# SVG Parser
SVG Parser is simple **python app** for **parsing** custom file format and showing it via ```arcade```. Inspired by ```svg``` and ```c++``` languages.


## Język Opisu Prostych Scen 2D
**Opis**: Stworzenie prostego, własnego języka do opisu wektorowych obiektów graficznych na płaszczyźnie.  
**Zakres**: Definiowanie komend typu ```CIRCLE x=10, y=20, r=5, color=red lub RECT w=100, h=50```. Parsowanie do struktur reprezentujących kształty.  
**Opcjonalnie**: generowanie rysunku (np. z użyciem biblioteki turtle lub zapis do SVG).  
**Czego można się nauczyć**: Obsługa i walidacja nazwanych parametrów, definiowanie struktury komend.



## TOC
- [SVG Parser](#svg-parser)
  - [Język Opisu Prostych Scen 2D](#język-opisu-prostych-scen-2d)
  - [TOC](#toc)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Building to executable](#building-to-executable)
    - [App](#app)
    - [Tests](#tests)
  - [Writing Tests](#writing-tests)
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
2. Run [```main.py```](main.py) with path to **file.svl**.



## Building to executable
### App
```bash
pyinstaller --onefile --windowed main.py
./dist/main
```
### Tests
```bash
pyinstaller --onefile tests.py
./dist/tests
```



## Writing Tests
1. Add your ```unit_test.py``` in ```Tests/Unit/```.
2. Make it inherit from ```testInterface```.
3. Write ```super``` with test name in constructor.
4. Add your tests as functions.
5. Add ```runAll()``` and run your tests from it.
6. Import your class tests in [tests.py](tests.py).
7. Run your tests in ```main()```.
8. For example look on [flags unit tests](Tests/Unit/flags.py)



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
2. We use ```from static_typing import typechecked``` to avoid issue with ```pyinstaller```.
3. We always use strict absolute **SRC_PATH** to assets (Should run from every location).
4. For ```release``` we build it via [**PyInstaller**](http://pyinstaller.org/en/stable/).



## Prerequisites [requirements](requirements.txt)
- **typeguard**: 4.5.2 - static typing.
- **arcade**: 3.3.3 - visuals.
- **pyinstaller**: 6.20.0 - executable builder.
- **rich**: 15.0.0 - terminal colors.



## Tasks

<details open>
<summary>🌟 Iteration 1 🌟</summary>

- [x] Setup repo (Daniel)
- [x] Architecture (Daniel)
- [x] Language design (Martyna)
- [x] Basic Renderer with arcade (Daniel)
- [x] Description for repo (Daniel).
- [x] Unit Tests structure (Daniel).
- [x] Tests workflow (Daniel).
- [x] Stage branch for testing (Daniel).
- [ ] Deployment workflow (Daniel).
- [ ] Community standards for repo (Daniel).
- [ ] Tickets (Daniel).
</details>

<details>
<summary>Iteration 2</summary>

- [ ] App class that stores data and provides functions for ```arcade``` renderer.
- [ ] Basic parser class with file validation and checking existence.
- [ ] Inherit Class for other object classes.
- [ ] Classes for ```Circle```, ```Rect```, ```Oval```.
- [ ] Examples.
</details>