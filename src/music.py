
import pygame
from src.confige import MUSIC_BACKGROUND_FILE


def play_background_music(volume=0.5):
    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_BACKGROUND_FILE)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)
