def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
        
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens_bnb(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def print_solution(board):
        for row in board:
            print("".join(["Q" if col == 1 else "." for col in row]))
        print()

    def solve(row):
        if row == n:
            solutions.append([row[:] for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)

    return solutions

n = 8
solutions = solve_n_queens_bnb(n)

for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    for row in solution:
        print("".join(["Q" if col == 1 else "." for col in row]))
    print("-" * 40)
