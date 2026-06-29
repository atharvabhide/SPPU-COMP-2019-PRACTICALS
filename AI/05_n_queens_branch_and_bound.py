import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from shared.n_queens_utils import create_board, print_solutions

def solveNQueens(n : int):
    col = set()
    posDiag = set() # determined by r+c
    negDiag = set() # determined by r-c

    res = []
    board = create_board(n)

    def backtrack(r):
        if (r == n):
            res.append([''.join(row) for row in board])
            return
        for c in range(n):
            if (c in col or r+c in posDiag or r-c in negDiag):
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = 'Q'
            backtrack(r + 1)
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = '.'
    backtrack(0)
    return res

if __name__ == "__main__":
    boards = solveNQueens(8)
    print_solutions(boards)
