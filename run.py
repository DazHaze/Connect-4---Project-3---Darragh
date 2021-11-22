"""
Your code goes here.
You can delete these comments, but do not change the name of this file
Write your code to expect a terminal of 80 characters wide and 24 rows high
"""
from time import sleep
from random import randrange
import numpy as np


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

    def display_upsidedown_board(self):
        print(f'\n{np.flip(self.board, 0)}\n')

    def display_board(self):
        print(self.board)

    def update_board(self, row, col, piece):
        self.board[row][col] = piece

    def valid_drop(self, piece):
        # global empty_row
        if piece == 1:
            user_choice = int(input("Please choose a column (0-6): \n"))
            for row in range(self.row_count):
                if self.board[row][user_choice] == 0:
                    empty_row = row
                    self.dropping_piece(empty_row, user_choice, 1)
                    break

                elif row == self.row_count-1:
                    print("Column is full, please choose another.\n")
                    self.valid_drop(1)
                    break

    def dropping_piece(self, row, col, piece):
        int_rows = self.row_count-1
        if row != int_rows:
            amount = int_rows - row
            for x in range(amount):
                self.update_board(int_rows-x, col, piece)
                self.display_upsidedown_board()
                self.update_board(int_rows-x, col, 0)
                x += 1
                sleep(0.4)
                if x == amount:
                    break
            else:
                self.update_board(row + 1, col, 0)
                self.update_board(row, col, piece)
                self.display_upsidedown_board()

    def check_win(self):
        """
        Check if there is a win in columns, rows or diagonals.
        """
        for row in range(self.row_count):
            for col in range(self.col_count):
                if self.board[row][col] == 1:
                    b = self.board
                    r = row
                    c = col
                    # Check if there is 4 in a row.
                    if b[r][c] == b[r+1][c] == b[r+2][c] == b[r+3][c]:
                        return True
                    # Check if there is 4 in a column.
                    elif b[r][c] == b[r][c+1] == b[r][c+2] == b[r][c+3]:
                        return True
                    # Check if there is 4 in a upward right diagonal.
                    elif b[r][c] == b[r+1][c+1] == b[r+2][c+2] == b[r+3][c+3]:
                        return True
                    # Check if there is 4 in a upwarward left diagonal.
                    elif b[r][c] == b[r+1][c-1] == b[r+2][c-2] == b[r+3][c-3]:
                        return True

    def computer_choice(self):
        """
        Chooses a random column
        Checks if that column has a free row
        Calls dropping_piece to then place the computers choice
        """
        print("Computer now thinking...")
        sleep(1.2)
        comp_choice = randrange(self.col_count)
        for row in range(self.row_count):
            if self.board[row][comp_choice] == 0:
                empty_row = row
                self.dropping_piece(empty_row, comp_choice, 2)
                break
            elif row == self.row_count-1:
                self.computer_choice()
                break


gb = Board()
PLAYING = True
INITIAL_MESSAGE = "***   Welcome to Connect4 written in python!   ***\n***  \
                     Try your best to beat the computer!    \
                      ***\n***   		Goodluck! :)                   ***\n"
PLAYING = True
PLAYER = 1
print(INITIAL_MESSAGE)
while PLAYING:
    gb.display_upsidedown_board()
    if PLAYER == 2:
        gb.computer_choice()
        PLAYER = 1
    else:
        gb.valid_drop(1)
        PLAYER = 2

    if gb.check_win():
        WIN_MESSAGE = "*** 		  You win!!!		       ***\n***     \
                        Would you like to play again? y/n      ***\n"
        user_input = input(WIN_MESSAGE)
        if user_input == "y":
            gb.board = np.zeros((gb.row_count, gb.col_count))
        else:
            PLAYING = False
