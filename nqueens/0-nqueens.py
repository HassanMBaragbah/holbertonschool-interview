#!/usr/bin/python3
"""
N Queens problem solver using backtracking.
"""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed safely at board[row][col]."""
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(row, n, board):
    """Recursively find and print all solutions using backtracking."""
    if row == n:
        solution = [[i, board[i]] for i in range(n)]
        print(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(row + 1, n, board)
            board[row] = -1


def main():
    """Main entry point for argument validation and execution."""
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

    board = [-1] * n
    solve_nqueens(0, n, board)


if __name__ == "__main__":
    main()
