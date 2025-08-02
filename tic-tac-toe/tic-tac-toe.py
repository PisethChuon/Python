import pygame
import sys

pygame.init()

# Constrants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 6
BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)