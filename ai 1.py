import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move=0, cost=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.cost = cost
        self.zero_pos = self.find_zero()

    def find_zero(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return (i, j)

    def is_goal(self):
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        return sum(self.board, []) == goal

    def __eq__(self, other):
        return self.board == other.board

    def __lt__(self, other):
        return self.cost < other.cost

    def __hash__(self):
        return hash(tuple(sum(self.board, [])))

def manhattan_distance(state):
    distance = 0
    size = len(state.board)
    goal_positions = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 0: (2, 2)}
    for i in range(size):
        for j in range(size):
            if state.board[i][j] != 0:
                goal_x, goal_y = goal_positions[state.board[i][j]]
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def a_star(start):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, (manhattan_distance(start), start))
    while open_list:
        _, current = heapq.heappop(open_list)
        if current.is_goal():
            return reconstruct_path(current)
        closed_set.add(current)
        for neighbor in get_neighbors(current):
            if neighbor not in closed_set:
                heapq.heappush(open_list, (neighbor.cost + manhattan_distance(neighbor), neighbor))
    return None

def get_neighbors(state):
    neighbors = []
    x, y = state.zero_pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(state.board) and 0 <= ny < len(state.board[0]):
            new_board = [row[:] for row in state.board]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            neighbors.append(PuzzleState(new_board, state, state.move + 1, state.move + 1))
    return neighbors

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]

def print_solution(path):
    for step in path:
        for row in step:
            print(row)
        print()

# Example usage:
start_board = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]
start_state = PuzzleState(start_board)
solution_path = a_star(start_state)

if solution_path:
    print_solution(solution_path)
else:
    print("No solution found.")
