import pygame
from src.player import Player
from src.block import Block
from src.fire import Fire
from src.gui import draw_intro_screen, check_button_event
from src.Collide import handle_move
from src.confige import WIDTH, HEIGHT, FPS
from src.spriteLoader import get_background, draw


window = pygame.display.set_mode((WIDTH, HEIGHT))


def main(window):
   clock = pygame.time.Clock()
   background, bg_image = get_background("rsz_1new2.png")
   start_button_rect, exit_button_rect = draw_intro_screen(window)


   while True:
       action = check_button_event(start_button_rect, exit_button_rect)
       if action == "start":
           break




   window.fill((255, 255, 255))
   pygame.display.flip()




   block_size = 96


   player = Player(100, 100, 50, 50)


   fires = [
       Fire(block_size * 6.35, HEIGHT - block_size - 64, 16, 32),
       Fire(block_size * 8.35, HEIGHT - block_size - 64, 16, 32),
       Fire(block_size * 10.35, HEIGHT - block_size - 64, 16, 32),
       Fire(block_size * 12.35, HEIGHT - block_size - 64, 16, 32),
       Fire(block_size * 12.35, HEIGHT - block_size - 64, 16, 32),
       Fire(block_size * 14.35, HEIGHT - block_size - 64, 16, 32),
       Fire(block_size * 31.35, HEIGHT - block_size - 64, 16, 32),
   ]


   for fire in fires:
       fire.on()


   floor = [Block(i * block_size, HEIGHT - block_size, block_size)
            for i in range(-WIDTH // block_size, WIDTH * 10 // block_size)]


   objects = [*floor, *fires]


   pole_start = 2
   pole_end = 7
   for i in range(pole_start, pole_end):
       block_x = 0
       block_y = HEIGHT - block_size * i
       objects.append(Block(block_x, block_y, block_size))


   horizontal1_start = 7
   horizontail1_end = 13


   for i in range(horizontal1_start, horizontail1_end + 2, 2):
       block_x = block_size * i
       block_y = HEIGHT - block_size * 2.5
       objects.append(Block(block_x, block_y, block_size))


   horizontal2_1_start = 16
   horizontail2_1_end = 27
   for i in range(3, 10):
       for j in range(horizontal2_1_start, horizontail2_1_end + 1):
           block_x = j * block_size
           block_y = HEIGHT - block_size * i
           objects.append(Block(block_x, block_y, block_size))


   objects.append(Block(block_size * 28, HEIGHT - block_size * 3, block_size))


   pole2_start = 2
   pole2_end = 8
   for i in range(pole2_start, pole2_end):
       block_x = block_size * 30
       block_y = HEIGHT - block_size * i
       objects.append(Block(block_x, block_y, block_size))


   objects.append(Block(block_size * 29, HEIGHT - block_size * 4.8, block_size))
   objects.append(Block(block_size * 28, HEIGHT - block_size * 7, block_size))
   objects.append(Block(block_size * 5, HEIGHT - block_size * 2, block_size))


   collums = [7, 6, 5, 4, 3, 2]
   for i in range(32, 37 + 1):
       height = collums[i - 32]
       for j in range(2, height + 1):
           block_x = block_size * i
           block_y = HEIGHT - block_size * j
           objects.append(Block(block_x, block_y, block_size))


   horizontal3_1_start = 39
   horizontal3_1_end = 46
   for i in range(horizontal3_1_start, horizontal3_1_end + 1):
       block_x = block_size * i
       block_y = HEIGHT - block_size * 3
       objects.append(Block(block_x, block_y, block_size))
       block_y2 = HEIGHT - block_size * 5
       objects.append(Block(block_x, block_y2, block_size))


   horizontal3_2_start = 49
   horizontal3_2_end = 56
   for i in range(horizontal3_2_start, horizontal3_2_end + 1):
       block_x = block_size * i
       block_y = HEIGHT - block_size * 4
       objects.append(Block(block_x, block_y, block_size))
       block_y2 = HEIGHT - block_size * 6.5
       objects.append(Block(block_x, block_y2, block_size))


   offset_x = 0
   scroll_area_width = 200


   run = True
   while run:
       clock.tick(FPS)
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False
               break
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE and player.jump_count < 2:
                   player.jump()


       player.loop(FPS)
       handle_move(player, objects)


       for fire in fires:
           fire.loop()


       draw(window, background, bg_image, player, objects, offset_x)


       if (player.rect.right - offset_x >= WIDTH - scroll_area_width and player.x_vel > 0) or (
               (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
           offset_x += player.x_vel


   pygame.quit()




if __name__ == "__main__":
   main(window)
