import pygame
import time
import math
import sys
import random
class pop(pygame.sprite.Sprite):
    #constructor, pass in x and y as position of the pop, and speed[int] for defining speed
    def __init__(self, pos, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill([0,0,100])
        self.rect = pygame.Rect(int(pos[0]),int(pos[1]),10,10)
        self.radius = 100
        self.speed = speed
        self.belly = 0
    def draw(self, screen):
            screen.blit(self.image, self.rect)

    def move(self, angle = None):
        #inspired by https://www.pygame.org/docs/tut/tom_games4.html?highlight=vector
        if angle == None:
            angle = math.pi*2*random.random()
        pos = self.rect
        dx = self.speed *math.sin(angle)
        dy = self.speed *math.cos(angle)
        if dx + pos[0] < 0 or dx+ pos[0]>470:
            x = pos[0] - dx
        else:
            x = pos[0] + dx

        if dy + pos[1] < 0 or dy+ pos[1]>350:
            y = pos[1] - dy
        else:
            y = pos[1] + dy
        self.move_to = x,y
        self.rect.left = int(self.move_to[0])
        self.rect.top = int(self.move_to[1])
    def go_to(self, other):
        xy_self = self.rect
        xy_other = other.rect
        tan = xy_other[0]-xy_self[0],xy_other[1]-xy_self[1]
        angle = math.atan2(tan[0],tan[1])
        self.move(angle)

    def update(self):
        self.move()

class food(pygame.sprite.Sprite):
    #class for food objects, with size(rect) to enable rectangle collision detection, and radius to enable circle collision detection
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill([100,0,0])
        self.rect = pygame.Rect(int(pos[0]),int(pos[1]),10,10)
        self.radius = 5
    def draw(self, screen):
        screen.blit(self.image, self.rect)

#skoro odnosi się to do dwóch klas umieściłem to poza klasami food i pop. Wzrok pozwala obiektom pop wykryć obiekty food i skierować się w stronę najbliższego.
#po zjedzeniu całego jedzenia pop będzie poruszał się losowo(obecnie występuje dryf w stronę lewego górnego rogu, przypuszczam że z powodu zamieniania z float na int przy pop.move())
def sight(self, other):
    sighted = pygame.sprite.groupcollide(self, other, False,False, collided = pygame.sprite.collide_circle)
    population = self.sprites()
    for pops in population:
        if pops in sighted:
            dist = list()
            point = list()
            for yumyum in sighted[pops]:
                distAngle = dist_angle(pops,yumyum)
                dist.append(distAngle[0])
                point.append(yumyum)

            for j in range(len(dist)):
                if min(dist) ==dist[j]:
                    pops.go_to(point[j])
        else:
            pops.move()
#metoda opodwiadająca za wykrywanie kolizji i zjadanie jedzenia

def eat(self, other):
    ate =  pygame.sprite.groupcollide(self, other, False,True)
    for lucky in ate:
        lucky.belly = lucky.belly + len(ate[lucky])


#Funkcja oblicza dystans między dwoma obiektami
def dist_angle(self, other):
    xy_self = self.rect
    xy_other = other.rect
    tan = xy_other[0]-xy_self[0],xy_other[1]-xy_self[1]
    distance = math.sqrt(pow((xy_other[0]-xy_self[0]),2)+pow((xy_other[1]-xy_self[1]),2))
    angle = math.atan2(tan[0],tan[1])
    return [distance,angle]
#Funkcja tworzy grupę pop'ów
def create_village(population, speed):
    village = pygame.sprite.Group()
    for i in range(population):
        village.add(pop([random.uniform(0,470),random.uniform(0,350)], speed ))
    return village
#Funkcja tworzy grupę z jedzeniem
def create_stack(amount):
    stack = pygame.sprite.Group()
    for i in range(amount):
        stack.add(food([random.uniform(0,470),random.uniform(0,350)]))
    return stack
#jeżeli poziom jedzenia spadnie poniżej 40 obiektów, metoda wygeneruje do 20 obiektów
def grow_food(self):
    if len(self.sprites())<40:
        for i in range(random.randrange(21)):
            self.add(food([random.uniform(0,470),random.uniform(0,350)]))
#metoda odpowiedzialna za rysowanie wszystkiego na ekranie monitora
def drawscreen(screen):
    screen.fill(green)
    village.draw(screen)
    stack.draw(screen)
    pygame.display.update()
    pygame.time.delay(100)




size = 10
green = 0,100,0
size = width, length = 480,360
screen = pygame.display.set_mode(size)

screen.fill(green)
#creating a first inhabitant
population = 100
village = create_village(population,5)
stack = create_stack(population)
pygame.init()
pygame.display.flip()
QUIT = pygame.QUIT
KEYDOWN = pygame.KEYDOWN

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    sight(village,stack)
    eat(village, stack)
    grow_food(stack)
    drawscreen(screen)
