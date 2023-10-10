import pygame
from components.Sheet_Handler import Spritesheet
from constants.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.locals import (
    K_w,
    K_a,
    K_s,
    K_d,
    K_j,
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.PlayerSheet = Spritesheet('constants/playersheet.png')
        self.PlayerSheet.create_dict([5, 8, 7, 3, 7], ['idle', 'run', 'hit', 'squat', 'die'])
        self.PlayerSheet_left = Spritesheet('constants/playersheet_left.png')
        self.PlayerSheet_left.create_dict([5, 8, 7, 3, 7], ['idle', 'run', 'hit', 'squat', 'die'])
        self.frame = 0
        self.state = 'idle'
        self.sprite = self.PlayerSheet.animation_dict[self.state][self.frame]
        self.rect = self.sprite.get_rect()
        self.interval = 4
        self.direction = 0
        self.mask = pygame.mask.from_surface(self.sprite)
        self.looping_animation = False
        

    def update(self, pressed_keys):
        sprites = self.PlayerSheet_left.animation_dict[self.state] if self.direction else self.PlayerSheet.animation_dict[self.state]
        sprite_index = (self.frame // self.interval) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.frame += 1 
        if pressed_keys[K_j]:
            self.state = 'hit'
            self.looping_animation = True
            self.frame=0
        if (self.frame // self.interval) % len(sprites) == len(sprites)-1: self.looping_animation = False ; self.frame=0
        if not self.looping_animation:
            self.state = 'idle'
            if pressed_keys[K_w]:
                self.direction = 0
                self.state = 'run'
                self.rect.move_ip(0, -5)
            if pressed_keys[K_s]:
                self.direction = 1
                self.state = 'run'
                self.rect.move_ip(0, 5)
            if pressed_keys[K_a]:
                self.direction = 1
                self.state = 'run'
                self.rect.move_ip(-5, 0)
            if pressed_keys[K_d]:
                self.direction = 0
                self.state = 'run'
                self.rect.move_ip(5, 0)

        # Update the mask after moving
        self.mask = pygame.mask.from_surface(self.sprite)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
