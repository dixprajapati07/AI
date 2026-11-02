from collections import deque
from itertools import product


def create_state(positions):
    pegs = [[], [], []]
    for disk in range(3, 0, -1):
        pegs[positions[disk - 1]].append(disk)
    return pegs


def successors(state):
    for source in range(3):
        source_disks = [d for d in range(1, 4) if state[d - 1] == source]
        if not source_disks:
            continue
        disk = min(source_disks)
        for destination in range(3):
            target_disks = [d for d in range(1, 4) if state[d - 1] == destination]
            if source != destination and (not target_disks or disk < min(target_disks)):
                next_state = list(state)
                next_state[disk - 1] = destination
                yield tuple(next_state), (disk, source, destination)


def solve(start, goal):
    queue = deque([start])
    parent = {start: None}
    move_used = {}
    while queue:
        state = queue.popleft()
        if state == goal:
            break
        for next_state, move in successors(state):
            if next_state not in parent:
                parent[next_state] = state
                move_used[next_state] = move
                queue.append(next_state)
    path, state = [], goal
    while state != start:
        path.append((state, move_used[state]))
        state = parent[state]
    return list(reversed(path))


def main():
    all_states = list(product(range(3), repeat=3))
    start, goal = (0, 0, 0), (2, 2, 2)
    print("TOTAL STATES =", len(all_states))
    print("Initial State:", create_state(start))
    print("Goal State:", create_state(goal))
    for step, (state, (disk, source, target)) in enumerate(solve(start, goal), 1):
        print(f"Move {step}: disk {disk} from {chr(65 + source)} to {chr(65 + target)}")
        print("State:", create_state(state))


if __name__ == "__main__":
    main()