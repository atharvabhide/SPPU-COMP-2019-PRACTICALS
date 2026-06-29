"""Shared utilities for N-Queens problem implementations."""


def create_board(n, empty_char='.'):
    """Create an n x n board initialized with the empty character."""
    return [[empty_char for _ in range(n)] for _ in range(n)]


def print_board(board):
    """Print a single board configuration."""
    for row in board:
        for col in row:
            print(col, end=' ')
        print()


def print_solutions(boards):
    """Print all board solutions with numbering."""
    for idx, board in enumerate(boards):
        print(f"Solution {idx + 1}")
        for row in board:
            for col in row:
                print(col, end=' ')
            print()
        print()
