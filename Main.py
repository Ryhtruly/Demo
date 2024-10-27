import pygame
from src.gui import draw_intro_screen, check_button_event, draw_leaderboard_screen
from src.game import main
from src.confige import WIDTH, HEIGHT, FPS
from src.music import play_background_music

pygame.init()

def main_loop():
    pygame.init()
    pygame.font.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    play_background_music()
    clock = pygame.time.Clock()

    running = True 
    in_menu = True
    in_leaderboard = False

    while running:

        clock.tick(FPS)

        if in_menu:
            result = draw_intro_screen(window)
            print(result)
            start_button_rect, exit_button_rect, leaderboard_button = draw_intro_screen(window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if start_button_rect.collidepoint(mouse_pos):
                        print("Start button clicked!")
                        in_menu = False
                        main(window)
                    elif exit_button_rect.collidepoint(mouse_pos):
                        running = False
                    elif leaderboard_button.collidepoint(mouse_pos):
                        in_menu = False
                        in_leaderboard = True

        elif in_leaderboard:
            return_button = draw_leaderboard_screen(window)
            while in_leaderboard:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print("Quit event detected.")
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        print(f"Mouse clicked at {mouse_pos}")
                        if return_button.collidepoint(mouse_pos):
                            in_leaderboard = False
                            in_menu = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main_loop()
