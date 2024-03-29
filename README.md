# Python AI Othello Player Project
Programed at Atomic Objects AI Games on Saturday October 29th with Dat Nguyen and Don Nguyen

The AI games was a code-a-thon to build an AI Othello player, this is our one day project.

## To Run The Project:
1. open Othello_Game_Server in Command Line or Terminal.
2. make sure you have at least java v17
        (type `java -version` in Terminal to check your Java version)
4. type: `java -jar othello.jar --p1-type remote --p2-type random --wait-for-ui`
    this starts the Othello server
4. open a new terminal tab in the AI_GAMES folder window and type `python player.py` (or `python player.py 1337` if that doesn't work)
    this starts our attempt at a minimax AI player (it ended up not quite working, but oh well, we tried!)
5. open your browser and search http://localhost:8080 to open the Othello board UI

## Files Explained:
- first_move_picker.py was our first completed AI.  It creates a list of all valid moves, then picks the first one.

- player.py was our attempt to creat an AI that evaluated all moves and would pick the one that gave them the most points (depth of search 1).  We thought we got this working and moved on to creating an AI player using a minimax algorithm, but for some reason this player did not work when we tested it later.  Either we accidently broke it with edits and didn't notice or the player never worked properly, and just one the game we tested it with.

-player1.py : our attempt at a minimax search algorithm to select the best moves.  We finished writing the algorithm, but did not have enough time to get it running :(


Disclaimer: developed with Python 3.7.0, tested with Python 2.7.10 - not guaranteed to work with other versions

## Recommended Software
* Python 3.7.0
* Java version 17
* [Pyenv](https://github.com/pyenv/pyenv)
