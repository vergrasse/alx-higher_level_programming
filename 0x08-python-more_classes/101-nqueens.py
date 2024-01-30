import sys

def is_safe(board, row, col, N):
    # Check if it's safe to place a queen at board[row][col]
    for i in range(row):
        if board[i] == col or abs(i - row) == abs(board[i] - col):
            return False
    return True

def solve_nqueens(N, row, board, solutions):
    # Recursive function to solve N queens problem using backtracking
    if row == N:
        solutions.append(list(board))  # Found a solution, add it to the list of solutions
        return
    for col in range(N):
        if all(is_safe(board, r, col, N) for r in range(row)):
            # If it's safe to place a queen at board[row][col], place the queen and move to the next row
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)

def print_solutions(solutions):
    # Print every solution in the list of solutions
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])  # Get N from the command-line argument
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    board = [-1] * N  # Initialize the board with -1 (no queen placed)
    solutions = []  # List to store all the solutions
    solve_nqueens(N, 0, board, solutions)  # Solve the N queens problem
    print_solutions(solutions)  # Print all the solutions
