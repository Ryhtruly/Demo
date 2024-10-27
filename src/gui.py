import pygame
import sys
from os.path import join
from src.confige import WIDTH, HEIGHT, BLACK, DATA_FILE, FONT_LEADERBOARD, LEADERBOARD_POS, WHITE
import pandas as pd

start_img = pygame.image.load(join("assets", "Other", "start_btn.png"))
exit_img = pygame.image.load(join("assets", "Other", "exit_btn.png"))
leaderboard_image = pygame.image.load(join("assets", "Menu", "Buttons", "LeaderBoard.png"))


def x_cor_center(window_width, element_width):
    return (window_width - element_width) // 2


def draw_intro_screen(window):
    intro_bg_image = pygame.image.load(join("assets", "Background", "rsz_new3.png"))
    intro_bg_width, intro_bg_height = intro_bg_image.get_size()

    for x in range(0, WIDTH, intro_bg_width):
        for y in range(0, HEIGHT, intro_bg_height):
            window.blit(intro_bg_image, (x, y))

    font = pygame.font.SysFont(None, 60)
    title_text = font.render('WELCOME TO THE GAME!', True, (255, 255, 255))

    start_img_width, start_img_height = start_img.get_size()

    start_button_x = (WIDTH - start_img_width) // 2
    start_button_y = (HEIGHT - start_img_height) // 2
    start_button_rect = pygame.Rect(start_button_x, start_button_y, start_img_width, start_img_height)

    window.blit(title_text, ((WIDTH - title_text.get_width()) // 2, HEIGHT // 4))

    exit_img_width, exit_img_height = exit_img.get_size()
    exit_button_x = (WIDTH - exit_img_width) // 2
    exit_button_y = start_button_y + start_img_height + 40
    exit_button_rect = pygame.Rect(exit_button_x, exit_button_y, exit_img_width, exit_img_height)

    width_board, height_board = leaderboard_image.get_size()
    width_board *= 3
    height_board *= 3
    leaderboard_image_scale = pygame.transform.scale(leaderboard_image, (width_board, height_board))
    x_leaderboard = x_cor_center(WIDTH, width_board)
    y_leaderboard = exit_button_y + exit_img_height + 50
    leaderboard_button = pygame.Rect(x_leaderboard, y_leaderboard, width_board, height_board)

    window.blit(exit_img, exit_button_rect.topleft)
    window.blit(start_img, start_button_rect.topleft)
    window.blit(leaderboard_image_scale, (x_leaderboard, y_leaderboard))

    return start_button_rect, exit_button_rect, leaderboard_button


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


def draw_return_button(window, return_img, window_width, window_height):
    return_button_x = (window_width - return_img.get_width()) // 2
    return_button_y = window_height - return_img.get_height() - 50
    return_button_rect = pygame.Rect(return_button_x, return_button_y, return_img.get_width(), return_img.get_height())

    window.blit(return_img, (return_button_x, return_button_y))

    return return_button_rect


def draw_leaderboard_screen(window):
    try:
        leaderboard = pd.read_csv(DATA_FILE)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        leaderboard = pd.DataFrame(columns=['name', 'score', 'map'])

    window.fill(BLACK)
    return_image = pygame.image.load(join("assets", "Menu", "Buttons", "Back.png"))
    font_board = pygame.font.SysFont(*FONT_LEADERBOARD)
    leaderboard = leaderboard.sort_values(by='score', ascending=False)
    title_surface = font_board.render("Leaderboard", True, WHITE)
    window.blit(title_surface, (LEADERBOARD_POS[0], LEADERBOARD_POS[1] - 50))

    if leaderboard.empty:
        no_data_text = font_board.render("No Data of previous Player.", True, WHITE)
        window.blit(no_data_text, ((WIDTH - no_data_text.get_width()) // 2, HEIGHT // 2))
    else:
        max_entries = min(len(leaderboard), 7)
        for i in range(max_entries):
            entry = leaderboard.iloc[i]
            text = f"{i + 1}. {entry['name']} - Score: {entry['score']} - Map: {entry['map']}"
            text_surface = font_board.render(text, True, WHITE)
            window.blit(text_surface, (LEADERBOARD_POS[0], LEADERBOARD_POS[1] + i * 30))

    pygame.display.update()

    return_button = draw_return_button(window, return_image, WIDTH, HEIGHT)

    pygame.display.flip()

    return return_button


def draw_introduction(window):
    window.fill(BLACK)

