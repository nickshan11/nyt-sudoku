from collections import Counter


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


def solve(board):
    pos = next_empty(board)
    if pos is None:
        return True
    row, col = pos
    for num in range(1, 10):
        board[row][col] = num
        print(board)
        if is_valid(board, row, col):
            board[row][col] = num
            if solve(board):
                return True
        board[row][col] = 0
    return False
