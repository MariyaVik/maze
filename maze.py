#создай игру "Лабиринт"!
from pygame import *


# классы
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (sprite_width, sprite_height))
        
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        
        self.speed = sprite_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# константы
win_height = 500
win_width = 700
sprite_height = 80
sprite_width = 80

clock = time.Clock()
FPS = 60

# картинки
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
player_image = 'hero.png'
enemy_image = 'cyborg.png'
gold_image = 'treasure.png'

# звуки
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()


# спрайты
player = GameSprite(player_image, 50, 50, 5)
enemy = GameSprite(enemy_image, 600, 200, 5)
gold = GameSprite(gold_image, 600, 400, 0)


# окно
window = display.set_mode((win_width, win_height))
display.set_caption("Лабиринт")

# игровой цикл
run = True

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(background,(0, 0))
    player.reset()
    enemy.reset()
    gold.reset()

    display.update()
    clock.tick(FPS)
















# class GameSprite(sprite.Sprite):
#     def __init__(self, name_image, spr_height, spr_width, spr_x, spr_y, spr_speed):
#         super().__init__()
#         self.image = transform.scale(image.load(name_image), (spr_width,spr_height))
#         self.speed = spr_speed

#         self.rect = self.image.get_rect()
#         self.rect.x = spr_x
#         self.rect.y = spr_y

#     def reset(self):
#         window.blit(self.image,(self.rect.x, self.rect.y))

# class Player(GameSprite):
#    def update(self):
#        keys = key.get_pressed()
#        if keys[K_LEFT] and self.rect.x > 5:
#            self.rect.x -= self.speed
#        if keys[K_RIGHT] and self.rect.x < win_width - 80:
#            self.rect.x += self.speed
#        if keys[K_UP] and self.rect.y > 5:
#            self.rect.y -= self.speed
#        if keys[K_DOWN] and self.rect.y < win_height - 80:
#            self.rect.y += self.speed
 
# class Enemy(GameSprite):
#    direction = "left"
#    def update(self):
#        if self.rect.x <= 470:
#            self.direction = "right"
#        if self.rect.x >= win_width - 85:
#            self.direction = "left"
 
#        if self.direction == "left":
#            self.rect.x -= self.speed
#        else:
#            self.rect.x += self.speed

# class Wall(sprite.Sprite):
#     def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
#         super().__init__()
#         self.color_1 = color_1
#         self.color_2 = color_2
#         self.color_3 = color_3
#         self.width = wall_width
#         self.height = wall_height

#         self.image = Surface((self.width, self.height))
#         self.image.fill((self.color_1, self.color_2, self.color_3))

#         self.rect = self.image.get_rect()
#         self.rect.x = wall_x
#         self.rect.y = wall_y

#     def paint(self):
#         window.blit(self.image,(self.rect.x, self.rect.y))


# win_width = 700
# win_height = 500
# window = display.set_mode((win_width, win_height))
# display.set_caption("Лабиринт")
# background = transform.scale(image.load("background.jpg"), (win_width, win_height))

# player = Player('hero.png', 100, 100, 250, 300, 5)
# enemy = Enemy('cyborg.png', 100, 100, 400, 300, 5)
# gold = GameSprite('treasure.png', 100, 100, 250, 100, 0)

# w1 = Wall(136, 245, 217, 200, 250, 10, 300)
# w2 = Wall(136, 245, 217, 200, 250, 300, 10)

# clock = time.Clock()
# FPS = 60

# mixer.init()
# win_sound = mixer.Sound("money.ogg")

# font.init()
# font = font.Font(None, 70)
# win_text = font.render("YOU WIN", True, (0, 255, 0))

# game = True
# finish = False

# while game:

#     for e in event.get():
#         if e.type == QUIT:
#             game = False

#     if not finish:
#         window.blit(background,(0, 0))
#         player.update()
#         enemy.update()
        
#         player.reset()
#         enemy.reset()
#         gold.reset()

#         w1.paint()
#         w2.paint()

#         if sprite.collide_rect(player, gold):
#             finish = True
#             window.blit(win_text, (200, 200))
#             win_sound.play()

#         if sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2):
#             finish = True

#     display.update()
#     clock.tick(FPS)






















# # класс-родитель для спрайтов 
# class GameSprite(sprite.Sprite):
#     #конструктор класса
#     def __init__(self, player_image, player_x, player_y, player_speed):
#         super().__init__()
 
#         # каждый спрайт должен хранить свойство image - изображение
#         self.image = transform.scale(image.load(player_image), (55, 55))
#         self.speed = player_speed
 
#         # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y

#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))

