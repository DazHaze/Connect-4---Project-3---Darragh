# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import numpy as np
import random as rn
from time import sleep
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

    def valid_drop(self, piece):
        global empty_row
        if piece == 1:
            choice = int(input("Please choose a column (0-6): \n"))
            for row in range(self.row_count):
                if self.board[row][choice] == 0:
                    empty_row = row
                    self.dropping_piece(empty_row, choice, 1)
                    # self.update_board(empty_row, choice, 1)
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
                # print(int_rows - x)
                self.update_board(int_rows-x, col, piece)
                self.display_upsidedown_board()
                self.update_board(int_rows-x, col, 0)
                x += 1
                sleep(0.4)
            else:
                # print(row, row + 1)
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
                    if row + 3 < 6:
                        # Check if there is 4 in a row.
                        if self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col]:
                            return True
                        # Check if there is 4 in a column.
                        elif self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3]:
                            return True
                        # Check if there is 4 in a upward right diagonal.
                        elif self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3]:
                            return True
                        # Check if there is 4 in a upwarward left diagonal.
                        elif self.board[row][col] == self.board[row+1][col-1] == self.board[row+2][col-2] == self.board[row+3][col-3]:
                            return True

    def computer_choice(self):
        print("Computer now thinking...")
        sleep(1.2)
        global empty_row
        global choice
        choice = randrange(self.col_count)
        for row in range(self.row_count):
            if self.board[row][choice] == 0:
                empty_row = row
                self.dropping_piece(empty_row, choice, 2)
                break
            elif row == self.row_count-1:
                self.computer_choice()
                break

    # for each point that is 2 (computer symbol)
        # check if there is another 2 in diag
            # if not try to place piece in diag
             # if space is not free loop through with random int to place piece in free row


gameBoard = Board()
playing = True
initial_message = "***   Welcome to Connect4 written in python!   ***\n***   Try your best to beat the computer!      ***\n***   		Goodluck! :)                   ***\n"

playing = True
player = 1
print(initial_message)
while playing:
    gameBoard.display_upsidedown_board()
    if player == 2:
        gameBoard.computer_choice()
        player = 1
    else:
        gameBoard.valid_drop(1)
        player = 2

    if gameBoard.check_win():
        print("You win!")
        playing = False



