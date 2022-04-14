from pygame import *
from random import *
from time import time as timer

class GameSprite (sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, size_x, size_y,         player_speed):
        super().__init__()
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset (self):
        window.blit(self.image,(self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update_l(self): #Левая
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.y < width - 50:
            self.rect.x += self.speed
    
  def update_r(self): #правая
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y < width - 50:
            self.rect.x += self.speed
    

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption("Пинг-понг")
back =(200, 255, 255)
window.fiil(back)
game = True
finish = False
FPS = 60
count = 0
font.init()
font1 = font.SysFont("Arial",36)
lose1= font1.render('Игрок 1 проиграл', True, (255, 255, 255))
lose2 = font1.render('Игрок 1 проиграл', True, (255, 0 ,0))