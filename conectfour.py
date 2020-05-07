import  numpy as np
#to make graphics we import pygame library
import pygame



#static unchanging variables are in caps
ROW_COUNT = 6
COLUMN_COUNT = 7

#can call np anything, tried custom and it worked
def create_board():
    #creates a board of all zeros with 6 rows 7 colums
    board = np.zeros((6,7))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece


#take current board and current column
def is_valid_loction(board, col):
    return board[5][col] == 0
    #return true if top location in column is a 0 value, will change to 1 for p1 turns and 2 for p2 turns

    #pass is same as return 0, used as a placeholder

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        #check board condidtion, returning first case that row = 0 in the column starting from y = 0 on a grid. check r statis in the column and return lowest "0" location, i.e acceptable spot
        if board[r][col] == 0:
            return r

def print_board(board):
    #used to make bottom up display, not top down, this py command will flip (board, over x axis)
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Check horizontal locations for win, 3 of th ecolumns cant win because you checked upto 3 from the right wall

    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True


#create board, and starting conditions
board = create_board()
game_over = False
#whos turn is it? 1 for p1, 2 for p2
turn = 0
#if using pygame you must init it before you can use it
pygame.init()
#define screen size
SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = ROW_COUNT+1 * SQUARESIZE

size = (width, height)
#can get all pygame code from their website
screen = pygame.display.set_mode(size)
#make game loop
while not game_over:
    # Ask for p1 input
    if turn == 0:
        col = int(input("p1 make your selection (0-6):"))
        if is_valid_loction(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
        #print(col)
        #show the variable type for selection, i.e string int ect
       # print(type(col))

#Ask for p2 input
    elif turn == 1:
        col = int(input("p2 make your selection (0-6):"))
        if is_valid_loction(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
    #this will alternate between player 1 turn and player 2 turn, 0%2 = 0, 1%2 = 1
    turn += 1
    turn = turn % 2
    print_board(board)

    if winning_move(board, 1):
        print(("Player one wins!!!"))
        game_over = True