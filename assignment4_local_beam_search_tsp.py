DISTANCE = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]
CITY_COUNT = 4
BEAM_WIDTH = 3


def cost(route):
    """Add the distances between cities, including the return to city 1."""
    total = sum(DISTANCE[route[i]][route[i + 1]]
                for i in range(CITY_COUNT - 1))
    return total + DISTANCE[route[-1]][route[0]]


def generate_neighbors(route):
    """Create nearby routes by swapping two cities; keep city 1 fixed."""
    neighbors = []
    for first in range(1, CITY_COUNT):
        for second in range(first + 1, CITY_COUNT):
            next_route = route[:]
            next_route[first], next_route[second] = next_route[second], next_route[first]
            neighbors.append(next_route)
    return neighbors


def print_states(states):
    for number, route in enumerate(states, 1):
        labels = " ".join(str(city + 1) for city in route)
        print(f"State {number}: {labels} -> 1   Cost = {cost(route)}")


def main():
    states = [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3]]
    best_route = min(states, key=cost)

    print("Initial States:")
    print_states(states)

    for iteration in range(1, 6):
        all_neighbors = [
            tuple(route)
            for state in states
            for route in generate_neighbors(state)
        ]
        all_neighbors = sorted(set(all_neighbors), key=lambda route: (cost(route), route))
        states = [list(route) for route in all_neighbors[:BEAM_WIDTH]]
        if cost(states[0]) < cost(best_route):
            best_route = states[0]

        print(f"\nIteration {iteration}:")
        print_states(states)

    print("\nBest Solution:")
    route = " -> ".join(str(city + 1) for city in best_route)
    print("Route:", route, "-> 1")
    print("Best Cost:", cost(best_route))


if __name__ == "__main__":
    main()