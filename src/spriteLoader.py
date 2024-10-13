import pygame
from os import listdir
from os.path import isfile, join
from src.confige import WIDTH, HEIGHT, DATA_FILE
import os
import pandas as pd

def flip(sprites):
   return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, directon = False):
   path = join("assets", dir1, dir2)
   images = [f for f in listdir(path) if isfile(join(path,f))]


   all_sprites = {}


   for image in images:
       sprite_sheet = pygame.image.load(os.path.join(path, image))


       sprites = []
       for i in range(sprite_sheet.get_width() // width):
           surface = pygame.Surface((width,height), pygame.SRCALPHA, 32)
           rect = pygame.Rect(i * width, 0, width, height)
           surface.blit(sprite_sheet, (0,0), rect)
           sprites.append(pygame.transform.scale2x(surface))


       if directon:
           all_sprites[image.replace(".png","") + "_right"] = sprites
           all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
       else:
           all_sprites[image.replace(".png","")] = sprites


   print("All Sprites Loaded:", all_sprites)


   return all_sprites




def load_block(size):
   path = join("assets","Terrain", "Terrain.png")
   image = pygame.image.load(path).convert_alpha()
   surface = pygame.Surface((size,size), pygame.SRCALPHA, 32)
   rect = pygame.Rect(0 ,0, size, size)
   surface.blit(image, (0,0), rect)
   return pygame.transform.scale2x(surface)


def get_background(name) :
   image = pygame.image.load(join("assets","Background", name))
   _,_, width, height = image.get_rect()
   tiles = []


   for i in range(WIDTH // width +  1):
       for j in range(HEIGHT // height + 1):
           pos = [ i * width, j * height]
           tiles.append(pos)


   return tiles, image


def draw(window , background, bg_image, player, object , offset_x, score_board):
   for tile in background:
       window.blit(bg_image, tile)


   for obj in object:
       obj.draw(window, offset_x)

   score_board.draw_score(window)

   player.draw(window, offset_x)
   pygame.display.update()


def get_highest_score():
    try:
        leaderboard = pd.read_csv(DATA_FILE)
        if leaderboard.empty:
            return 0
        return leaderboard['score'].iloc[0]
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return 0
