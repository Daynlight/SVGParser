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
    - [Via python](#via-python)
    - [By Executable](#by-executable)
  - [Supported Shapes](#supported-shapes)
    - [Colors](#colors)
  - [Language Syntaxes](#language-syntaxes)
  - [Camera Movement](#camera-movement)
  - [Building to executable](#building-to-executable)
    - [App](#app)
    - [Tests](#tests)
  - [Adding new Shapes](#adding-new-shapes)
  - [Architecture](#architecture)
    - [Start up](#start-up)
    - [Parsing file](#parsing-file)
    - [Integrity](#integrity)
    - [Implementation](#implementation)
  - [Writing Tests](#writing-tests)
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
### Via python
We provide python code with ```requirements.txt``` for self run and edition.
1. Create your **file.svl** or use one of [**Examples**](/Example)
2. Run [```main.py```](main.py) with path to **file.svl**.
    ```bash
    python3 main.py <Path to File>
    ```
### By Executable
We provide build in executable generated via ```PyInstaller``` that doesn't requires you to download all python libraries and easier to use. [Download](https://github.com/Daynlight/SVGParser/releases) with executable in name.
1. Create your **file.svl** or use one of [**Examples**](/Example)
2. Run from shell
    ```bash
    ./SVGParser <Path to File>
    ```



## Supported Shapes
- ```Circle(x = 20, y = 300, r = 80, c = #A5FF31);```
- ```Ellipse(x = 20, y = 300, rx = 50, ry = 80, c = #A5FF31);```
- ```Line(x1 = 500, y1 = 400, x2 = 420, y2 = 200, w = 8, color = #2C3E50);```
- ```Rectangle(x=100,y=200,w=30,h=400);```

### Colors
- In ```HEX``` format. 
- ```red```.
- ```blue```.
- ```green```.
- ```azure```.
- ```black```.
- ```white```.
- ```yellow```.
- ```pink```.
- ```purple```.
- ```orange```.
- ```brown```.
- ```gray```.



## Language Syntaxes
1. Each entry is separated via ```;```;
2. Each object is created via keyword of struct ```Name(parameters)``` separated by ```,```.
3. Example:
    ```cpp
    Circle(x = 20, y = 300, r = 80, c = #A5FF31);
    ```



## Camera Movement
- Move up: W
- Move down: S
- Move left: A
- Move right: D 
- Move zoom in: P
- Move zoom out: I



## Building to executable
### App
  ```bash
  pyinstaller --onefile --windowed main.py
  ./dist/main Examples/test.svl
  ```

### Tests
  ```bash
  pyinstaller --onefile tests.py
  ./dist/tests
  ```



## Adding new Shapes
1. Copy [shape](App/shapes/shape.py) and edit for new provide all operations.
2. Register new shape in [shape_register](App/shapes/shapes_register.py).
3. Add new [Example](Examples/) where you show how to use it.
4. Cover parsing popery.
5. Update [Supported Shapes](#supported-shapes).
6. Add [unit tests](Tests/Unit/) for your shape. 



## Architecture
### Start up
1. On start we provide path to **file.svl**.
2. We then check if ```path``` is correct and file exist.
3. We initialize renderer and window (**arcade**).
4. We parsee **file.svl** and create objects in ```object register```.
5. Every implemented object is inherit from ```Shape``` interface. 
6. We render our objects.

### Parsing file
1. We parse entries in file and adds them to ```object register```.
2. We use ```object register``` to render on scene.
3. If entry is invalid we print error with line and skip object.
4. We save this objects in ```object register```.

### Integrity
1. We check ```last time write``` of file.
2. If something had changed we.
   1. We remove all objects.
   2. We reparse **file.svl**.

### Implementation
1. We use ```typeguard``` for hard typing and checking variables.
2. We use ```from static_typing import typechecked``` to avoid issue with ```pyinstaller```.
3. We use [**PyInstaller**](http://pyinstaller.org/en/stable/) for building executable.



## Writing Tests
1. Add your ```unit_test.py``` in ```Tests/Unit/```.
2. Make it inherit from ```testInterface```.
3. Write ```super``` with test name in constructor.
4. Add your tests as functions.
5. Add ```runAll()``` and run your tests from it.
6. Import your class tests in [tests.py](tests.py).
7. Run your tests in ```main()```.
8. For example look on [flags unit tests](Tests/Unit/flags.py)
9. Run tests via python
    ```bash
    python3 tests.py
    ```
10. Run tests via builded executable
    ```bash
    pyinstaller --onefile tests.py
    ./dist/tests
    ```



## Prerequisites [requirements](requirements.txt)
- **python**: 3.13.5 - programming language.
- **typeguard**: 4.5.2 - static typing.
- **arcade**: 3.3.3 - visuals.
- **pyinstaller**: 6.20.0 - executable builder.
- **rich**: 15.0.0 - terminal colors.
- **numpy**: 2.2.6 - mathematical operations.
- **re**: 2.2.1 - regex.



## Tasks
<details>
<summary>Iteration 1</summary>

- [x] Language design (Martyna)
- [x] Setup repo (Daniel)
- [x] Architecture (Daniel)
- [x] Basic Renderer with arcade (Daniel)
- [x] Description for repo (Daniel).
- [x] Unit Tests structure (Daniel).
- [x] Tests workflow (Daniel).
- [x] Stage branch for testing (Daniel).
- [x] Deployment workflow (Daniel).
- [x] Tickets (Daniel).
</details>

<details>
<summary>Iteration 2</summary>

- [x] Add ```main.py``` with parsing arguments and starting app (Daniel).
- [x] Add ```App/app.h``` main windowed application using ```arcade``` (Daniel).
- [x] Add camera movement (Daniel).
- [x] Abstract Shape Class (Daniel).
- [x] Class for ```Circle Shape``` inherit from **Abstract Shape Class** (Daniel).
- [x] Unit Tests for ```argv``` parsing via ```re``` (Daniel).
- [x] Add ```Parser class``` in ```parser.py``` and register in main app (Daniel).
- [x] Add ```Circle``` detection and parsing (Daniel).
- [x] ```Lsat Time Write``` detection and regeneration (Daniel).
</details>

<details>
<summary>Iteration 3</summary>

- [x] Add ```Rectangle Shape``` inherit from **Abstract Shape Class** (Martyna).
- [x] Add ```Rectangle``` detection and parsing (Martyna).
- [x] Add ```Elipse Shape``` inherit from **Abstract Shape Class** (Martyna).
- [x] Add ```Elipse``` detection and parsing (Martyna).
- [x] Add ```Line Shape``` inherit from **Abstract Shape Class** (Martyna).
- [x] Add ```Line``` detection and parsing (Martyna).
- [x] Add color parsing (Martyna).
- [x] Examples (Martyna).
- [x] Documentation for Writing files (Daniel Martyna).
</details>