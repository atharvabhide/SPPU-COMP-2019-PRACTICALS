def solveNQueens(n : int):
    col = set()
    posDiag = set() # determined by r+c
    negDiag = set() # determined by r-c

    res = []
    board = [['.' for _ in range(n)] for _ in range(n)]

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

def printSolutions(boards):
    for board in enumerate(boards):
        print(f"Solution: {board[0]+1}")
        for row in board[1]:
            for col in row:
                print(col, end=' ')
            print()
        print()

if __name__ == "__main__":
    boards = solveNQueens(8)
    printSolutions(boards)
