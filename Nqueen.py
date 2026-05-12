# N-Queens Problem using Backtracking

# Function to print board
def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


# Check if queen can be placed
def is_safe(board, row, col, n):

    # Check left side of row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i = row
    j = col

    while i < n and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


# Backtracking function
def solve(board, col, n):

    # All queens placed
    if col == n:
        return True

    for i in range(n):

        if is_safe(board, i, col, n):

            # Place queen
            board[i][col] = 'Q'

            # Recur for next column
            if solve(board, col + 1, n):
                return True

            # Backtrack
            board[i][col] = '.'

    return False


# Main Program
n = int(input("Enter number of queens: "))

board = []

for i in range(n):
    row = ['.'] * n
    board.append(row)

if solve(board, 0, n):

    print("\nSolution Found:\n")
    print_board(board, n)

else:
    print("No Solution Exists")
