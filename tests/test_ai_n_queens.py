import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'AI'))

from importlib.machinery import SourceFileLoader

mod_backtracking = SourceFileLoader(
    "n_queens_backtracking",
    os.path.join(os.path.dirname(__file__), '..', 'AI', '04_n_queens_backtracking.py'),
).load_module()

mod_branch_bound = SourceFileLoader(
    "n_queens_branch_bound",
    os.path.join(os.path.dirname(__file__), '..', 'AI', '05_n_queens_branch_and_bound.py'),
).load_module()

solveNQueens_bt = mod_backtracking.solveNQueens
solveNQueens_bb = mod_branch_bound.solveNQueens


def _is_valid_board(board):
    """Verify no two queens attack each other."""
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
    def test_4_queens_has_solutions(self):
        solutions = solveNQueens_bt(4)
        assert len(solutions) >= 1

    def test_4_queens_valid(self):
        for board in solveNQueens_bt(4):
            assert _is_valid_board(board)

    def test_1_queen(self):
        solutions = solveNQueens_bt(1)
        assert len(solutions) == 1
        assert solutions[0] == ['Q']

    def test_each_row_one_queen(self):
        for board in solveNQueens_bt(6):
            for row in board:
                assert row.count('Q') == 1


class TestNQueensBranchAndBound:
    def test_4_queens_count(self):
        solutions = solveNQueens_bb(4)
        assert len(solutions) == 2

    def test_8_queens_count(self):
        solutions = solveNQueens_bb(8)
        assert len(solutions) == 92

    def test_all_valid(self):
        for board in solveNQueens_bb(5):
            assert _is_valid_board(board)

    def test_1_queen(self):
        solutions = solveNQueens_bb(1)
        assert len(solutions) == 1
        assert solutions[0] == ['Q']

    def test_board_size_matches_n(self):
        n = 6
        for board in solveNQueens_bb(n):
            assert len(board) == n
            for row in board:
                assert len(row) == n


class TestConsistency:
    def test_same_solution_count_for_small_n(self):
        """Both approaches should find the same number of solutions for n=5."""
        bt_count = len(solveNQueens_bt(5))
        bb_count = len(solveNQueens_bb(5))
        assert bt_count == bb_count