# #класс-наследник для спрайта-игрока (управляется стрелками)
# class Player(GameSprite):
#     def update(self):
#         keys = key.get_pressed()
#         if keys[K_LEFT] and self.rect.x > 5:
#             self.rect.x -= self.speed
#         if keys[K_RIGHT] and self.rect.x < win_width - 80:
#             self.rect.x += self.speed
#         if keys[K_UP] and self.rect.y > 5:
#             self.rect.y -= self.speed
#         if keys[K_DOWN] and self.rect.y < win_height - 80:
#             self.rect.y += self.speed

# #класс-наследник для спрайта-врага (перемещается сам)
# class Enemy(GameSprite):
#     side = "left"
#     def update(self):
#         if self.rect.x <= 470:
#             self.side = "right"
#         if self.rect.x >= win_width - 85:
#             self.side = "left"
#         if self.side == "left":
#             self.rect.x -= self.speed
#         else:
#             self.rect.x += self.speed

# #класс для спрайтов-препятствий
# class Wall(sprite.Sprite):
#     def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
#         super().__init__()
#         self.color_1 = color_1
#         self.color_2 = color_2
#         self.color_3 = color_3
#         self.width = wall_width
#         self.height = wall_height
 
#         # картинка стены - прямоугольник нужных размеров и цвета
#         self.image = Surface([self.width, self.height])
#         self.image.fill((color_1, color_2, color_3))
 
#         # каждый спрайт должен хранить свойство rect - прямоугольник
#         self.rect = self.image.get_rect()
#         self.rect.x = wall_x
#         self.rect.y = wall_y
 
#     def draw_wall(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))
#         #draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))

# '''Описание игры'''

# #Игровая сцена:
# win_width = 700
# win_height = 500
# window = display.set_mode((win_width, win_height))
# display.set_caption("Maze")
# background = transform.scale(image.load("background.jpg"), (win_width, win_height))

# w1 = Wall(154, 205, 50, 100, 20 , 450, 10)
# w2 = Wall(154, 205, 50, 100, 480, 350, 10)
# w3 = Wall(154, 205, 50, 100, 20 , 10, 380)
# w4 = Wall(154, 205, 50, 200, 130, 10, 350)
# w5 = Wall(154, 205, 50, 450, 130, 10, 360)
# w6 = Wall(154, 205, 50, 300, 20, 10, 350)
# w7 = Wall(154, 205, 50, 390, 120, 130, 10)

# #Персонажи игры:
# packman = Player('hero.png', 5, win_height - 80, 4)
# monster = Enemy('cyborg.png', win_width - 80, 280, 2)
# final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

# game = True
# finish = False
# clock = time.Clock()
# FPS = 60

# font.init()
# font = font.Font(None, 70)
# win = font.render('YOU WIN!', True, (255, 215, 0))
# lose = font.render('YOU LOSE!', True, (180, 0, 0))

# #музыка
# mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play()

# money = mixer.Sound('money.ogg')
# kick = mixer.Sound('kick.ogg')

# while game:
#     for e in event.get():
#         if e.type == QUIT:
#             game = False

#     if finish != True:
#         window.blit(background,(0, 0))
#         packman.update()
#         monster.update()
        
#         packman.reset()
#         monster.reset()
#         final.reset() 
        
#         w1.draw_wall()
#         w2.draw_wall()
#         w3.draw_wall()
#         w4.draw_wall()
#         w5.draw_wall()
#         w6.draw_wall()
#         w7.draw_wall()

#         #Ситуация "Проигрыш"
#         # if sprite.collide_rect(packman, monster) or sprite.collide_rect(packman, w1) or sprite.collide_rect(packman, w2)or sprite.collide_rect(packman, w2)or sprite.collide_rect(packman, w3)or sprite.collide_rect(packman, w4)or sprite.collide_rect(packman, w5)or sprite.collide_rect(packman, w6)or sprite.collide_rect(packman, w7):
#         #     finish = True
#         #     window.blit(lose, (200, 200))
#         #     kick.play()

#         #Ситуация "Выигрыш"
#         if sprite.collide_rect(packman, final):
#             finish = True
#             window.blit(win, (200, 200))
#             money.play()


#         #-------------------------------------
#         #Ситуация "Проигрыш" и простой рестарт
#         if sprite.collide_rect(packman, monster) :
#             finish = True
#             window.blit(lose, (200, 200))
#             kick.play()

#         if sprite.collide_rect(packman, w1) or sprite.collide_rect(packman, w2)or sprite.collide_rect(packman, w2)or sprite.collide_rect(packman, w3)or sprite.collide_rect(packman, w4)or sprite.collide_rect(packman, w5)or sprite.collide_rect(packman, w6)or sprite.collide_rect(packman, w7):
#             packman.rect.x = 5
#             packman.rect.y = win_height - 80
#         #-------------------------------------


#     display.update()
#     clock.tick(FPS)