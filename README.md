# Chess Games Data Generator

This project is a chess games data generator that I created to work on some personal projects. It can generate random chess games in text format on top-level engines such as Stockfish, lc0, and Komodo. feel free to use this data for your purposes, or to push more games.

## Setup Guide

```bash
# create virtual Python env
$ python -m venv env
# Connect to the env
$ source env/Scripts/activate
# run the generator
$ python main.py
```

You can find all the games' data in `data` where it's arranged in the file according to the time of thinking, for example, data/0.1 has all the games that ran on 0.1 engine thinking time.
