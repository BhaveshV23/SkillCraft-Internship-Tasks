from constants import GRID_SIZE, BOX_SIZE

def find_empty(board):
    """Return first empty cell position (row, col) or None."""
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if board[r][c] == 0:
                return (r, c)
    return None

def is_valid(board, number, position):
    """Check whether number placement obeys Sudoku rules."""

    row, col = position

    # Row check
    if number in board[row]:
        return False

    # Column check
    for r in range(GRID_SIZE):
        if board[r][col] == number:
            return False

    # Box check
    box_row = (row // BOX_SIZE) * BOX_SIZE
    box_col = (col // BOX_SIZE) * BOX_SIZE

    for r in range(box_row, box_row + BOX_SIZE):
        for c in range(box_col, box_col + BOX_SIZE):
            if board[r][c] == number:
                return False

    return True


def solve(board):
    """Solve Sudoku board using backtracking."""

    empty = find_empty(board)

    if empty is None:
        return True

    row, col = empty

    for number in range(1, 10):

        if is_valid(board, number, (row, col)):
            board[row][col] = number

            if solve(board):
                return True

            board[row][col] = 0

    return False