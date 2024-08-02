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
- {0}{0},{1}{1},{2}{2},
''''
