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
pip install -e '.[test]'
```

## For Pyenv users

TODO

## Downloading the data

At minimum you'll need a short audio file to test the code with, which can be:

* Something you record yourself, or
* A snippet of an audio oral history interview such as [this mp3](https://github.com/audreyfeldroy/HistoryAIToolkit/blob/2ea4f8fc974783f996dd367c4110b50d1185a972/data/sampled-2-Martine%2BBarrat_FINAL.mp3), or
* An audio file from the [Oral History Audio Interviews](https://www.kaggle.com/datasets/audreyfeldroy/oral-history-audio-interviews) dataset on Kaggle, if you want a longer file

### Very Optional: For Advanced Users

Most people won't need to do this, but if you need 1 GB of real oral history interviews, these commands download the entire dataset from Kaggle and put it in the `data` directory:

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
