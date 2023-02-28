# Python AI Othello Player Project
Programed at Atomic Objects AI Games in October, 2022 with [Dat Nguyen](https://github.com/imtiendat0311) and [Don Nguyen](https://github.com/nhutu1911)

We participated in [Atomic Object](https://www.atomicobject.com/)'s 2022 AI Games: an 8 hour code-a-thon in teams of 2-3 people. We were given 8 hours to design an AI Othello player. 
We did not all know each other at the start of this challenge. We had to learn to work together to do our best work. It was a learning experience in programming ability as well as teamwork in a fast paced environment.

This is our one day project:

## To Run The Project
1. open Othello_Game_Server in Command Line or Terminal.
2. make sure you have at least java v17
        (type `java -version` in Terminal to check your Java version)
4. type: `java -jar othello.jar --p1-type remote --p2-type random --wait-for-ui`
    this starts the Othello server
4. open a new terminal tab in the AI_GAMES folder window and type `python player.py` (or `python player.py 1337` if that doesn't work)
    this starts our attempt at a minimax AI player
5. open your browser and search http://localhost:8080 to open the Othello board UI

## Files Explained
* first_move_picker.py was our first completed AI.  It creates a list of all valid moves, then picks the first one.

* player.py was our attempt to creat an AI that evaluated all moves and would pick the one that gave them the most points (depth of search 1).  We thought we got this working and moved on to creating an AI player using a minimax algorithm, but for some reason this player did not work when we tested it later.  Either we accidently broke it with edits and didn't notice or the player never worked properly, and just one the game we tested it with.

* player1.py : our attempt at a minimax search algorithm to select the best moves.  We finished writing the algorithm, but did not have enough time to get it running :(


## Instructions
To run the client, run: `python client.py [optional port] [optional hostname]`

To run all tests, run `python -m unittest`
To run all tests in "test.py" tests, run `python -m unittest test`
To run the TestGetMove class in "test.py", run `python -m unittest test.TestGetMove`
To run the test_get_move_returns_a_valid_move test case in the TestGetMove class in "test.py", run `python -m unittest test.TestGetMove.test_get_move_returns_a_valid_move`

## Recommended Software
* Python 3.7.0. (Disclaimer: developed with Python 3.7.0, tested with Python 2.7.10 - not guaranteed to work with other versions)
* Java version 17
* [Pyenv](https://github.com/pyenv/pyenv)
