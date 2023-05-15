import pygame
import random


# 5 || 10 || 25 || 50 ..., bigger is more computational intence
BOARD_ROWS = 25
BOARD_COLS = 25


def draw_squares(board, rows, cols):
    for r in range(rows):
        for c in range(cols):
            x = r * (square_size)
            y = c * (square_size)
            if board[r][c] == 1:
                pygame.draw.rect(screen, (200, 0, 0), (x, y, square_size, square_size))
            else:
                board[r][c] = 0
                pygame.draw.rect(screen, (255, 255, 255), (x, y, square_size, square_size))


def get_neighbors(board, r0, c0):
    nbors = []
    for dr in range (-1, 2):
        for dc in range (-1, 2):
            if dr != 0 or dc != 0:
                r = r0 + dr
                c = c0 + dc
                if 0 <= r and r < BOARD_ROWS:
                    if 0 <= c and c < BOARD_COLS:
                        nbors.append(board[r][c])

    return nbors

def next_board(current_board):
    next_board = current_board
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            nbrs = get_neighbors(current_board, row, col)
            if current_board[row][col] == 0:
                if nbrs.count(1) == 3:
                    next_board[row][col] = 1
                else:
                    next_board[row][col] = 0
            elif  current_board[row][col] == 1:
                if nbrs.count(1) == 2 or nbrs.count(1) == 3:
                    next_board[row][col] = 1
                else:
                    next_board[row][col] = 0

    return next_board

# Initialize Pygame
pygame.init()

# Set the screen size and create a window
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the square size
square_size = screen_width / BOARD_ROWS

# more/less 0(zeros) in the list changes the initial board
current_board = [[random.choice([0,0,0,0,0,0,1]) for col in range(BOARD_COLS)] for row in range(BOARD_ROWS)]


# Calculate the number of squares
num_squares = int(BOARD_ROWS * BOARD_COLS)

clock = pygame.time.Clock() 

draw_squares(current_board, BOARD_ROWS, BOARD_COLS)

# Update the screen and wait for the user to close the window
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    

    updated_board = next_board(current_board)
    current_board = updated_board

    draw_squares(current_board, BOARD_ROWS, BOARD_COLS)
    pygame.display.flip()
    clock.tick(1)
