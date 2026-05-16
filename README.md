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



## Architecture



## Prerequisites
- typeguard



## Tasks
- [ ] Setup repo (Daniel)
- [ ] Language design (Daniel)
- [ ] Architecture (Daniel)
- [ ] Basic Classes (Daniel)
