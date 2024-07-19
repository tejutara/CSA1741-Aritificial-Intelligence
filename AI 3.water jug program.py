from collections import deque

def is_valid_state(state, capacities):
    return 0 <= state[0] <= capacities[0] and 0 <= state[1] <= capacities[1]

def get_next_states(state, capacities):
    next_states = []
    jug1, jug2 = state
    cap1, cap2 = capacities

    # Fill Jug1
    next_states.append((cap1, jug2))

    # Fill Jug2
    next_states.append((jug1, cap2))

    # Empty Jug1
    next_states.append((0, jug2))

    # Empty Jug2
    next_states.append((jug1, 0))

    # Pour Jug1 into Jug2
    pour = min(jug1, cap2 - jug2)
    next_states.append((jug1 - pour, jug2 + pour))

    # Pour Jug2 into Jug1
    pour = min(jug2, cap1 - jug1)
    next_states.append((jug1 + pour, jug2 - pour))

    return [state for state in next_states if is_valid_state(state, capacities)]

def bfs(capacities, target):
    start_state = (0, 0)
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        (current_state, path) = queue.popleft()
        if current_state in visited:
            continue

        visited.add(current_state)
        path = path + [current_state]

        jug1, jug2 = current_state
        if jug1 == target or jug2 == target:
            return path

        for next_state in get_next_states(current_state, capacities):
            if next_state not in visited:
                queue.append((next_state, path))

    return None

def print_solution(solution):
    if solution:
        for step in solution:
            print(f"Jug1: {step[0]} liters, Jug2: {step[1]} liters")
    else:
        print("No solution found.")

# Example usage:
try:
    capacity1 = int(input("Enter the capacity of Jug1: "))
    capacity2 = int(input("Enter the capacity of Jug2: "))
    target = int(input("Enter the target amount of water: "))

    if target > max(capacity1, capacity2):
        print("Target amount is greater than the capacity of both jugs.")
    else:
        solution = bfs((capacity1, capacity2), target)
        print_solution(solution)
except ValueError:
    print("Please enter valid integers.")
