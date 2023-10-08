import pygame

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.animation_dict = {}

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        sprite = pygame.transform.scale(sprite, (w * 4, h * 4))
        return sprite

    def create_dict(self, frames, names):
        for i, num_frames in enumerate(frames):
            animation = []  
            for frame_index in range(num_frames):
                sprite = self.get_sprite(frame_index * 32, i * 32, 32, 32)
                animation.append(sprite)
            self.animation_dict[names[i]] = animation

