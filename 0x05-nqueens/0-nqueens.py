#!/usr/bin/python3
"""
This script solves the N Queens problem, which is the challenge of placing
N non-attacking queens on an N×N chessboard.
"""
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at position (row, col) on the board.

    Args:
        board (list): Current state of the board, where board[i] represents the row of the queen in column i.
        row (int): Row index to check for safety.
        col (int): Column index to check for safety.

    Returns:
        bool: True if it's safe to place a queen at position (row, col), False otherwise.
    """
    for i in range(col):
        # Check if there is a queen in the same row or if it attacks diagonally
        if board[i] == row or \
                board[i] - i == row - col or \
                board[i] + i == row + col:
            return False
    return True


def solve_nqueens(n, board, col, solutions):
    """
    Solve the N Queens problem recursively using backtracking.

    Args:
        n (int): Size of the chessboard (N x N).
        board (list): Current state of the board, where board[i] represents the row of the queen in column i.
        col (int): Current column being processed.
        solutions (list): List to store the found solutions.
    """
    if col == n:
        # If all columns are processed, add the current board configuration to solutions
        solutions.append(list(enumerate(board)))
        return

    for i in range(n):
        if is_safe(board, i, col):
            # If it's safe to place a queen at position (i, col), place it and move to the next column
            board[col] = i
            solve_nqueens(n, board, col + 1, solutions)


def print_solutions(solutions):
    """
    Print the found solutions.

    Args:
        solutions (list): List of solutions, where each solution is a list of (row, column) positions of queens.
    """
    for solution in solutions:
        print(solution)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with all queens in the same row (-1 indicates no queen)
    board = [-1] * n
    solutions = []
    solve_nqueens(n, board, 0, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()