""""
Author: Piseth Chuon
Tic Tac Toe Game using Pygame library
"""

import pygame
import sys

pygame.init()

# SET UP THE GAME WINDOW
# Constrants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 6
BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# DRAE THE GAME GRID
def draw_lines():
    # Horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), LINE_WIDTH)
    
    # Vertical
    pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 300), LINE_WIDTH)

draw_lines()

# Step 3: Create the Game Board
borad = [[0 for _ in range(3)] for _ in range(3)]

# Step 4: Handle Player Clicks
player = 2

def mark_square(row, col, player):
    borad[row][col] = player

def is_square_empty(row, col):
    return borad[row][col] == 0

def get_clicked_row_col(pos):
    x, y = pos
    row = y // 100
    col = x // 100
    return row, col

def draw_figures():
    for row in range(3):
        for col in range(3):
            if borad[row][col] == 1:
                pygame.draw.line(screen, (255, 0, 0), (col*100 + 20, row*100 + 20), (col*100 + 80, row*100 + 80), 4)
                pygame.draw.line(screen, (255, 0, 0), (col*100 + 20, row*100 + 80), (col*100 + 80, row*100 + 20), 4)
            elif borad[row][col] == 2:
                pygame.draw.circle(screen, (0, 0, 255), (col*100 + 50, row*100 + 50), 30, 4)

def check_win(player):
    # Horizontal
    for row in borad:
        if row.count(player) == 3:
            return True
    
    # Vertical
    for col in range(3):
        if all([borad[row][col] == player for row in range(3)]):
            return True

    # Diagonal
    if all([borad[i][i] == player for i in range(3)]) or all([borad[i][2 - i] == player for i in range(3)]):
        return True
    
    return False

game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            row, col = get_clicked_row_col(pos)

            if is_square_empty(row, col):
                mark_square(row, col, player)
                if check_win(player):
                    print(f"Player {player} wins!")
                    game_over = True
                player = 2 if player == 1 else 1
                draw_figures()

    pygame.display.update()

