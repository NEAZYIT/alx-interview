#!/usr/bin/python3

"""
N Queens Solver

This script solves the N Queens problem, which is the challenge of placing N non-attacking queens on an N×N chessboard.
"""

import sys


class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def solve(self):
        """Solve the N Queens problem"""
        self._solve_util(0, [], [], [])

    def _solve_util(self, row, cols, diags1, diags2):
        """Recursive utility function to solve the N Queens problem"""
        if row == self.n:
            self.solutions.append(cols[:])
            return

        for col in range(self.n):
            if col not in cols and row + col not in diags1 and row - col not in diags2:
                cols.append(col)
                diags1.append(row + col)
                diags2.append(row - col)

                self._solve_util(row + 1, cols, diags1, diags2)

                cols.pop()
                diags1.pop()
                diags2.pop()

    def print_solutions(self):
        """Print all solutions"""
        for solution in self.solutions:
            print([[row, col] for row, col in enumerate(solution)])


def main():
    """Main function"""
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

    solver = NQueensSolver(n)
    solver.solve()
    solver.print_solutions()


if __name__ == "__main__":
    main()