def is_safe(board, row, col, n):
    # Check this column on the left side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, n):
    if row >= n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, n):
                return True
            board[row][col] = 0  # Backtrack

    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solve_n_queens_util(board, 0, n):
        return board
    else:
        return None

def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))

# Example usage:
try:
    n = int(input("Enter the size of the board (e.g., 8 for 8x8 board): "))
    if n < 1:
        print("Please enter a positive integer.")
    else:
        solution = solve_n_queens(n)
        if solution:
            print_board(solution)
        else:
            print("No solution found.")
except ValueError:
    print("Please enter a valid integer.")
