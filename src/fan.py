import pygame
from src.spriteLoader import load_sprite_sheets
from src.block import Block

class BaseFan(Block):
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
        self.start_pos = None
        self.end_pos = None

    def reset(self):
        self.animation_count = 0

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

        self.move()

    def move(self):
        # Được override bởi các lớp con
        pass

class VerticalFan(BaseFan):
    def __init__(self, x, y, width, height, distance=400):
        super().__init__(x, y, width, height)
        self.moving_up = True
        self.start_y = y
        self.end_y = y - distance

    def move(self):
        if self.moving_up:
            self.rect.y -= self.MOVE_SPEED
            if self.rect.y <= self.end_y:
                self.moving_up = False
        else:
            self.rect.y += self.MOVE_SPEED
            if self.rect.y >= self.start_y:
                self.moving_up = True

class HorizontalFan(BaseFan):
    def __init__(self, x, y, width, height, distance=550):
        super().__init__(x, y, width, height)
        self.moving_right = True
        self.start_x = x
        self.end_x = x + distance

    def move(self):
        if self.moving_right:
            self.rect.x += self.MOVE_SPEED
            if self.rect.x >= self.end_x:
                self.moving_right = False
        else:
            self.rect.x -= self.MOVE_SPEED
            if self.rect.x <= self.start_x:
                self.moving_right = True

# Các lớp cũ có thể được thay thế bằng các lớp mới như sau:
class Fan(VerticalFan):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, 400)

class Fan_M(VerticalFan):
    def __init__(self, x, y, width, height, num):
        super().__init__(x, y, width, height, num)

class FanRow(HorizontalFan):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, 550)

class Fan_N(HorizontalFan):
    def __init__(self, x, y, width, height, num):
        super().__init__(x, y, width, height, num)
