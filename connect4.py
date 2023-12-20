import numpy as np

rows = 6
cols = 7

def create_board():
    #Initializes a board
    board = np.zeros((6,7))
    return board

def drop_piece(board, row, col, piece):
    #"Drops" a piece into the board
    board[row][col] = piece

def is_valid_location(board, col):
    #checks the row has an open spot to place a piece
    return board[5][col] == 0

def get_next_open_row(board, col):
    #returns the first available spot to place a piece
    for i in range(rows):
        if board[i][col] == 0:
            return i

def print_board(board):
    #prints an inverted board to match what players see
    print(np.flip(board, 0))

turn = 0
board = create_board()
print_board(board)
game_over = False

while not game_over:
    #Player 1 input
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6): "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

    #Player 2 input
    else:
        col = int(input("Player 2 Make your Selection (0-6): "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

    print_board(board)

    turn += 1
    turn = turn % 2