def heuristic(board, goal):
    """Count numbered tiles that are not yet in their goal positions."""
    return sum(board[i] != 0 and board[i] != goal[i] for i in range(9))


def moves(board):
    """Return each board that can be reached by sliding the blank once."""
    result = []
    blank = board.index(0)
    row, col = divmod(blank, 3)
    for row_change, col_change in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + row_change, col + col_change
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            other = new_row * 3 + new_col
            next_board = board.copy()
            next_board[blank], next_board[other] = next_board[other], next_board[blank]
            result.append(next_board)
    return result


def astar(start, goal):
    """Pick the open state with the lowest f = g + h score each time."""
    open_list = [(heuristic(start, goal), 0, start, [start])]
    visited = []

    while open_list:
        open_list.sort()
        f_score, cost, board, path = open_list.pop(0)
        if board == goal:
            return path
        if board in visited:
            continue
        visited.append(board)

        for next_board in moves(board):
            if next_board not in visited:
                next_cost = cost + 1
                score = next_cost + heuristic(next_board, goal)
                open_list.append((score, next_cost, next_board, path + [next_board]))
    return None


def main():
    start = [1, 2, 3, 0,4, 6, 7, 5, 8]
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    path = astar(start, goal)

    if path:
        for board in path:
            for row in range(0, 9, 3):
                print(board[row:row + 3])
            print()
        print("Total moves:", len(path) - 1)
    else:
        print("No solution")


if __name__ == "__main__":
    main()