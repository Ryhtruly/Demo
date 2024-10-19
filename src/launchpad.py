
import pygame
from src.Object import Object
from src.spriteLoader import load_sprite_sheets

class LaunchPad(Object):
    ANIMATION_DELAY = 3
    LAUNCH_FORCE = -30

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "launchpad")
        self.sprites = load_sprite_sheets("Traps", "Trampoline", width, height)
        self.image = self.sprites["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Idle"
        self.launch_power = -60

    def animate(self):
        self.animation_name = "Idle"
        self.animation_count = 0

    def loop(self):
        sprites = self.sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
            if self.animation_name == "Jump":
                self.animation_name = "Idle"

    # New method to launch the player
    def launch(self, player):
        player.y_vel = self.launch_power

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))
