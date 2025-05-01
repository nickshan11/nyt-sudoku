from collections import Counter

test = [[0, 4, 0, 0, 6, 2, 8, 1, 9],
        [9, 2, 0, 0, 4, 0, 6, 0, 0],
        [0, 6, 8, 0, 7, 3, 0, 2, 0],
        [0, 0, 1, 6, 2, 0, 0, 8, 0],
        [2, 0, 6, 3, 0, 0, 1, 9, 7],
        [0, 0, 9, 7, 0, 0, 0, 0, 6],
        [8, 0, 3, 0, 0, 5, 0, 6, 0],
        [0, 0, 0, 1, 0, 0, 4, 0, 8],
        [7, 0, 0, 0, 8, 6, 0, 0, 0]]

valid_test = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


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
