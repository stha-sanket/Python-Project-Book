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
