def is_safe(board, row, col):
    """Check earlier rows for a queen in the same column or diagonal."""
    for previous_row in range(row):
        same_column = board[previous_row] == col
        same_diagonal = abs(board[previous_row] - col) == abs(previous_row - row)
        if same_column or same_diagonal:
            return False
    return True


def print_board(board, message):
    print("\n" + message)
    for row in range(8):
        print(" ".join("Q" if board[row] == col else "." for col in range(8)))


def solve(board, row):
    if row == 8:
        print_board(board, "GOAL STATE")
        return True

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            print_board(board, f"Queen placed at Row {row + 1}, Column {col + 1}")
            if solve(board, row + 1):
                return True
            board[row] = -1
            print(f"Backtracking: removed queen from row {row + 1}")
    return False


def main():
    board = [-1] * 8
    print_board(board, "INITIAL STATE")
    solve(board, 0)


if __name__ == "__main__":
    main()