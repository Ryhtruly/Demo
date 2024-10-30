import pygame
import sys
from src.confige import PLAYER_VEL, WHITE, GREY, BLACK
from src.fire import Fire
from src.saw import Saw, Saw_Collum, Saw_Row, Saw_Collum2, Saw_Row2, Saw_Row_N
from src.fan import FanRow
from src.food import Food
from src.block import Block, Block2
from src.end_of_map import LastPoint


def handle_vertical_collision(player, objects, dy, scoreboard):
    collided_objects = []
    to_remove = []
    collision_food_vertical = False
    check_list = []

    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if isinstance(obj, Food):
                scoreboard.increase_score()
                to_remove.append(obj)
                collision_food_vertical = True
                break
            if dy > 0:

                exist_above_obj = False

                y_cor_to_check = obj.rect.y + 96
                if isinstance(obj, Block) or isinstance(obj, Block2):
                    check_list.append(obj)

                for check_block in check_list:
                    if abs(check_block.rect.y - y_cor_to_check) <= 50:
                        # print(f"distance to land: {check_block.rect.y - y_cor_to_check}")
                        exist_above_obj = True
                        break

                if not exist_above_obj:
                    player.rect.bottom = obj.rect.top
                    print(f"landed, x: {player.rect.x}, y: {player.rect.y}")
                    player.landed()
                    if isinstance(obj, FanRow):
                        if obj.moving_right:
                            player.rect.x += obj.MOVE_SPEED
                        else:
                            player.rect.x -= obj.MOVE_SPEED
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()
                player.y_vel = 0
            collided_objects.append(obj)

    for obj in to_remove:
        objects.remove(obj)

    return collided_objects, collision_food_vertical


def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collided_object = None

    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break

    player.move(-dx, 0)
    player.update()
    return collided_object


def handle_move(player, objects, scoreboard):
   keys = pygame.key.get_pressed()


   player.x_vel = 0
   collide_left = collide(player, objects, -PLAYER_VEL)
   collide_right = collide(player, objects, PLAYER_VEL)


   if keys[pygame.K_LEFT] and not collide_left:
       player.move_left(PLAYER_VEL)
       player.is_landed = False
   if keys[pygame.K_RIGHT] and not collide_right:
       player.move_right(PLAYER_VEL)
       player.is_landed = False


   vertical_collide, collision_food_vertical = handle_vertical_collision(player, objects, player.y_vel, scoreboard)
   to_check = {collide_left, collide_right, *vertical_collide}

   for obj in to_check:

       if isinstance(obj, (Fire, Saw, Saw_Collum, Saw_Row, Saw_Collum2, Saw_Row2, Saw_Row_N)):
           player.make_hit()

       if not collision_food_vertical and isinstance(obj, Food):
           scoreboard.increase_score()
           objects.remove(obj)
           break

       if isinstance(obj, LastPoint):
           show_victory_screen()
           return True

   return False


def show_victory_screen():
    screen = pygame.display.get_surface()
    font = pygame.font.Font(None, 54)

    outline_positions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    for pos in outline_positions:
        outline_text = font.render("Victory. You are great Player. Click to back to the menu.", True, BLACK)
        outline_rect = outline_text.get_rect(
            center=(screen.get_width() // 2 + pos[0], screen.get_height() // 2 + pos[1]))
        screen.blit(outline_text, outline_rect)

    shadow_text = font.render("Victory. You are great Player. Click to back to the menu.", True, GREY)
    shadow_rect = shadow_text.get_rect(center=(screen.get_width() // 2 + 2, screen.get_height() // 2 + 2))
    screen.blit(shadow_text, shadow_rect)

    main_text = font.render("Victory. You are great Player. Click to back to the menu.", True, WHITE)
    main_text_rect = main_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(main_text, main_text_rect)

    pygame.display.flip()


    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False