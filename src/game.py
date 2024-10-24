import pygame
import sys
import os
from src.player import Player
from src.block import Block
from src.fire import Fire
from src.gui import draw_intro_screen, check_button_event
from src.collide import handle_move
from src.confige import WIDTH, HEIGHT, FPS
from src.spriteLoader import get_background, draw
from src.scoreboard import ScoreBoard, get_player_name
from src.fan import Fan, FanRow
from src.saw import Saw_Row, Saw_Collum, Saw
from os.path import join
from src.spriteLoader import get_background
from src.food import Banana, Apple

# food.loop()
#
#        draw(window, background, bg_image, player, objects, offset_x, food, score_board)

window = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))


def load_background(name):
    path = join("assets", "Background", name)
    image = pygame.image.load(path)
    _, _, width, height = image.get_rect()
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    return image


def load_and_scale(path, size=(100, 100)):

    try:
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size)
    except pygame.error as e:
        print(f"Không thể tải hình ảnh: {path}")
        print(f"Lỗi: {e}")
        return pygame.Surface(size)


def load_character_images():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    base_path = os.path.join(project_root, 'assets', 'MainCharacters')

    characters = {
        'NinjaFrog': os.path.join('NinjaFrog', 'fall.png'),
        'PinkMan': os.path.join('PinkMan', 'fall.png'),
        'VirtualGuy': os.path.join('VirtualGuy', 'fall.png'),
        'MaskDude': os.path.join('MaskDude', 'fall.png')
    }

    images = []

    for character, rel_path in characters.items():
        full_path = os.path.join(base_path, rel_path)
        print(f"Attempting to load: {full_path}")
        if os.path.exists(full_path):
            images.append(load_and_scale(full_path))
        else:
            print(f"File không tồn tại: {full_path}")

    return images


def character_selection_screen(window, character_images):
    characters = ["NinjaFrog", "PinkMan", "VirtualGuy", "MaskDude"]
    selected = 0
    font = pygame.font.Font(None, 36)
    background, bg_image = get_background("rsz_new3.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected = (selected - 1) % len(characters)
                elif event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % len(characters)
                elif event.key == pygame.K_RETURN:
                    return characters[selected]
            break

        for tile in background:
            window.blit(bg_image, tile)

        for i, (character, image) in enumerate(zip(characters, character_images)):
            x = WIDTH // 2 + (i - 1.5) * 200
            y = HEIGHT // 2 - 50

            window.blit(image, (x - image.get_width() // 2, y - image.get_height() // 2))

            color = (255, 0, 0) if i == selected else (255, 255, 255)
            text = font.render(character, True, color)
            window.blit(text, (x - text.get_width() // 2, y + image.get_height() // 2 + 10))

            if i == selected:
                pygame.draw.rect(window, (255, 0, 0), (x - image.get_width() // 2 - 5, y - image.get_height() // 2 - 5, image.get_width() + 10, image.get_height() + 10), 3)

        pygame.display.flip()


def main(window):
   clock = pygame.time.Clock()
   background, bg_image = get_background("rsz_1new2.png")
   start_button_rect, exit_button_rect, leaderboard_button = draw_intro_screen(window)

   while True:
       action = check_button_event(start_button_rect, exit_button_rect)
       if action == "start":
            break
       elif action == "exit":
            pygame.quit()
            return

   player_name = get_player_name(window, WIDTH, HEIGHT)
   map_level = 1
   if player_name is None:
       return
   score_board = ScoreBoard(player_name, map_level)

   character_images = load_character_images()

   selected_character = character_selection_screen(window, character_images)

   font = pygame.font.SysFont(None, 44)

   message = f"Select Character:  {selected_character}"
   text = font.render(message, True, (255, 255, 255))
   window.fill((0, 0, 0))
   window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
   pygame.display.flip()
   pygame.time.wait(2000)  # Wait for 2 seconds


   block_size = 96

   player = Player(100, 100, 50, 50, selected_character)


   fires = [
       Fire(block_size * 6.35, HEIGHT - block_size - 64, 16, 32),
       Fire(block_size * 8.35, HEIGHT - block_size - 64, 16, 32),
       Fire(block_size * 10.35, HEIGHT - block_size - 64, 16, 32),
       Fire(block_size * 12.35, HEIGHT - block_size - 64, 16, 32),
       Fire(block_size * 12.35, HEIGHT - block_size - 64, 16, 32),
       Fire(block_size * 14.35, HEIGHT - block_size - 64, 16, 32),
       Fire(block_size * 31.35, HEIGHT - block_size - 64, 16, 32),
   ]
   fan = Fan(block_size * 4, HEIGHT - block_size - 64, 24, 8)
   saw = Saw(block_size * 6, HEIGHT - block_size * 4, 38, 38)
   saw_row = Saw_Row(block_size * 4, HEIGHT - block_size * 2.5, 38, 38)
   saw_collum = Saw_Collum(block_size * 8, HEIGHT - block_size * 2.5, 38, 38)
   banana = [Banana(block_size * 2, HEIGHT - block_size - 64), Banana(block_size * 50, HEIGHT - block_size - 64)]
   apple = [Apple(block_size * 3, HEIGHT - block_size - 64), Apple(block_size * 55, HEIGHT - block_size - 64)]
   fan_row = FanRow(block_size * 2, HEIGHT  - block_size * 3, 24 , 8)


   for fire in fires:
       fire.on()


   floor = [Block(i * block_size, HEIGHT - block_size, block_size)
            for i in range(-WIDTH // block_size, WIDTH * 10 // block_size)]


   objects = [*floor, *fires, fan, saw, saw_row, saw_collum, *banana, *apple, fan_row]
   fan.on()
   saw.on()
   saw_row.on()
   saw_collum.on()
   fan_row.on()

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
       handle_move(player, objects, score_board)
       saw.loop()
       saw_row.loop()
       saw_collum.loop()
       for fire in fires:
           fire.loop()
       fan.loop()
       for bnn in banana:
          bnn.loop()
       for ap in apple:
          ap.loop()
       fan_row.loop()


       draw(window, background, bg_image, player, objects, offset_x, score_board)


       if (player.rect.right - offset_x >= WIDTH - scroll_area_width and player.x_vel > 0) or (
               (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
           offset_x += player.x_vel

   pygame.quit()

if __name__ == "__main__":
   main(window)