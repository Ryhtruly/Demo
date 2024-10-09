import pygame
from src.Object import Object
from src.spriteLoader import load_block


class Block(Object):
   def __init__(self,x, y, size):
       super().__init__(x, y , size, size)
       block = load_block(size)
       self.image.blit(block,(0,0))
       self.mask = pygame.mask.from_surface(self.image)
