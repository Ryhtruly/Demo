
import pygame.font
from src.confige import FONT_SCORE, WHITE, SCORE_POS, DATA_FILE
from src.spriteLoader import get_highest_score
import pandas as pd


class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.highest_score = get_highest_score()
        self.font = pygame.font.SysFont(*FONT_SCORE)
        self.text_surface = None
        # self.update_data(player_name, map_level)

    def increase_score(self):
        self.score += 1

    def draw_score(self, window):
        self.text_surface = self.font.render(f"Your Score: {self.score}, HIGHEST SCORE: {self.highest_score}",
                                             True, WHITE)
        window.blit(self.text_surface, SCORE_POS)

    def update_data(self, player_name, map_level):
        """use at the end of game"""
        new_data = pd.DataFrame({
            'name': [player_name],
            'score': [self.score],
            'map': [map_level]
        })

        try:
            leaderboard = pd.read_csv(DATA_FILE)
            leaderboard = pd.concat([leaderboard, new_data], ignore_index=True)
        except FileNotFoundError:
            leaderboard = new_data

        leaderboard = leaderboard.sort_values(by='score', ascending=False)
        self.highest_score = leaderboard.iloc[0]

        leaderboard.to_csv(DATA_FILE, index=False)

