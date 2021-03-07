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
COLOR_BLACK = (0, 0, 0)

screen = pygame.display.set_mode([570, 550])

# for point in range(0, 501, 50):
#     pygame.draw.line(surface, (0, 255, 255), (point, 0), (point, 500))

# for point in range(0, 501, 50):
#     pygame.draw.line(surface, (0, 255, 255), (0, point), (500, point))

class GameBoard():
    def draw_game_board(self):
        screen.fill(COLOR_WHITE)
        pygame.draw.rect(screen, COLOR_BLUE,
                         pygame.Rect(25, 80, 520, 450))

        for y_axis in range(130, 510, 70):
            for x_axis in range(75, 510, 70):
                pygame.draw.circle(screen, COLOR_WHITE,
                                   (x_axis, y_axis), 30)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.circle = pygame.Surface((75, 25))
        self.circle.fill(COLOR_BLACK)
        self.rect = self.circle.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-25, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(25, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 530:
            self.rect.right = 500

connect_four = GameBoard()
player = Player()

clock = pygame.time.Clock()

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

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    connect_four.draw_game_board()

    screen.blit(player.circle, player.rect)
    pygame.display.flip()

    clock.tick(40)

pygame.quit()
    