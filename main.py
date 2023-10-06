import pygame

from pygame.locals import (
K_w,
K_a,
K_s,
K_d,
K_j,
K_k,
K_ESCAPE,
KEYDOWN,
QUIT
)
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True

while running:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.type == K_ESCAPE:
                running = False
        elif event.type ==QUIT:
            running = False