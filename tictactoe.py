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
    turn = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] != EMPTY:
                turn += 1

    return X if turn % 2 == 0 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_moves = set()
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == EMPTY:
                available_moves.add((r, c))

    return available_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    available_moves = actions(board)
    board_copy = copy.deepcopy(board)
    player_turn = player(board)

    if action not in available_moves:
        raise NameError("Invalid move.")
    else:
        board_copy[action[0]][action[1]] = player_turn

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[0][0]

        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][0]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != EMPTY:
        return board[2][0]

    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != EMPTY or len(actions(board)) == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner = winner(board)

    if winner == X:
        return 1

    if winner == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    raise NotImplementedError
