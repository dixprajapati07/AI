from collections import deque


def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {tuple(start)}

    while queue:
        board, path = queue.popleft()
        if board == goal:
            return path

        blank = board.index(0)
        row, col = divmod(blank, 3)
        for row_change, col_change in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + row_change, col + col_change
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_position = new_row * 3 + new_col
                next_board = board.copy()
                next_board[blank], next_board[new_position] = (
                    next_board[new_position], next_board[blank]
                )

                if tuple(next_board) not in visited:
                    visited.add(tuple(next_board))
                    queue.append((next_board, path + [next_board]))
    return None


def main():
    start = [1, 2, 3, 4, 0, 6, 7, 5, 8]
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    path = bfs(start, goal)

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