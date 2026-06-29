import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from shared.n_queens_utils import create_board, print_solutions

def solveNQueens(n: int):
    res = []
    board = create_board(n)

    def isSafe(row, col):
        # check in column
        for i in range(row):    
            if (board[i][col] == 'Q'):
                return False
            
        # check in positive diagonal
        i = row
        j = col
        while (i >= 0 and j < n):
            if (board[i][j] == 'Q'):
                return False
            i -= 1
            j += 1

        # check in negative diagonal
        i = row
        j = col
        while (i >= 0 and j >= 0):
            if (board[i][j] == 'Q'):
                return False
            i -= 1
            j -= 1

        return True

    def backtrack(row):
        if (row == n):
            res.append([''.join(row) for row in board])
            return False
        for col in range(n):
            if (isSafe(row, col)):
                board[row][col] = 'Q'
                possible = backtrack(row+1)
                if (possible):
                    return True
                board[row][col] = '.'
        return False
    
    backtrack(0)
    return res

if __name__ == "__main__":
    boards = solveNQueens(4)
    print_solutions(boards)
