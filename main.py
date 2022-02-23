import pygame
import requests
from PIL import Image

pygame.init()

icon = requests.get('https://d.radikal.ru/d30/2202/2a/dedac0c03d82.png', stream = True).raw
img_icon = Image.open(icon)
img_icon.save('icon.png')

pygame.display.set_mode((800,400))
pygame.display.set_caption("RPG Game")
pygame.display.set_icon(pygame.image.load('icon.png'))

clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            exit()

    clock.tick(FPS)

class Personag(object):
    def __init__(self,hp,damage,name):
        self.hp = hp
        self.damage = damage
        self.name = name
class Gamer(Personag):
    def __init__(self,exp,hp,damage,name):
        self.exp = exp
        super().__init__(hp,damage,name)
        def ataka (self,monster):
            monster.hp -= self.damage
            if monster.hp <= 0:
                print(monster.name,"повержен + 10 опыто")
                self.exp += 10
            else:
                print(self.name,"нанёс удар: %s" %self.damage )
                print(monster.name,"теперь имеет " ,monster.hp, "здоровьё")

#class Monster(Personag):
#Jora = Gamer(0,10,4,"жоронимо")
