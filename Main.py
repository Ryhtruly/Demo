import pygame
from src.gui import draw_intro_screen, draw_leaderboard_screen, draw_introduction_screen
from src.game import main
from src.confige import WIDTH, HEIGHT, FPS
from src.music import play_background_music

def main_loop():
    pygame.init()
    pygame.font.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    play_background_music()
    clock = pygame.time.Clock()

    running = True
    in_menu = True
    in_leaderboard = False
    in_introduction = False

    while running:

        clock.tick(FPS)

        if in_menu:
            start_button_rect, exit_button_rect, leaderboard_button, intro_button = draw_intro_screen(window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if start_button_rect.collidepoint(mouse_pos):
                        print("Start button clicked!")
                        main(window)
                        in_menu = True
                    elif exit_button_rect.collidepoint(mouse_pos):
                        running = False
                    elif leaderboard_button.collidepoint(mouse_pos):
                        in_menu = False
                        in_leaderboard = True
                    elif intro_button.collidepoint(mouse_pos):
                        in_menu = False
                        in_introduction = True

        elif in_leaderboard:
            return_button = draw_leaderboard_screen(window)
            while in_leaderboard:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print("Quit event detected.")
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        print(f"Mouse clicked LeaderBoard at {mouse_pos}")
                        if return_button.collidepoint(mouse_pos):
                            in_leaderboard = False
                            in_menu = True

        elif in_introduction:
            return_button = draw_introduction_screen(window)
            while in_introduction:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if return_button.collidepoint(mouse_pos):
                            in_introduction = False
                            in_menu = True

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main_loop()