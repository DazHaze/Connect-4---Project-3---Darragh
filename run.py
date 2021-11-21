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

    def display_upsidedown_board(self):
        print(np.flip(self.board, 0))

    def display_board(self):
        print(self.board)

    def update_board(self, row, col, piece):
        self.board[row][col] = piece

    def valid_drop(self):
        global empty_row
        global choice
        choice = int(input("Please choose a column: \n"))
        for row in range(self.row_count):
            if self.board[row][choice] == 0:
                empty_row = row
                self.update_board(empty_row, choice, 7)
                break
            elif row == self.row_count-1:
                print("Column is full, please choose another.\n")
                choice = int(input("Please choose a column: \n"))
                break

    def check_win(self):
        # Check win in columns
        for row in range(self.row_count):
            for col in range(self.col_count):
                if self.board[row][col] == 7:
                    if row + 3 < 6:
                        if self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col]:
                            return True
        # Check win in rows
        for col in range(self.col_count):
            for row in range(self.row_count):
                if self.board[row][col] == 7:
                    if col + 3 < 7:
                        if self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3]:
                            return True

    def check_win_rows(self):
        for col in range(self.col_count):
            for row in range(self.row_count):
                if self.board[row][col] == 7:
                    if col + 3 < 7:
                        if self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3]:
                            return True


gameBoard = Board()

playing = True
while playing:
    win = False
    while not win:
        gameBoard.display_upsidedown_board()
        gameBoard.valid_drop()
        if gameBoard.check_win():
            win = True
            print("You won!")
        else:
            win = False
    else:
        playing = False
