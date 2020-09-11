from typing import List


def hourglass(board: List[List[int]]) -> int:
    """
    There are 16 hourglasses in board. An hourglass sum is the sum
    of an hourglass' values. Calculate the hourglass sum for every
    hourglass in board, then print the maximum hourglass sum. The
    array will always be 6x6.
    """
    max_column = 4
    max_row = 4
    hourglass_sums = list()

    for n_row, row in enumerate(board):
        if n_row == max_row:
            break

        for n_column, value in enumerate(row):
            if n_column == max_column:
                break

            top = sum(row[n_column:n_column + 3])
            mid = board[n_row + 1][n_column + 1]
            bottom = sum(board[n_row + 2][n_column:n_column + 3])

            hourglass_sums.append(top + mid + bottom)

    return max(hourglass_sums)


sample_board_1 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]
assert hourglass(sample_board_1) == 19
sample_board_2 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 9, 2, -4, -4, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, -1, -2, -4, 0]
]
assert hourglass(sample_board_2) == 13
