import pygame
from src.spriteLoader import load_sprite_sheets
from src.block import Block

class BaseSaw(Block):
    ANIMATION_DELAY = 3
    MOVE_SPEED = 1.65

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width)
        self.fan_images = load_sprite_sheets("Traps", "Saw", width, height)
        self.frames = self.fan_images["off"]
        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.animation_count = 0
        self.animation_name = "off"
        self.mask = pygame.mask.from_surface(self.image)

    def reset(self):
        self.animation_count = 0

    def on(self):
        self.animation_name = "on"
        self.frames = self.fan_images["on"]

    def off(self):
        self.animation_name = "off"
        self.frames = self.fan_images["off"]

    def animate(self):
        sprites = self.frames
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
            self.animation_count = 0

    def move(self):
        pass

    def loop(self):
        self.animate()
        self.move()

class MovingSaw(BaseSaw):
    def __init__(self, x, y, width, height, distance):
        super().__init__(x, y, width, height)
        self.start_pos = 0
        self.end_pos = distance
        self.moving_positive = True

class VerticalSaw(MovingSaw):
    def __init__(self, x, y, width, height, distance, move_down=False):
        super().__init__(x, y, width, height, distance)
        self.start_y = y
        self.end_y = y + distance if move_down else y - distance
        self.moving_down = move_down

    def move(self):
        if self.moving_down:
            if self.moving_positive:
                self.rect.y += self.MOVE_SPEED
                if self.rect.y >= self.end_y:
                    self.moving_positive = False
            else:
                self.rect.y -= self.MOVE_SPEED
                if self.rect.y <= self.start_y:
                    self.moving_positive = True
        else:
            if self.moving_positive:
                self.rect.y -= self.MOVE_SPEED
                if self.rect.y <= self.end_y:
                    self.moving_positive = False
            else:
                self.rect.y += self.MOVE_SPEED
                if self.rect.y >= self.start_y:
                    self.moving_positive = True

class HorizontalSaw(MovingSaw):
    def __init__(self, x, y, width, height, distance, move_left=False):
        super().__init__(x, y, width, height, distance)
        self.start_x = x
        self.end_x = x - distance if move_left else x + distance
        self.moving_left = move_left

    def move(self):
        if self.moving_left:
            if self.moving_positive:
                self.rect.x -= self.MOVE_SPEED
                if self.rect.x <= self.end_x:
                    self.moving_positive = False
            else:
                self.rect.x += self.MOVE_SPEED
                if self.rect.x >= self.start_x:
                    self.moving_positive = True
        else:
            if self.moving_positive:
                self.rect.x += self.MOVE_SPEED
                if self.rect.x >= self.end_x:
                    self.moving_positive = False
            else:
                self.rect.x -= self.MOVE_SPEED
                if self.rect.x <= self.start_x:
                    self.moving_positive = True

class Saw(BaseSaw):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

class Saw_Collum(VerticalSaw):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, 300, move_down=False)

class Saw_Collum2(VerticalSaw):
    def __init__(self, x, y, width, height, num):
        super().__init__(x, y, width, height, num, move_down=True)

class Saw_Row(HorizontalSaw):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, 300, move_left=False)

class Saw_Row2(HorizontalSaw):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, 300, move_left=True)

class Saw_Row_N(HorizontalSaw):
    def __init__(self, x, y, width, height, num):
        super().__init__(x, y, width, height, num, move_left=False)

class Saw_Row_N2(HorizontalSaw):
    def __init__(self, x, y, width, height, num):
        super().__init__(x, y, width, height, num, move_left=True)

class Saw_Collum_N(VerticalSaw):
    def __init__(self, x, y, width, height, num):
        super().__init__(x, y, width, height, num, move_down=True)

class Saw_Collum3(VerticalSaw):
    def __init__(self, x, y, width, height, num):
        super().__init__(x, y, width, height, num, move_down=False)
