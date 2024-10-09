import pygame
import sys
from os.path import join
from src.confige import WIDTH, HEIGHT


start_img = pygame.image.load(join("assets", "Other", "start_btn.png"))
exit_img = pygame.image.load(join("assets", "Other", "exit_btn.png"))


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


   window.blit(exit_img, exit_button_rect.topleft)
   window.blit(start_img, start_button_rect.topleft)


   return start_button_rect, exit_button_rect


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

