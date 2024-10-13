import pygame
from src.gui import draw_intro_screen, check_button_event
from src.game import main
from src.confige import WIDTH, HEIGHT


def main_loop():
    pygame.init()
    pygame.font.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    in_menu = True

    while running:
        clock.tick(60)

        if in_menu:
            start_button_rect, exit_button_rect = draw_intro_screen(window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if start_button_rect.collidepoint(mouse_pos):
                        in_menu = False
                        main(window)
                    elif exit_button_rect.collidepoint(mouse_pos):
                        running = False
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main_loop()
