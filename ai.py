import pygame
import time
import math
import sys
import random
class pop(pygame.sprite.Sprite):
    #constructor, pass in x and y position of the pop
    def __init__(self, pos, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill([0,0,100])
        self.rect = int(pos[0]),int(pos[1])

        self.speed = speed
    def draw(self, screen):
            screen.blit(self.image, self.rect)

    def move(self,screen):
        #inspired by https://www.pygame.org/docs/tut/tom_games4.html?highlight=vector
        angle = math.pi*2*random.random()
        pos = self.rect
        dx = + self.speed *math.cos(angle)
        dy = self.speed *math.sin(angle)
        if dx + pos[0] < 0 or dx+ pos[0]>470:
            x = pos[0] - dx
        else:
            x = pos[0] + dx

        if dy + pos[1] < 0 or dy+ pos[1]>350:
            y = pos[1] - dy
        else:
            y = pos[1] + dy
        self.move_to = x,y
        self.rect = self.move_to

    def update(self,screen):
        self.move(screen)

class food(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill([100,0,0])
        self.rect = int(pos[0]),int(pos[1])

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def create_village(population, speed):
    village = pygame.sprite.Group()
    for i in range(population):
        village.add(pop([random.uniform(0,480),random.uniform(0,360)], speed ))
    return village

def create_stack(amount):
    stack = pygame.sprite.Group()
    for i in range(amount):
        stack.add(food([random.uniform(0,480),random.uniform(0,360)]))
    return stack


size = 10
green = 0,100,0
size = width, length = 480,360
screen = pygame.display.set_mode(size)
background = screen
screen.fill(green)
#creating a first inhabitant
villager = pop([random.uniform(0,470),random.uniform(0,350)], 3)

village = create_village(10,5)
fruit_1 = food([120,150])
stack = create_stack(10)
pygame.init()
pygame.display.flip()
QUIT = pygame.QUIT
KEYDOWN = pygame.KEYDOWN
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(green)
    village.update(screen)
    fruit_1.draw(screen)
    village.draw(screen)
    stack.draw(screen)
    pygame.display.update()
    pygame.time.delay(100)
