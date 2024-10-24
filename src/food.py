import pygame
from src.object import Object
from src.spriteLoader import load_sprite_sheets


class Food(Object):
    ANIMATION_DELAY = 2

    def __init__(self, x, y, name_food):
        super().__init__(x, y, 32, 32, name="food")
        self.all_sprites = load_sprite_sheets("Items", "Fruits", 32, 32, False)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.animation_count = 0
        self.sprites = self.all_sprites[name_food]
        self.sprite = self.sprites[0]
        self.mask = pygame.mask.from_surface(self.sprite)
        self.collected = False

    def check_collision(self, player):
        if not self.collected and pygame.sprite.collide_mask(player, self):
            self.collected = True
            return True
        return False

    def loop(self):
        if not self.collected:
            if self.animation_count // self.ANIMATION_DELAY >= len(self.sprites):
                self.animation_count = 0

            idx_sprite = (self.animation_count // self.ANIMATION_DELAY) % len(self.sprites)
            self.sprite = self.sprites[idx_sprite]
            self.animation_count += 1

            self.mask = pygame.mask.from_surface(self.sprite)

    # @override draw method
    def draw(self, win, offset_x):
        if not self.collected:
            win.blit(self.sprite,  (self.rect.x - offset_x, self.rect.y))


class Banana(Food):
    def __init__(self, x, y):
        super().__init__(x, y, "Bananas")


class Apple(Food):
    def __init__(self, x, y):
        super().__init__(x, y, "Apple")


class Strawberry(Food):
    def __init__(self, x, y):
        super().__init__(x, y, "Strawberry")


class Melon(Food):
    def __init__(self, x, y):
        super().__init__(x, y, "Melon")