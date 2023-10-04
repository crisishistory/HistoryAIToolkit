# Getting Started

## Prerequisites

TODO: check which versions of Python this works with

## For most Python users

As of now the project isn't on PyPI, so you'll have to install it from source. 

1. Fork the project on GitHub
2. Clone it to your computer
3. In your terminal, run:

```
python -m venv .venv
source .venv/bin/activate
pip install '.[test]'
```

## For Pyenv users

TODO

## Downloading the data

Get the data from [Kaggle](https://www.kaggle.com/c/ieee-fraud-detection/data) and put it in the `data` directory:

```
mkdir data
cd data
kaggle datasets download -d oral-history-audio-interviews
```


## Using the CLI

Once you've installed the project, you can run the command-line interface with:

```
(.venv) audrey@supercomputer HistoryAIToolkit % historyaitoolkit hello
Hello, world!
(.venv) audrey@supercomputer HistoryAIToolkit % historyaitoolkit todo 
TODO: Add another command here
```

Note: the CLI hasn't been connected to the rest of the project yet

TODO: implement commands to run the code from slicer.py and transcript.py
