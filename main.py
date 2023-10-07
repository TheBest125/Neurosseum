import pygame
from constants.constants import SCREEN_WIDTH,SCREEN_HEIGHT
from entities.player import Player
from pygame.locals import (
KEYDOWN,
QUIT,
K_ESCAPE
)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

player = Player()

pygame.init()

while(running):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == QUIT:
            running = False
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    screen.fill((0, 0, 0))
    screen.blit(player.surf, player.rect)
    pygame.display.flip()
    clock.tick(60)