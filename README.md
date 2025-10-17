# Tic-Tac-Toe

## The latest version of Python you are advised to use in this project is Python 3.12.

Using Minimax Algorithm, we will implement an AI to play Tic-Tac-Toe optimally.

Understanding
There are two main files in this project: runner.py and tictactoe.py. tictactoe.py contains all of the logic for playing the game, and for making optimal moves. runner.py contains all of the code to run the graphical interface for the game. 

First, we define three variables: X, O, and EMPTY, to represent possible moves of the board.

The function initial_state returns the starting state of the board. For this problem, we’ve chosen to represent the board as a list of three lists (representing the three rows of the board), where each internal list contains three values that are either X, O, or EMPTY. 

Specification

The player function takes a board state as input, and return which player’s turn it is (either X or O). In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.

Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).

The actions function returns a set of all of the possible actions that can be taken on a given board.

Each action is represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).

Possible moves are any cells on the board that do not already have an X or an O in them.

Any return value is acceptable if a terminal board is provided as input.

The result function takes a board and an action as input, and returns a new board state, without modifying the original board.

If action is not a valid action for the board, your program raises an exception.
The returned board state is the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.
Importantly, the original board is left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in board itself is not a correct implementation of the result function. You’ll likely want to make a deep copy of the board first before making any changes.
The winner function accepts a board as input, and return the winner of the board if there is one.
If the X player has won the game, your function returns X. If the O player has won the game, your function returns O.
One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).
If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function returns None.
The terminal function accepts a board as input, and return a boolean value indicating whether the game is over.
If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function returns True.
Otherwise, the function returns False if the game is still in progress.
The utility function accepts a terminal board as input and output the utility of the board.
If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.
You may assume utility will only be called on a board if terminal(board) is True.
The minimax function takes a board as input, and return the optimal move for the player to move on that board.
The move returned is the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
If the board is a terminal board, the minimax function returns None.
