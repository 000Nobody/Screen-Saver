import pygame
from random import random

from classes.Board import Board
from classes.Ball import Ball

WINDOW_SIZE = (1000, 1000)
screen = pygame.display.set_mode(WINDOW_SIZE)

color1 = (80, 80, 85)
color2 = (20, 20, 25)
ball1_vel = [1, -1.7] #[random()*-3, random()*3]
ball2_vel = [-1, 1.5] #[random()*3, random()*-3]

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1], 10, 10, (color1, color2))
ball1 = Ball(
    board.all_tiles,
    (100, 500),
    25,
    colors=(color1, color2),
    init_vel=ball1_vel
)

ball2 = Ball(
    board.all_tiles,
    (700, 100),
    25,
    colors=(color1, color2),
    init_vel=ball2_vel
)

# ball3 = Ball(board.all_tiles, (100, 500), 15, colors=(color1, color2), init_vel=[-2, 1])
# ball4 = Ball(board.all_tiles, (700, 100), 15, colors=(color1, color2), init_vel=[2, 1])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(color1)

    board.draw(screen)

    ball1.update(screen)
    ball2.update(screen)
    # ball3.update(screen)
    # ball4.update(screen)

    pygame.display.update()
