# Python AI Othello Player Project
Programed at Atomic Objects AI Games on Saturday October 29th with Rob Don

The AI games was a code-a-thon to build an AI Othello player, this is our one day project.


To Run The Project:
1. open Othello_Game_Server in command line.
2. make sure you have at least java v17
3. type: `java -jar othello.jar --p1-type remote --p2-type random --wait-for-ui`
    this starts the Othello server
4. open a new terminal tab in the AI_GAMES folder window and type `python player.py` (or `python player.py 1337` if that doesn't work)
    this starts our attempt at a minimax AI player
5. open your browser and search http://localhost:8080 to open the Othello board UI




Disclaimer: developed with Python 3.7.0, tested with Python 2.7.10 - not guaranteed to work with other versions

## Instructions
To run the client, run: `python client.py [optional port] [optional hostname]`

To run all tests, run `python -m unittest`
To run all tests in "test.py" tests, run `python -m unittest test`
To run the TestGetMove class in "test.py", run `python -m unittest test.TestGetMove`
To run the test_get_move_returns_a_valid_move test case in the TestGetMove class in "test.py", run `python -m unittest test.TestGetMove.test_get_move_returns_a_valid_move`

## Recommended Software
* Python 3.7.0
* Java version 17
* [Pyenv](https://github.com/pyenv/pyenv)
