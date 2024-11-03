import pygame
import sys
from os.path import join
from src.confige import WIDTH, HEIGHT, BLACK, DATA_FILE, FONT_LEADERBOARD, LEADERBOARD_POS, WHITE
import pandas as pd

start_img = pygame.image.load(join("assets", "Other", "start_btn.png"))
exit_img = pygame.image.load(join("assets", "Other", "exit_btn.png"))
leaderboard_image = pygame.image.load(join("assets", "Menu", "Buttons", "LeaderBoard.png"))
introduction_image = pygame.image.load(join("assets", "Menu", "Buttons", "introductionicon.png"))

def x_cor_center(window_width, element_width):
    return (window_width - element_width) // 2


def draw_intro_screen(window):
    intro_bg_image = pygame.image.load(join("assets", "Background", "rsz_new3.png"))
    intro_bg_width, intro_bg_height = intro_bg_image.get_size()

    for x in range(0, WIDTH, intro_bg_width):
        for y in range(0, HEIGHT, intro_bg_height):
            window.blit(intro_bg_image, (x, y))

    font = pygame.font.SysFont(None, 60)
    title_text = font.render('WELCOME TO FUNNY ADVENTURE GAME!', True, (255, 255, 255))
    window.blit(title_text, ((WIDTH - title_text.get_width()) // 2, 100))

    start_img_width, start_img_height = start_img.get_size()

    start_button_x = (WIDTH - start_img_width) // 2
    start_button_y = 215
    start_button_rect = pygame.Rect(start_button_x, start_button_y, start_img_width, start_img_height)


    exit_img_width, exit_img_height = exit_img.get_size()
    exit_button_x = (WIDTH - exit_img_width) // 2
    exit_button_y = start_button_y + start_img_height + 40
    exit_button_rect = pygame.Rect(exit_button_x, exit_button_y, exit_img_width, exit_img_height)


    width_board, height_board = leaderboard_image.get_size()
    width_board *= 3
    height_board *= 3
    leaderboard_image_scale = pygame.transform.scale(leaderboard_image, (width_board*1.4, height_board*1.4))
    x_leaderboard = x_cor_center(WIDTH, width_board*1.4)
    y_leaderboard = exit_button_y + exit_img_height + 40
    leaderboard_button = pygame.Rect(x_leaderboard, y_leaderboard, width_board, height_board)

    width_intro, height_intro = introduction_image.get_size()
    introduction_image_scaled = pygame.transform.scale(introduction_image, (width_intro // 4, height_intro // 4))
    x_intro_button = x_cor_center(WIDTH, width_intro//4)
    y_intro_button = y_leaderboard + height_board // 3 + 80
    intro_button = pygame.Rect(x_intro_button, y_intro_button, width_intro, height_intro)


    window.blit(exit_img, exit_button_rect.topleft)
    window.blit(start_img, start_button_rect.topleft)
    window.blit(leaderboard_image_scale, (x_leaderboard, y_leaderboard))
    window.blit(introduction_image_scaled, (x_intro_button, y_intro_button))

    return start_button_rect, exit_button_rect, leaderboard_button, intro_button


def check_button_event(start_button_rect, exit_button_rect):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_button_rect.collidepoint(mouse_pos):
                return "start"
            if exit_button_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()
    return None


def draw_return_button(window):
    return_img = pygame.image.load(join("assets", "Menu", "Buttons", "Back.png"))
    scaled_return_img = pygame.transform.scale(return_img, (return_img.get_width() * 6, return_img.get_height() * 6))

    return_button_x = (WIDTH - return_img.get_width()) // 2
    return_button_y = HEIGHT - return_img.get_height() - 110

    return_button_rect = pygame.Rect(return_button_x, return_button_y, scaled_return_img.get_width(), scaled_return_img.get_height())

    window.blit(scaled_return_img, (return_button_x, return_button_y))

    return return_button_rect


def draw_leaderboard_screen(window):
    try:
        leaderboard = pd.read_csv(DATA_FILE)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        leaderboard = pd.DataFrame(columns=['name', 'score', 'map'])
        leaderboard.to_csv(DATA_FILE, index=False)

    window.fill(BLACK)

    font_title = pygame.font.SysFont(FONT_LEADERBOARD[0], 70, True)
    font_board = pygame.font.SysFont(*FONT_LEADERBOARD)

    title_surface = font_title.render("LEADERBOARD", True, WHITE)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, LEADERBOARD_POS[1] - 70))
    window.blit(title_surface, title_rect.topleft)


    if leaderboard.empty:
        no_data_text = font_board.render("No Data of previous Player.", True, WHITE)
        window.blit(no_data_text, ((WIDTH - no_data_text.get_width()) // 2, HEIGHT // 2))
    else:
        header_font = pygame.font.SysFont(*FONT_LEADERBOARD)
        headers = ["Rank", "Name", "Score", "Map"]
        header_x_positions = [LEADERBOARD_POS[0], LEADERBOARD_POS[0] + 150, LEADERBOARD_POS[0] + 400,
                              LEADERBOARD_POS[0] + 550]

        for idx, header in enumerate(headers):
            header_surface = header_font.render(header, True, WHITE)
            window.blit(header_surface, (header_x_positions[idx], LEADERBOARD_POS[1] + 20))

        leaderboard = leaderboard.sort_values(by='score', ascending=False).head(7)
        max_entries = min(len(leaderboard), 7)
        for i in range(max_entries):
            entry = leaderboard.iloc[i]
            rank_text = f"{i + 1}."
            name_text = f"{entry['name']}"
            score_text = f"{entry['score']}"
            map_text = f"{entry['map']}"

            rank_surface = font_board.render(rank_text, True, WHITE)
            name_surface = font_board.render(name_text, True, WHITE)
            score_surface = font_board.render(score_text, True, WHITE)
            map_surface = font_board.render(map_text, True, WHITE)

            row_y = LEADERBOARD_POS[1] + 50 + i * 30
            window.blit(rank_surface, (header_x_positions[0], row_y))
            window.blit(name_surface, (header_x_positions[1], row_y))
            window.blit(score_surface, (header_x_positions[2], row_y))
            window.blit(map_surface, (header_x_positions[3], row_y))

    pygame.display.update()

    return_button = draw_return_button(window)
    pygame.display.flip()

    return return_button


def draw_introduction_screen(window):
    window.fill(BLACK)

    font_intro = pygame.font.SysFont("Arial", 42)
    intro_text = [
        "Welcome to Adventure Game!",
        "Rules:",
        "1. Avoid obstacles and reach the endpoint to WIN.",
        "2. Collect items for points.",
        "3. Have fun!",
        "4. You can give us 10 score if you love this. Please <3"
    ]

    for i, line in enumerate(intro_text):
        line_surface = font_intro.render(line, True, WHITE)
        line_rect = line_surface.get_rect(center=(WIDTH // 2, 150 + i * 50))
        window.blit(line_surface, line_rect.topleft)

    return_button = draw_return_button(window)
    pygame.display.flip()

    return return_button
