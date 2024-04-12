#!/usr/bin/python3
"""
This script solves the N Queens problem, which is the challenge of placing N non-attacking queens on an N×N chessboard.

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
This script utilizes backtracking to find all possible solutions to the N Queens problem.

Usage: nqueens N
- N represents the size of the chessboard and must be an integer greater or equal to 4.

If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by
a new line, and exit with the status 1.
If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1.
If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1.
The program prints every possible solution to the problem, with one solution per line in the format:
[[row1, col1], [row2, col2], ...].

Read: Queen, Backtracking
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on the board[row][col]
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, n):
    """
    Solve the N Queens problem using backtracking
    """
    if col == n:
        # Print the solution
        print_solution(board, n)
        return

    # Place this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place the queen
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_nqueens(board, col + 1, n)

            # If the queen cannot be placed safely in any row of this column,
            # remove the queen from the current row
            board[i][col] = 0


def print_solution(board, n):
    """
    Print the board configuration
    """
    solution = []
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def main():
    """
    Entry point of the program
    """
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

    # Create an empty board
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Solve the N Queens problem
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    main()