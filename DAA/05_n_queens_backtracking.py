def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_with_known_first_queen(n, first_queen_row, first_queen_col):
    board = [[0 for _ in range(n)] for _ in range(n)]

    board[first_queen_row][first_queen_col] = 1

    def solve_n_queens_util(row):
        if row == n:
            return True

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                if solve_n_queens_util(row + 1):
                    return True
                board[row][col] = 0

        return False

    if not solve_n_queens_util(first_queen_row + 1):
        print("No solution exists.")
    else:
        for row in board:
            for col in row:
                if col == 1:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()

n = 8
first_queen_row = 0  
first_queen_col = 1 
solve_n_queens_with_known_first_queen(n, first_queen_row, first_queen_col)
