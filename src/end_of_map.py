import pygame
from src.object import Object
from src.spriteLoader import load_sprite_sheets

image_path = "assets/Items/Checkpoint/End"


class LastPoint(Object):
    ANIMATION_DELAY = 2

    def __init__(self, x, y):
        super().__init__(x, y, 64, 64, name="LastPoint")
        self.all_sprites = load_sprite_sheets("Items", "Checkpoints\\End", 64, 64, False)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.animation_count = 0
        self.sprites = self.all_sprites["End (Pressed) (64x64)"]
        self.image = self.sprites[0]
        self.mask = pygame.mask.from_surface(self.image)

    def loop(self):
        if self.animation_count // self.ANIMATION_DELAY >= len(self.sprites):
            self.animation_count = 0

        idx_sprite = (self.animation_count // self.ANIMATION_DELAY) % len(self.sprites)
        self.image = self.sprites[idx_sprite]
        self.animation_count += 1

        self.mask = pygame.mask.from_surface(self.image)