def solveNQueens(n: int):
    res = []
    board = [['.' for _ in range(n)] for _ in range(n)]

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

def printSolutions(boards):
    for board in enumerate(boards):
        print(f"Solution {board[0]+1}")
        for row in board[1]:
            for col in row:
                print(col, end=' ')
            print()
        print()

if __name__ == "__main__":
    boards = solveNQueens(4)
    printSolutions(boards)
