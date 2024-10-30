
import pygame.font
from src.confige import FONT_SCORE, WHITE, SCORE_POS, DATA_FILE, FONT_LEADERBOARD, GREY, WIDTH, HEIGHT
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
        self.text_surface = self.font.render(f"YOUR SCORE: {self.score}           |           HIGHEST SCORE: "
                                             f"{self.highest_score}",True, WHITE)
        text_rect = self.text_surface.get_rect(topleft=SCORE_POS)
        padding = 10
        pygame.draw.rect(window, GREY, (text_rect.x - padding, text_rect.y - padding, text_rect.width + padding * 2, text_rect.height + padding * 2))
        window.blit(self.text_surface, text_rect.topleft)

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


def get_player_name(window):
    pygame.font.init()
    font = pygame.font.SysFont(None, 48)
    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)
    color_inactive = pygame.Color('light gray')
    color_active = pygame.Color('deepskyblue')
    color = color_inactive
    active = False
    text = ''

    background, bg_image = get_background('rsz_new3.png')

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
        for tile in background:
            window.blit(bg_image, tile)

        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        input_box.centerx = WIDTH // 2
        window.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(window, color, input_box, 2)

        instruction_surface = font.render("Enter Your Name:", True, (255, 255, 255))

        instruction_x = (WIDTH - instruction_surface.get_width()) // 2
        instruction_y = HEIGHT // 2 - 100
        window.blit(instruction_surface, (instruction_x, instruction_y))

        pygame.display.flip()