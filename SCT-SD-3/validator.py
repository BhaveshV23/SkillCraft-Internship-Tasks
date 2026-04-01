from solver import is_valid
from constants import GRID_SIZE


def is_board_valid(board):
    """
    Check whether the board has duplicate conflicts
    before solving begins.
    """

    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            number = board[r][c]

            if number != 0:
                board[r][c] = 0

                if not is_valid(board, number, (r, c)):
                    board[r][c] = number
                    return False

                board[r][c] = number

    return True