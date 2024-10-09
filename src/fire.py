import pygame
from src.spriteLoader import load_sprite_sheets
from src.block import Block


class Fire(Block):
   ANIMATION_DELAY = 3


   def __init__(self, x, y, width, height):
       super().__init__(x, y, width)
       self.fire = load_sprite_sheets("Traps", "Fire", width, height)
       self.image = self.fire["off"][0]
       self.mask = pygame.mask.from_surface(self.image)
       self.animation_count = 0
       self.animation_name = "on"


   def on(self):
       self.animation_name = "on"


   def off(self):
       self.animation_name = "off"


   def loop(self):
       sprites = self.fire[self.animation_name]
       sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
       self.image = sprites[sprite_index]
       self.animation_count += 1


       self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
       self.mask = pygame.mask.from_surface(self.image)


       if self.animation_count // self.ANIMATION_DELAY > len(sprites):
           self.animation_count = 0




def draw(window , background, bg_image, player, object , offset_x):
   for tile in background:
       window.blit(bg_image, tile)


   for obj in object:
       obj.draw(window, offset_x)


   player.draw(window, offset_x)
   pygame.display.update()
