def dfs(capacity1, capacity2, goal):
    start = (0, 0)
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()
        jug1, jug2 = current
        if current in visited:
            continue
        visited.add(current)

        print("\nCurrent Percept:")
        print("Jug 1:", jug1, "litres")
        print("Jug 2:", jug2, "litres")
        print("Current State:", current)

        if jug1 == goal or jug2 == goal:
            print("\nGoal Reached!")
            return path, visited

        states = [
            (capacity1, jug2),
            (jug1, capacity2),
            (0, jug2),
            (jug1, 0),
            (jug1 - min(jug1, capacity2 - jug2),
             jug2 + min(jug1, capacity2 - jug2)),
            (jug1 + min(jug2, capacity1 - jug1),
             jug2 - min(jug2, capacity1 - jug1)),
        ]

        for next_state in states:
            if next_state not in visited and next_state != current:
                stack.append((next_state, path + [next_state]))

    return None, visited


def main():
    capacity1, capacity2, goal = 4, 3, 2
    path, visited = dfs(capacity1, capacity2, goal)

    print("\n========== ALL VISITED STATES ==========")
    for state in visited:
        print("Jug 1:", state[0], "litres | Jug 2:", state[1], "litres")

    print("\n========== FINAL SOLUTION PATH ==========")
    if path:
        for step, state in enumerate(path, 1):
            print(f"Step {step} | Jug 1: {state[0]} litres | Jug 2: {state[1]} litres")
    else:
        print("No solution found")


if __name__ == "__main__":
    main()