import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'DAA'))

from importlib.machinery import SourceFileLoader

mod = SourceFileLoader(
    "n_queens_backtracking",
    os.path.join(os.path.dirname(__file__), '..', 'DAA', '05_n_queens_backtracking.py'),
).load_module()

solveNQueens = mod.solveNQueens


def _is_valid_board(board):
    """Check that no two queens threaten each other."""
    n = len(board)
    queens = []
    for r, row in enumerate(board):
        for c, ch in enumerate(row):
            if ch == 'Q':
                queens.append((r, c))
    for i, (r1, c1) in enumerate(queens):
        for r2, c2 in queens[i + 1:]:
            if r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                return False
    return True


class TestNQueensBacktracking:
    def test_4_queens_first_col_0_no_solution(self):
        solutions = solveNQueens(4, 0)
        assert len(solutions) == 0

    def test_4_queens_first_col_1(self):
        solutions = solveNQueens(4, 1)
        assert len(solutions) >= 1
        for board in solutions:
            assert board[0][1] == 'Q'
            assert _is_valid_board(board)

    def test_8_queens(self):
        solutions = solveNQueens(8, 0)
        assert len(solutions) >= 1
        for board in solutions:
            assert _is_valid_board(board)

    def test_each_row_has_exactly_one_queen(self):
        solutions = solveNQueens(8, 1)
        for board in solutions:
            for row in board:
                assert row.count('Q') == 1

    def test_1_queen(self):
        solutions = solveNQueens(1, 0)
        assert len(solutions) == 1
        assert solutions[0] == ['Q']
