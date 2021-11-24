# Python Connect4

Python Connect4 is a python terminal implementation of the classic connect 4 game.
It runs in the [Code Institue](https://codeinstitute.net/all-access-coding-challenge/?utm_term=code%20institute&utm_campaign=CI+-+IRL+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14304747355&hsa_grp=128775288209&hsa_ad=539453915484&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAiAv_KMBhAzEiwAs-rX1PXOCAky8yjljHzgvSnccpkyUOvNLVGMuzG11t86weTdFdPiTfNHHhoCFuwQAvD_BwE) mock terminal on [Heroku](https://id.heroku.com/login).

The user can play a connect four game against the computer.

[Try it out here (Link to external site)](https://connect4-python.herokuapp.com/)

![Am-I-Responsive-Connect4](images/connect-4-air.png)

## How to play

Python Connect4 is based on the classic tabletop game connect 4.

* Connect Four (also known as Four Up, Plot Four, Find Four, Captain's Mistress, Four in a Row, Drop Four, and Gravitrips in the Soviet Union) is a two-player connection board game, in   which the players choose a color and then take turns dropping colored discs into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs. Connect Four is a solved game. The first player can always win by playing the right moves. The game was first sold under the Connect Four trademark[3] by Milton Bradley in February 1974. [Wikipedia, 2021](https://en.wikipedia.org/wiki/Connect_Four)

## Data Model

I decided to use a board class as my model. The game creates an instance of the board when the game starts.

The board class stores the board, size and if the game is currently playing. The board also has moethpds to help play the game. Such as a `print_board` method to print out the current board. A `valid_drop` method to check if there is space in the chosen column and what row that space is. A `dropping_piece` method to create a print animation to drop the piece into the board.

## Testing

I have manually tested this project by doing the following:
    * Passed the code through [PEP8](http://pep8online.com/checkresult) linter and confirmed there are no warnings or errors.
    * Given invalid inputes: strings when numbers are expected, out of bounds inputs, the same input twice.
    * Tested in both local and deployed terminals.

## Bugs

### Solved Bugs
When creating the 'check_win' function I was getting out of bounds in array errors for some win conditions. I noticed this would be because to check
if the user has won the conditions had row + 1, row + 2 and row + 3 ( with the same for columns). If the board position was ( 5, 3) then row +3 would cause the final value of 
8 to be greater than the actual number of rows available to check. My first idea for a fix was just to add:

    ```python
    if (row + 3) <= 6:
        Check for wins
    ```