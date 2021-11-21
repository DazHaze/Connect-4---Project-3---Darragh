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
                self.update_board(empty_row, col, 7)
                print(empty_row)
                break
            elif row == self.row_count-1:
                print("Column is full, please choose another.")
                break

    def check_win_columns(self):
        for row in range(self.row_count):
            for col in range(self.col_count):
                if self.board[row][col] == 7:
                    if row + 3 < 6:
                        if self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col]:
                            print("Win columns")
    
    def check_win_rows(self):
        for col in range(self.col_count):
            for row in range(self.row_count):
                if self.board[row][col] == 7:
                    if col + 3 < 7:
                        if self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3]:
                            print("Win rows")




gameBoard = Board()

gameBoard.update_board(2, 0, 7)
gameBoard.update_board(2, 1, 7)
gameBoard.update_board(2, 2, 7)
gameBoard.update_board(2, 3, 7)



user_choice = int(input("Player 1, Make your Selection(0-6):"))
gameBoard.valid_drop(user_choice)
print(gameBoard.display_board())
gameBoard.check_win_rows()