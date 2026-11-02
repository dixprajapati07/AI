def vacuum_agent(location, status):
    """Choose one action from the room and its current cleanliness."""
    if status == "Dirty":
        return "Suck"
    if location == "A":
        return "Right"
    return "Left"


def main():
    environment = {"A": "Dirty", "B": "Dirty"}
    location = "A"
    performance = 0

    while "Dirty" in environment.values():
        status = environment[location]
        action = vacuum_agent(location, status)
        print(f"Location: {location} | Status: {status} | Action: {action}")

        if action == "Suck":
            environment[location] = "Clean"
            performance += 1
        elif action == "Right":
            location = "B"
        else:
            location = "A"

    print("Final Environment:", environment)
    print("Performance Score (suck):", performance)


if __name__ == "__main__":
    main()