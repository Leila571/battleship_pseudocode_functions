"""
10/22/2020
Leila Lopez Marks
Battleship Functions Intro
"""

def intro():
    print("Welcome to Battleship!")

intro()

board = [
    [" ", "", " "," "," "," ", " ", " "],
    [" ", "", " "," "," "," ", " ", " "],
    [" ", "", " "," "," "," ", " ", " "],
    [" ", "", " "," "," "," ", " ", " "],
    [" ", "", " "," "," "," ", " ", " "],
    [" ", "", " "," "," "," ", " ", " "],
    [" ", "", " "," "," "," ", " ", " "],
    [" ", "", " "," "," "," ", " ", " "],
]

def DrawBoard():
    for i in range (8):
        for j in range (8):
            board[i][j] = "~"
    for i in range (8):
        print(board[i])

DrawBoard()

#This is the check for win condition
win_condition = who won
if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
    print(board[0][0], "is the winner player1")

elif board[0][0] == [1][0] and board[0][0] == board[2][0]:
    print(board[0][0], "is the winner player2")
else:
    print("keep playing")

#This is the win message
#Player1 wins
print("Player1 has won!")
#Player2 wins
print("Player2 has won!")

        0000000000
      00000000000000
    00000000000000000
   0000000000000000000
  000000    000    000000
  00000     000     00000
  00000     000     00000
  00000     000     00000
  000000    000    000000
  00000000000000000000000
  00000000000000000000000
  00000            000000
   00000          000000
    00000        000000
     00000000000000000
      000000000000000
       0000000000000

#Ask to play again
print("Do you want to play again?")
