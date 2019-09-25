# AI Assignment 1

## Compilation and Set Up
None Needed, just have Python 3.7 installed. 

**I am using features from 3.7, it will not run on earlier versions of Python**

## Before Running

Before running you may want to change some configuration settings, those are in `config.py` and are explained below.

Key             | Type          | Definition
----------------|---------------|----------------------------------------------------------------------------------------------
MAX_ITERS       | Integer       | The maximimum number of iterations the program runs before quiting
ROWS            | Integer       | The number of rows for the tile game
COLS            | Integer       | The number of columns for the tile game
SIZE            | Integer       | **Do not modify**
INPUT_FROM_FILE | {True, False} | Reads input from a file instead of from user input
USE_STR_IDS     | {True, False} | Determines whether the program uses strings in the unique identifiers. *I found this to be useful to read the output, but it is off by default since the assignment specifies integers*
SHOW_BOARD      | {True, False} | Whether or not the program shows the board on each step.

If you enable INPUT_FROM_FILE, you should put the arrays in `input.txt` before running, one on each line.

## Running
In the folder where you extracted this zip, run `python .\aja_assignment_1.py`

You will be by default, prompted for the start state and the end state.
