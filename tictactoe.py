"""
Tic Tac Toe Player
"""
from collections import Counter
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    number_of_X_player = 0
    number_of_O_player = 0

    # First, check if the board is in terminal state. If so, return None
    if terminal(board):
        return None
    
    """
    Second, check if this is kick-off state of the game, so whether the board is in the initial state. If so, return X player.
    If not in initial state, loop over the cells of the board to sum how many cells is allocated by X and by O players.
    Since the initial board state starts with X player, at any given time, number of cells allocated by X player must be either 
    greater or equal to O player.
    """
    if board == initial_state():
        return X
    else:
        for each_row in board:
            for each_cell in each_row:
                if each_cell == X:
                    number_of_X_player += 1
                elif each_cell == O:
                    number_of_O_player += 1

    if number_of_O_player < number_of_X_player:
        return O
    else:
        return X
    
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_list = set()

    if board == terminal(board=board):
        return None
    
    for index_i, each_row in enumerate(board):
        for index_j, each_cell in enumerate(each_row):
            if board[index_i][index_j] == EMPTY:
                action_list.add((index_i, index_j))
    return action_list

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # First, check if the action is a valid action on the board
    if action not in actions(board):
        raise Exception(f"{action} is not a valid action on the board!")
    
    # Deep copy the original board as temp_board and get the current player and then insert given action into the temp_board
    current_player = player(board)    
    temp_board = copy.deepcopy(board)
    temp_board[action[0]][action[1]] = current_player

    return temp_board
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    solution_list = possible_tic_tac_toe_lines(board=board)

    # Now loop through the solution_list to take each sublist item to check if any sublist is a winner of either X or O player or tied.
    for each in solution_list:
        if Counter(each)[X] == 3:
            return X
        elif Counter(each)[O] == 3:
            return O
        
    return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if the game has a winner already, if so, return True
    if winner(board) is not None:
        return True
    
    # Check if the board is filled with X or O and no one wins, no EMPTY cell is left.
    empty_cell_number = 0
    board_size = len(board)
    for each in board:
        empty_cell_number += Counter(each)[EMPTY]

    if empty_cell_number == 0:
        return True
    
    # Otherwise return False as the game is still not over
    return False

    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board=board) == X:
        return 1
    elif winner(board=board) == O:
        return -1
    else:
        return 0
    
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # First, check if the board is in terminal board status
    if terminal(board):
        return None
    
    # Get the current player whose turn it is
    current_player = player(board=board)

    # Get the available actions from the action(board) function for the currently processing board
    available_actions = actions(board)

    # For each current player (O) action, calculate the resulting opponent (X) Player action by using utility(board) function
    action_value_map = set()
    for each in available_actions:
        temp_board = result(board, each)


        current_player = player(temp_board) # it is now the opponent player
        available_actions_for_the_current_player = actions(temp_board) # available actions for the opponent player
        action_value_map_for_X_player = set()
        
        max_value_for_X_player_move = -math.inf

        for each_X in available_actions_for_the_current_player:
            temp_board_X_player = result(temp_board, each_X)
            if utility(temp_board_X_player) > max_value_for_X_player_move:
                max_value_for_X_player_move = utility(temp_board_X_player)

        action_value_map.add((each, max_value_for_X_player_move))
    
    min = math.inf

    # test_set = {((1, 0), -3), ((1, 2), 0), ((2, 0), -2), ((0, 2), 0), ((0, 1), 0), ((2, 1), 0), ((2, 2), -1), ((1, 1), 0), ((0, 0), -4)}

    for each in action_value_map:
        if each[1] < min:
            min = each[1]
            optimal_action = each[0]

    return optimal_action
    

    # raise NotImplementedError


def possible_tic_tac_toe_lines(board):
    """
    Helper Function: Includes sublist of all possible tic tac toe combination of the board cells. Returns them as a sublists in a list container.
    1. Horizontal Rows of the board
    2. Vertical Coulumns of the board
    3. Two Diagonals of the board
    """
    solution_list = list()

    # Get the rows of the board in a sublists
    for eachrow in board:
        solution_list.append(eachrow)

    # Get the coulumns of the board in a sublists
    solution_list.extend(list(map(list, zip(*board))))

    # Get the diagonals of the board in a sublists and add them to the solution_list.
    # Calculate and add the Primary diagonal of the board
    primary_diagonal = [board[i][i] for i in range(len(board))]
    solution_list.append(primary_diagonal)

    # Calculate and add the Secondary diagonal of the board 
    secondary_diagonal = [board[i][len(board)-i-1] for i in range(len(board))]
    solution_list.append(secondary_diagonal)

    return solution_list
