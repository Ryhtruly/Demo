import pygame
from src.confige import PLAYER_VEL

def handle_vertical_collision(player, objects, dy):
   collided_objects = []
   for obj in objects:
       if pygame.sprite.collide_mask(player, obj):
           if dy > 0:
               player.rect.bottom = obj.rect.top
               player.landed()
               player.y_vel = 0
           elif dy < 0:
               player.rect.top = obj.rect.bottom
               player.hit_head()
               player.y_vel = 0


           collided_objects.append(obj)


   return collided_objects


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
   collide_left = collide(player, objects, -PLAYER_VEL )
   collide_right = collide(player, objects, PLAYER_VEL )


   if keys[pygame.K_LEFT] and not collide_left:
       player.move_left(PLAYER_VEL)
   if keys[pygame.K_RIGHT] and not collide_right:
       player.move_right(PLAYER_VEL)


   vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
   to_check = [collide_left, collide_right, *vertical_collide]


   for obj in to_check:
       if obj and obj.name == "fire":
           player.make_hit()

       if obj and obj.name == "food":
           if obj.check_collision(player):
               print("Food collision detected!")
               scoreboard.increase_score()
               to_check.remove(obj)
           else:
               print("Food collision not detected!")
