from collections import Counter
import curses


def next_empty(sudoku):
    for row_i, row in enumerate(sudoku):
        for col_i, each in enumerate(row):
            if each == 0:
                return row_i, col_i
    return None


def is_valid(board, row, col):

    def no_row_duplicate(board, row, col):
        curr_row = board[row]
        count = Counter(curr_row)
        for nums in range(1, 10):
            if count[nums] > 1:
                return False
        return True

    def no_col_duplicate(board, row, col):
        curr_col = [i[col] for i in board]
        count = Counter(curr_col)
        for nums in range(1, 10):
            if count[nums] > 1:
                return False
        return True

    def no_box_duplicate(board, row, col):
        curr_box = []
        big_row = row // 3
        big_col = col // 3
        for r_index, rows in enumerate(board):
            for c_index, num in enumerate(rows):
                if r_index // 3 == big_row and c_index // 3 == big_col:
                    curr_box.append(num)
        count = Counter(curr_box)
        for nums in range(1, 10):
            if count[nums] > 1:
                return False
        return True

    if no_row_duplicate(board, row, col) and no_col_duplicate(board, row, col) and no_box_duplicate(board, row, col):
        return True
    return False


CELL_HEIGHT = 2
CELL_WIDTH = 4


def draw_board(win, board):
    """Draw a 9×9 grid once, then fill in all the numbers/dots."""
    win.clear()
    height = 9 * CELL_HEIGHT + 1
    width = 9 * CELL_WIDTH + 1

    # 1) Draw all the horizontal grid lines
    for i in range(10):
        y = i * CELL_HEIGHT
        for x in range(width):
            win.addch(y, x, curses.ACS_HLINE)

    # 2) Draw all the vertical grid lines
    for j in range(10):
        x = j * CELL_WIDTH
        for y in range(9 * CELL_HEIGHT + 1):
            win.addch(y, x, curses.ACS_VLINE)

    # 3) Draw the intersections
    for i in range(10):
        for j in range(10):
            y = i * CELL_HEIGHT
            x = j * CELL_WIDTH
            win.addch(y, x, curses.ACS_PLUS)

    # 4) Fill in the cells
    for r in range(9):
        for c in range(9):
            y = r * CELL_HEIGHT + 1
            x = c * CELL_WIDTH + 2
            ch = str(board[r][c]) if board[r][c] else '·'
            win.addch(y, x, ch)

    win.refresh()


def update_cell(win, r, c, val):
    """Only overwrite the one cell at (r,c)."""
    y = r * CELL_HEIGHT + 1
    x = c * CELL_WIDTH + 2
    ch = str(val) if val else '·'
    win.addch(y, x, ch)
    win.refresh()


def _solve(win, board):
    pos = next_empty(board)
    if pos is None:
        return True
    r, c = pos
    for num in range(1, 10):
        board[r][c] = num
        update_cell(win, r, c, num)
        if is_valid(board, r, c) and _solve(win, board):
            return True
    board[r][c] = 0
    update_cell(win, r, c, 0)
    return False


def solve_curses(board):
    curses.wrapper(lambda win: (draw_board(win, board), _solve(win, board)))
