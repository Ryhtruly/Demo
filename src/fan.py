import pygame
from src.spriteLoader import load_sprite_sheets
from src.block import Block


class Fan(Block):
    ANIMATION_DELAY = 3
    MOVE_SPEED = 1.65

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width)
        self.fan_images = load_sprite_sheets("Traps", "Fan", width, height)
        self.frames = self.fan_images["Off"]
        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.animation_count = 0
        self.animation_name = "Off"
        self.mask = pygame.mask.from_surface(self.image)
        self.moving_up = True
        self.start_y = y
        self.end_y = y - 550

    def on(self):
        self.animation_name = "On"
        self.frames = self.fan_images["On"]

    def off(self):
        self.animation_name = "Off"
        self.frames = self.fan_images["Off"]

    def loop(self):
        sprites = self.frames
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
            self.animation_count = 0

        if self.moving_up:
            self.rect.y -= self.MOVE_SPEED
            if self.rect.y <= self.end_y:
                self.moving_up = False
        else:
            self.rect.y += self.MOVE_SPEED
            if self.rect.y >= self.start_y:
                self.moving_up = True
