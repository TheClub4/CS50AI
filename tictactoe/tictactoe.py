"""
Tic Tac Toe Player
"""

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
    # If the board is empty (initial state func)
    if board == initial_state():
        return X

    X_count = 0
    O_count = 0
    for row in board:
        X_count += row.count(X)
        O_count += row.count(O)

    # If the counts of X and O are the same, then it's X's turn; O's turn otherwise
    if X_count == O_count:
        return X

    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []

    # row
    for i in range(3):
        #cell
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append([i, j])
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    branches = copy.deepcopy(board)
    try:
        if branches[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            branches[action[0]][action[1]] = player(branches)
            return branches
    except IndexError:
        print("Cell occupied")



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    wins = []

    # Three in a column
    for i in range(3):
        wins.append(set([board[k][i] for k in range(3)]))
    # Three in a row
    for row in board:
        wins.append(set(row))
    # Three in a diagonal
    wins.append(set([board[i][i] for i in range(3)]))
    wins.append(set([board[i][2 -i] for i in range(3)]))

    # Check if any three are the same
    for trio in wins:
        if trio == set([X]):
            return X
        elif trio == set([O]):
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if board is still empty
    empty_count = 0
    for row in board:
        empty_count += row.count(EMPTY)
    if empty_count == 0:
        return True
    # If board is not empty but there is a winner
    elif winner(board) is not None:
        return True
    else:
        return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    # Given a board 's' (state), MAX picks action 'a' in actions(s)
    # that produces the highest value of Min_Value(results(s, a))
    if current_player == X:
        v = -math.inf
        for action in actions(board):
            k = Min_Value(result(board, action))
            if k > v:
                v = k
                best_move = action

    else:
        # Given a board 's' (state), MIN picks action 'a' in actions(s)
        # that produces the lowest value of Max_Value(results(s, a))
        v = math.inf
        for action in actions(board):
            k = Max_Value(result(board, action))
            if k < v:
                v = k
                best_move = action

    return best_move


def Max_Value(board):
    # If game is over
    if terminal(board):
        return utility(board)

    # If game is still progressing, then implement recursive reasoning
    v = -math.inf
    for action in actions(board):
        v = max(v, Min_Value(result(board, action)))
    return v


def Min_Value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, Max_Value(result(board, action)))
    return v

