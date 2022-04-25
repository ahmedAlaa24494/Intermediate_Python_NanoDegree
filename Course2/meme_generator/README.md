# Meme Generator

This app generates memes, Which can be created randomly or using Html form.

This app built on top of `Flask` framework 

## Setup

On your venv with a `Python 3.8.5` installation, navigate to the root directory and run `pip install -r requirements.txt`.
You also need to install `pdftotext` from here:
- Windows: https://www.xpdfreader.com/download.html
- Debian: `sudo apt-get update && sudo apt-get install -y xpdf`
- macOS: `brew install --cask pdftotext`

## Runing

To start the app navigate to `/src` and run `python app.py`. The frontend can be accessed at: http://127.0.0.1:5000/.

## Project Interface

The project consists of 2 basic modules:

- `QuoteEngine`
- `MemeEngine`

### Quote Engine

This module contains all the classes responsible for parsing quotes from different types of data (csv, docx, pdf & txt) and assigning them to a `QuoteModel`.

#### QuoteModel.py

Contains the main class `QuoteModel` that represents a single quote and holds the information of the body and the author of that specific quote.

#### IngestorInterface.py

Contains the main base class that further classes inherit from, to serve a certain functionality based on the type of data that is to be parsed. These are the following:

- `CSVIngestor` 
- `DocxIngestor` 
- `TxtIngestor` 
- `PDFIngestor` 

#### Ingestor.py

Contains `Ingestor`, a class that encapsulates the aforementioned derived classes' functionality and is responsible for the selection of the appropriate helper class for parsing the data. It finally returns a list of `QuoteModel` objects.

A typical example on the use of `Ingestor` is the following:

```python
from QuoteEngine.Ingestor import Ingestor

quotes = Ingestor.parse("./_data/DogQuotes/DogQuotesDOCX.docx")

# returns a list of QuoteModel objects
for quote in quotes:
    print(quote)
```

### MemeEngine

This module contains the `MemeGenerator` class that is responsible for generating a meme for a given image and a quote (text/body and author).

The use of `MemeGenerator` is pretty straightforward:

```python
from MemeGenerator import MemeGenerator

# intantiate a MemeGenerator with a given output directory
mg = MemeGenerator("memes/")

# generate meme from a given image and a quote
mg.make_meme(
    "src/_data/photos/dog/xander_2.jpg",
    body="Life's a bitch and then you die",
    author="Nas",
    width=400,
)
```

## Flask app

The Flask app consists of 2 components:

- meme.py
- app.py

### meme.py

This script encapsulates `MemeGenerator`'s functionality by additionally providing accessibility via the command line. At a command line you can run `python meme.py --help` for an explanation on how to invoke the script.

```console
usage: meme.py [-h] [--body BODY] [--author AUTHOR] [--path PATH]

Generate meme.

optional arguments:
  -h, --help       show this help message and exit
  --body BODY      Quote body.
  --author AUTHOR  Quote author.
  --path PATH      Image path.

```

### app.py

A typical Flask template script that provides the following endpoints for the user to interact with the frontent (http://127.0.0.1:5000/):

- `/`: The homepage that includes the main html form for random meme generation (`./src/templates/meme.html`). It picks a random image and a quote from `./src/_data/` and generates a meme with a `MemeGenerator` object.
- `/create`: Provides the ability to generate a custom meme from a given image url and a quote. Consists of the following stages:
  - `GET`: The GET request gets the user data from the html form that user completes (`./src/templates/meme.html`), consisting of the following areas: `image url`, `Quote Body` & `Quote Author`.
  - `POST`: Once the form is filled the POST request is used to send the user data to the server in order to finally generate the meme.
