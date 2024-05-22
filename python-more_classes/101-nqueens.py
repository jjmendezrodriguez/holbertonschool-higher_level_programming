import sys


def print_board(board):
    """Prints the current board configuration as a list of positions."""
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i] == j:
                solution.append([i, j])
    print(solution)


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row):
    """Use backtracking to solve the N queens problem."""
    if row == len(board):
        print_board(board)
        return
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)
            board[row] = -1


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [-1] * N
    solve_nqueens(board, 0)


if __name__ == "__main__":
    main()
