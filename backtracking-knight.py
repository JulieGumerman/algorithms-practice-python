#chessboard size

n = 8

def isSafe(x, y, board):
    #checks if i and j are places on the board
    if (x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False

def printSolution(board):
    #prints chessboard
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = " ")
        print()

def solveBK():
    board = [[-1 for i in range(n)] for i in range(n)]