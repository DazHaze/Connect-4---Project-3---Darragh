# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import numpy as np
import random as rn
from random import randrange


class Board:
    """
    Creates a Connect4 Board
    """

    def __init__(self):
        self.row_count = 6
        self.col_count = 7
        self.board = np.zeros((self.row_count, self.col_count))
        self.user_row = []
        self.user_column = []

    # Remember to flip board

    def display_upsidedown_board(self):
        print(f'\n{np.flip(self.board, 0)}\n')

    def display_board(self):
        print(self.board)

    def update_board(self, row, col, piece):
        self.board[row][col] = piece

    def valid_drop(self):
        global empty_row
        global choice
        choice = int(input("Please choose a column (0-6): \n"))
        for row in range(self.row_count):
            if self.board[row][choice] == 0:
                empty_row = row
                self.update_board(empty_row, choice, 1)
                break
            elif row == self.row_count-1:
                print("Column is full, please choose another.\n")
                choice = int(input("Please choose a column (0-6): \n"))
                break

    def check_win(self):
        # Check win in columns
        for row in range(self.row_count):
            for col in range(self.col_count):
                if self.board[row][col] == 1:
                    if row + 3 < 6:
                        if self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col]:
                            return True
        # Check win in rows
        for col in range(self.col_count):
            for row in range(self.row_count):
                if self.board[row][col] == 1:
                    if col + 3 < 7:
                        if self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3]:
                            return True

    def check_win_rows(self):
        for col in range(self.col_count):
            for row in range(self.row_count):
                if self.board[row][col] == 1:
                    if col + 3 < 7:
                        if self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3]:
                            return True

    def computer_choice(self):
        global empty_row
        global choice
        choice = randrange(self.col_count)
        for row in range(self.row_count):
            if self.board[row][choice] == 0:
                empty_row = row
                self.update_board(empty_row, choice, 2)
                break
            elif row == self.row_count-1:
                choice = randrange(self.col_count)
                break



gameBoard = Board()

playing = True
initial_message = "***   Welcome to Connect4 written in python!   ***\n***   Try your best to beat the computer!      ***\n***   		Goodluck! :)                   ***\n"

while playing:
    print(initial_message)
    win = False
    while not win:
        gameBoard.display_upsidedown_board()
        gameBoard.valid_drop()
        gameBoard.computer_choice()
        if gameBoard.check_win():
            gameBoard.display_upsidedown_board()
            win = True
            print("You won!")
        else:
            win = False
    else:
        playing = False
