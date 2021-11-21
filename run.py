# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import numpy as np


class Board:
    """
    Creates a Connect4 Board
    """
    def __init__(self):
        self.row_count = 6
        self.col_count = 7
        self.board = np.zeros((self.row_count, self.col_count))

    # Remember to flip board
    def display_board(self):
        print(self.board)

    def update_board(self, row, col, piece):
        self.board[row][col] = piece

    def valid_drop(self, col):
        global empty_row
        for row in range(self.row_count):
            if self.board[row][col] == 0:
                empty_row = row
                self.update_board(empty_row, col, 8)
                print(empty_row)
                break
            elif row == self.row_count-1:
                print("Column is full, please choose another.")
                break


gameBoard = Board()

gameBoard.update_board(0, 4, 7)
gameBoard.update_board(1, 4, 7)
gameBoard.update_board(2, 4, 7)
gameBoard.update_board(3, 4, 7)
gameBoard.update_board(4, 4, 7)

gameBoard.update_board(5, 4, 7)


user_choice = int(input("Player 1, Make your Selection(0-6):"))
gameBoard.valid_drop(user_choice)
print(gameBoard.display_board())