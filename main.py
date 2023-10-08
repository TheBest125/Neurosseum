import pygame

from constants.constants import SCREEN_WIDTH,SCREEN_HEIGHT,FPS

pygame.init()



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

from entities.player import Player

from components.Sheet_Handler import Spritesheet

from pygame.locals import (
KEYDOWN,
QUIT,
K_ESCAPE
)



clock = pygame.time.Clock()

running = True

frames=0

player = Player()


while(running):

    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:

                running = False

        if event.type == QUIT:

            running = False

    pressed_keys = pygame.key.get_pressed()
    
    player.update(pressed_keys)

    screen.fill((255, 255, 255))

    screen.blit(player.sprite, player.rect)
    
    pygame.display.flip()

    clock.tick(FPS)