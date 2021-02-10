#! /usr/bin/env python3

import pygame
pygame.init()

# Keystrokes
from pygame.locals import (
    K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, K_RETURN, QUIT
)

# Colors
COLOR_BLUE = (0, 0, 205)
COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)

# Primary Screen
screen = pygame.display.set_mode([500, 550])
screen.fill(COLOR_WHITE)

# for point in range(0, 501, 50):
#     pygame.draw.line(surface, (0, 255, 255), (point, 0), (point, 500))

# for point in range(0, 501, 50):
#     pygame.draw.line(surface, (0, 255, 255), (0, point), (500, point))

class GameBoard():
    def __init__(self):
        self.draw_game_board()
        pygame.display.flip()

    def draw_game_board(self):
        pygame.draw.rect(screen, COLOR_BLUE, pygame.Rect(25, 80, 450, 450))
        for y_axis in range(130, 500, 70):
            for x_axis in range(75, 480, 70):
                pygame.draw.circle(screen, COLOR_WHITE, (x_axis, y_axis), 30)

connect_four = GameBoard()

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_LEFT:
                print('Left key is pressed')
            elif event.key == K_RIGHT:
                print('Right key is pressed')
            elif event.key == K_RETURN:
                print('Return key is pressed')
    pygame.display.flip()

pygame.quit()
    