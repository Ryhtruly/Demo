
import pygame.font
from src.confige import FONT_SCORE, WHITE, SCORE_POS, DATA_FILE, FONT_LEADERBOARD
from src.spriteLoader import get_highest_score
import pandas as pd
from src.spriteLoader import get_background


class ScoreBoard:
    def __init__(self, player_name, map_level):
        self.score = 0
        self.highest_score = get_highest_score()
        self.font = pygame.font.SysFont(*FONT_SCORE)
        self.font_board = pygame.font.SysFont(*FONT_LEADERBOARD)
        self.player_name = player_name
        self.map_level = map_level
        self.text_surface = None

    def increase_score(self):
        self.score += 1

    def draw_score(self, window):
        self.text_surface = self.font.render(f"Your Score: {self.score}, HIGHEST SCORE: {self.highest_score}",
                                             True, WHITE)
        window.blit(self.text_surface, SCORE_POS)

    def update_data(self):
        """use at the end of game"""
        new_data = pd.DataFrame({
            'name': [self.player_name],
            'score': [self.score],
            'map': [self.map_level]
        })

        try:
            leaderboard = pd.read_csv(DATA_FILE)
            leaderboard = pd.concat([leaderboard, new_data], ignore_index=True)
        except FileNotFoundError:
            leaderboard = new_data

        leaderboard = leaderboard.sort_values(by='score', ascending=False)
        self.highest_score = leaderboard.iloc[0]

        leaderboard.to_csv(DATA_FILE, index=False)


def get_player_name(window, WIDTH, HEIGHT):
    pygame.font.init()
    font = pygame.font.SysFont(None, 48)
    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''

    background, bg_image = get_background('new3.png')
    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text:
                            return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        window.blit(bg_image, (0, 0))

        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        window.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(window, color, input_box, 2)

        instruction_surface = font.render("Enter your name:", True, (0, 0, 0))
        window.blit(instruction_surface, (WIDTH // 2 - 100, HEIGHT // 2 - 100))

        pygame.display.flip()