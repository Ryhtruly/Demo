import pygame
from src.spriteLoader import load_sprite_sheets
from src.confige import WIDTH, HEIGHT


class Player(pygame.sprite.Sprite):
   COLOR = ( 250, 0, 0)
   GRAVITY = 1
   SPRITES = load_sprite_sheets("MainCharacters","VirtualGuy", 32, 32, True)
   ANIMATION_DELAY = 3


   def __init__(self, x , y , width, height):
       super().__init__()


       self.rect = pygame.Rect(x, y , width, height)
       self.x_vel = 0
       self.y_vel = 0
       self.mask = None
       self.direction = "left"
       self.animation_count = 0
       self.fall_count = 0
       self.jump_count = 0
       self.hit = False
       self.hit_count = 0
       self.is_dead = False


       self.SPRITES = load_sprite_sheets("MainCharacters", "VirtualGuy", 32, 32, True)
       self.sprite = self.SPRITES["idle_" + self.direction][0]


   def jump(self):
       self.y_vel = -self.GRAVITY * 9
       self.animation_count = 0
       self.jump_count += 1
       if self.jump_count == 1:
           self.fall_count = 0


   def move(self, dx, dy):
       self.rect.x += dx
       self.rect.y += dy


   def make_hit(self):
       if not self.is_dead:
           self.hit = True
           self.hit_count += 1
           if self.hit_count >= 2:
               self.is_dead = True


   def move_left(self, vel):
       self.x_vel = -vel
       if self.direction != "left":
           self.direction = "left"
           self.animation_count = 0


   def move_right(self, vel):
       self.x_vel = vel
       if self.direction != "right":
           self.direction = "right"
           self.animation_count = 0


   def loop(self, fps):
       if not self.is_dead:
             self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
             self.move(self.x_vel, self.y_vel)
             if self.hit:
                   self.hit_count += 1
             if self.hit_count > fps * 2:
                  self.hit = False
                  self.hit_count = 0


       self.fall_count += 1
       self.update_sprite()


   def landed(self):
       self.fall_count = 0
       self.y_vel = 0
       self.jump_count = 0


   def hit_head(self):
       self.count = 0
       self.y_vel *= -1


   def update_sprite(self):
       sprite_sheet = "idle"
       if self.hit:
           sprite_sheet = "hit"
       elif self.y_vel < 0:
           if self.jump_count == 1:
               sprite_sheet = "jump"
           elif self.jump_count == 2:
               sprite_sheet = "double_jump"
       elif self.y_vel > self.GRAVITY * 2:
           sprite_sheet = "fall"
       elif self.x_vel != 0:
           sprite_sheet = "run"


       sprite_sheet_name = sprite_sheet + "_" + self.direction
       sprites = self.SPRITES.get(sprite_sheet_name)
       if sprites:
           sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
           self.sprite = sprites[sprite_index]
           self.animation_count += 1
           self.update()


   def update(self):
       if self.sprite:
           self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
           self.mask = pygame.mask.from_surface(self.sprite)


   def draw(self, win, offset_x):
       if self.sprite:
           win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))
       if self.is_dead:
           font = pygame.font.SysFont('Pixeled', 64)
           text = font.render('DEFEAT', True, (255, 255, 255))
           text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
           win.blit(text, text_rect)