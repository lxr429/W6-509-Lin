# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    for n in range(3):
        if board[n][0] == board[n][1] == board[n][2] and board[n][0] is not None:
            return board[n][0]
        if board[0][n] == board[1][n] == board[2][n] and board[0][n] is not None:
            return board[0][n]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    if all(board[i][j] is not None for i in range(3) for j in range(3)):
        return 'Draw'


def other_player(player):
    """Given the character for a player, returns the other player."""
    return 'O' if player == 'X' else 'X'
