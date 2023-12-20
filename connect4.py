import numpy as np
import pygame
import sys
import math

BLUE = (0, 0, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
rows = 6
cols = 7

def create_board():
    #Initializes a board
    board = np.zeros((rows,cols))
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

def winning_board(board, piece):
    #Check horizontal wins
    for i in range(cols - 3):
        for b in range(rows):
            if board[b][i] == piece and board [b][i+1] ==  piece and board [b][i+2] == piece and board [b][i+3]:
                return True
    
    #Check Vertical wins
    for i in range(cols):
        for b in range(rows - 3):
            if board[b][i] == piece and board [b+1][i] ==  piece and board [b+2][i] == piece and board [b+3][i]:
                return True
    
    #Check Upwards sloping diagonal wins
    for i in range(cols - 3):
        for b in range(rows - 3):
            if board[b][i] == piece and board [b+1][i+1] ==  piece and board [b+2][i+2] == piece and board [b+3][i+3]:
                return True

    #check Downwards sloping diagonal wins
    for i in range(cols - 3):
        for b in range(3, rows):
            if board[b][i] == piece and board [b-1][i+1] ==  piece and board [b-2][i+2] == piece and board [b-3][i+3]:
                return True
            
def draw_board(board):
    for i in range(cols):
        for b in range(rows):
            pygame.draw.rect(screen, BLUE, (i*squaresize, b*squaresize + squaresize, squaresize, squaresize))
            pygame.draw.circle(screen, BLACK, (int(i*squaresize + squaresize/2), int(b*squaresize + squaresize + squaresize/2)), radius)
    
    for i in range(cols):
        for b in range(rows):
            if board[b][i] == 0:
                circolor = BLACK
            elif board[b][i] == 1:
                circolor = RED
            elif board[b][i] == 2:
                circolor = YELLOW
            pygame.draw.circle(screen, circolor, (int(i*squaresize + squaresize/2), height - int(b*squaresize + squaresize/2)), radius)
    pygame.display.update()


turn = 0
board = create_board()
print_board(board)
game_over = False

pygame.init()

squaresize = 100
width = squaresize * cols
height = squaresize * (rows + 1)
radius = int(squaresize/2 - 5)

size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, squaresize))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(squaresize/2)), radius)
            if turn == 1:
                pygame.draw.circle(screen, YELLOW, (posx, int(squaresize/2)), radius)
        pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            pygame.draw.rect(screen, BLACK, (0, 0, width, squaresize))

            #Player 1 input
            if turn == 0:

                posx = event.pos[0]
                col = int(math.floor(posx/squaresize))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_board(board, 1):
                        label = myfont.render("Player 1 Wins!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True

            #Player 2 input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/squaresize))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_board(board, 1):
                        label = myfont.render("Player 2 Wins!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

            print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 2
            
            if game_over:
                pygame.time.wait(3000)