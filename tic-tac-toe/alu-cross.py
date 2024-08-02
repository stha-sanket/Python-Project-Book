# Lets make a board first
''''
should be like this
  |   |  
----------
  |   |  
----------
  |   |  
----------
i.e this "-" should be 10 of them to divide them and "|" should be in between rows
''''
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

''''
defining how one can win?
so it basic 3 "X" or "O" in horizontal/vertical or diagonal right, that means toomuch of matrix
lets say "X" or "O" is know as mark and our board is designed in matrix form i.e [0,1,2]
then,

possibe win chance;
- {0}{0},{1}{1},{2}{2}
- {0}{2},{1,1},{2}{0}
- {0}{colum},{0}{colum},{0}{colum},
- if row[0] == mark and row[1] == mark and row[2] == mark:
''''
def check_winner(board, mark):
    # Check rows
    for row in board:
        if row[0] == mark and row[1] == mark and row[2] == mark:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == mark and board[1][col] == mark and board[2][col] == mark:
            return True
    # Check diagonals
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def Alu_Cross():
    board = [[" " for _ in range(3)] for _ in range(3)]
    marks = ["X", "O"]
    current_mark = 0
