"""
This app creates a connect four game that runs in the terminal.
choose a number from 0 to 6 and click enter to play.
Enjoy!
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
        """
        Prints the upside down and flipped board array so pieces at 0,0
        are at the bottom.
        """
        print(f'\n{np.flip(self.board, 0)}\n')

    def display_board(self):
        """
        Prints the board array.
        """
        print(self.board)

    def update_board(self, row, col, piece):
        """
        Updates the board array with new value.
        """
        self.board[row][col] = piece

    def valid_drop(self, piece):
        """
        Checks which row is free in column.
        Asks for another column if not free.
        """
        if piece == 1:
            user_choice = str(input("Please choose a column (0-6): \n"))
            if (user_choice.isnumeric() and
                int(user_choice) < 7 and
                    int(user_choice) >= 0):
                user_choice = int(user_choice)
                for row in range(self.row_count):
                    if self.board[row][user_choice] == 0:
                        empty_row = row
                        self.dropping_piece(empty_row, user_choice, 1)
                        break

                    elif row == self.row_count-1:
                        print("Column is full, please choose another.\n")
                        self.valid_drop(1)
                        break
            else:
                self.valid_drop(1)

    def dropping_piece(self, row, col, piece):
        """
        Prints dropping piece animation on game board.
        """
        int_rows = self.row_count-1
        if row != int_rows:
            amount = int_rows - row
            for x in range(amount):
                self.update_board(int_rows-x, col, piece)
                self.display_upsidedown_board()
                self.update_board(int_rows-x, col, 0)
                x += 1
                sleep(0.1)
            else:
                self.update_board(row + 1, col, 0)
                self.update_board(row, col, piece)
                self.display_upsidedown_board()
        else:
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
                    if r+3 <= 6:
                        # Check if there is 4 in a row.
                        if b[r][c] == b[r+1][c] == b[r+2][c] == b[r+3][c]:
                            return "user"
                    elif c+3 <= 7:
                        # Check if there is 4 in a column.
                        if b[r][c] == b[r][c+1] == b[r][c+2] == b[r][c+3]:
                            return "user"
                    # Check if there is 4 in a upward right diagonal.
                    elif b[r][c] == b[r+1][c+1] == b[r+2][c+2] == b[r+3][c+3]:
                        return "user"
                    # Check if there is 4 in a upwarward left diagonal.
                    elif b[r][c] == b[r+1][c-1] == b[r+2][c-2] == b[r+3][c-3]:
                        return "user"
                elif self.board[row][col] == 2:
                    b = self.board
                    r = row
                    c = col
                    if r+3 <= 6:
                        # Check if there is 4 in a row.
                        if b[r][c] == b[r+1][c] == b[r+2][c] == b[r+3][c]:
                            return "computer"
                    elif c+3 <= 7:
                        # Check if there is 4 in a column.
                        if b[r][c] == b[r][c+1] == b[r][c+2] == b[r][c+3]:
                            return "computer"
                    # Check if there is 4 in a upward right diagonal.
                    elif b[r][c] == b[r+1][c+1] == b[r+2][c+2] == b[r+3][c+3]:
                        return "computer"
                    # Check if there is 4 in a upwarward left diagonal.
                    elif b[r][c] == b[r+1][c-1] == b[r+2][c-2] == b[r+3][c-3]:
                        return "computer"

    def computer_choice(self):
        """
        Chooses a random column
        Checks if that column has a free row
        Calls dropping_piece to then place the computers choice
        """
        print("Computer now thinking...")
        sleep(0.3)
        print(".")
        sleep(0.3)
        print("...")
        sleep(0.3)
        print(".....")
        sleep(0.3)
        print("......")
        sleep(0.3)
        print("........")
        sleep(0.3)
        comp_choice = randrange(self.col_count)
        for row in range(self.row_count):
            if self.board[row][comp_choice] == 0:
                empty_row = row
                self.dropping_piece(empty_row, comp_choice, 2)
                break
            elif row == self.row_count-1:
                self.computer_choice()
                break


class Player:
    """
    Player class used to choose the player type.
    """
    def __init__(self, player_type):
        self.player_type = player_type
        self.score = 0

    def return_player_type(self):
        if self.player_type == "user":
            return 1
        elif self.player_type == "computer":
            return 2
        else:
            return "f'{self.player_type} is not a recognised player type."


def play_game():
    """
    Creates the computer and user player.
    Creates the game board.
    Starts while loop with value PLAYING.
    """
    computer_player = Player("computer")
    user_player = Player("user")
    u_p = computer_player.return_player_type()
    c_p = user_player.return_player_type()
    gb = Board()
    global PLAYING
    PLAYING = True
    INITIAL_MESSAGE = "***   Welcome to Connect4 written in python!   ***\n*** \
  Try your best to beat the computer!   \
   ***\n***   		Goodluck! :)                   ***"
    PLAYER = u_p
    print(INITIAL_MESSAGE)
    while PLAYING:
        gb.display_upsidedown_board()
        if PLAYER == c_p:
            gb.computer_choice()
            PLAYER = u_p
        else:
            gb.valid_drop(1)
            check_winner(gb, user_player, computer_player)
            PLAYER = c_p


def check_winner(gb, user_player, computer_player):
    """
    Checks if the winner is either the user or the computer.
    Displays a win message and asks the user if they want to play again.
    """
    if gb.check_win() == "user":
        user_player.score += 1
        WIN_MESSAGE = f"            Player Score:{user_player.score}\n \
            Computer Score:{computer_player.score}   \n\
***     You win!!!\n\
***     Would you like to play again? y/n\n"
        user_input = input(WIN_MESSAGE)
        if user_input == "y":
            gb.board = np.zeros((gb.row_count, gb.col_count))
        else:
            PLAYING = False
    elif gb.check_win() == "computer":
        computer_player.score += 1
        WIN_MESSAGE = f"            Player Score:{user_player.score}\n \
            Computer Score:{computer_player.score}   \n\
***     Computer Wins!!!\n\
***     Would you like to play again? y/n\n"
        user_input = input(WIN_MESSAGE)
        if user_input == "y":
            gb.board = np.zeros((gb.row_count, gb.col_count))
        else:
            PLAYING = False

play_game()
