import pygame
import time
import math
import sys
import random
class pop(pygame.sprite.Sprite):
    #constructor, pass in x and y as position of the pop, and speed[int] for defining speed
    def __init__(self, pos = [240,180], speed=5, color = [0,0,100], rect = [10,10]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([rect[0],rect[1]])
        self.image.fill(color)
        self.rect = pygame.Rect(int(pos[0]),int(pos[1]),rect[0],rect[1])
        self.radius = 50
        self.speed = speed
        self.belly = 1
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


def run_away(self):
    population = self.sprites()
    for pops in population:
        pos = pops.rect
        if pos[0]>240 and pos[1]>180:
            pops.move(math.pi/4)
        elif pos[0]<240 and pos[1]>180:
            pops.move(-math.pi/4)
        elif pos[0]<240 and pos[1]<180:
            pops.move(math.pi+math.pi/4)
        elif pos[0]>240 and pos[1]<180:
            pops.move(math.pi-math.pi/4)

def hide(self,where):
    sight(self, where)


#metoda opodwiadająca za wykrywanie kolizji i zjadanie jedzenia
def eat(self, other):
    ate =  pygame.sprite.groupcollide(self, other, False ,True)
    for lucky in ate:
        lucky.belly = lucky.belly + len(ate[lucky])



def protected(fort,other):
    global safe
    safe_villager = pygame.sprite.groupcollide(fort, other, False, True)

    for forts in safe_villager:
        for villager in safe_villager[forts]:
            safe.add(villager)


def go_outside(self,other):
    for pop in self:
        pop.remove(self)
        other.add(pop)

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
    stack.color = [0,0,100]
    for i in range(amount):
        stack.add(food([random.uniform(0,470),random.uniform(0,350)]))
    return stack

#tworzy miejsca w których villager może się ukryć
def create_forts():
    stack = pygame.sprite.Group()
    black = [0,0,0]
    stack.add(pop(pos = [120,90],rect = [20,20], color = black ))
    stack.add(pop(pos = [360,270],rect = [20,20], color = black))
    stack.add(pop(pos = [360,90],rect = [20,20], color = black))
    stack.add(pop(pos = [120,270],rect = [20,20],color = black))
    return stack
#jeżeli poziom jedzenia spadnie poniżej 40 obiektów, metoda wygeneruje do 20 obiektów

def grow_food(self):
    for i in range(random.randrange(21)):
        self.add(food([random.uniform(0,470),random.uniform(0,350)]))
#metoda odpowiedzialna za rysowanie wszystkiego na ekranie monitora

def create_wolfpack(population, speed):
        wolfpack = pygame.sprite.Group()
        wolfpack.color = [220,220,220]
        for i in range(population):
            wolfpack.add(pop([random.uniform(0,470),random.uniform(0,350)], speed, wolfpack.color  ))
        return wolfpack
def redeploy(self):
    pack = self.sprites()
    for i in range(len(pack)):
        if i%4==0:
            pack[i].rect[0]=0
            pack[i].rect[1]=random.uniform(0,350)
        if i%4==1:
            pack[i].rect[0]=random.uniform(0,470)
            pack[i].rect[1]=0
        if i%4==2:
            pack[i].rect[0]=random.uniform(0,470)
            pack[i].rect[1]=350
        if i%4==3:
            pack[i].rect[0]=470
            pack[i].rect[1]=random.uniform(0,350)
def multiply(self,col=[0,0,100] ):
    all = self.copy()
    for sprite in all.sprites():
        while sprite.belly>2:
            self.add(pop([sprite.rect[0]+random.randint(0,10),sprite.rect[1]+random.randint(0,10)],sprite.speed, color = col))
            sprite.belly = sprite.belly - 2

        if sprite.belly == 0:
            sprite.kill()
        sprite.belly = sprite.belly -1

def drawscreen(screen):
    global i
    screen.fill(green)
    village.draw(screen)
    stack.draw(screen)
    forts.draw(screen)
    wolfpack.draw(screen)
    screen.blit(alive_villagers, [480,0])
    screen.blit(alive_wolves, [480,30])
    screen.blit(day, [480,60])

#    man.draw(screen)
    pygame.display.update()
    pygame.time.delay(100)

pygame.init()
#setting up colours
green = 0,100,0
grey = 220,220,220

#setting up screen1
size = 10
size = width, length = 720,360
screen = pygame.display.set_mode(size)
screen.fill(green)

#setting up text



#creating a first inhabitants
Year = 0
safe = pygame.sprite.Group()
#man = pop()
population = 100
village = create_village(population,5)
stack = create_stack(int(0/4))
wolfpack = create_wolfpack(int(1), 7)
forts = create_forts()
days = 200
font = pygame.font.Font('freesansbold.ttf', 16)
alive_villagers = font.render('alive villagers:'+str(len(village)), True, [0,0,0], green)
alive_wolves = font.render('alive wolves:'+str(len(wolfpack)), True, [0,0,0], green)
day = font.render('Year:'+str(Year)+'Day:'+str(0), True, [0,0,0], green)

pygame.display.flip()
QUIT = pygame.QUIT
KEYDOWN = pygame.KEYDOWN



while True:

    for i in range(days):
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                sys.exit()


        alive_villagers = font.render('alive villagers:'+str(len(village)+len(safe)), True, [0,0,0], green)
        alive_wolves = font.render('alive wolves:'+str(len(wolfpack)), True, [0,0,0], green)
        day = font.render('Year:'+str(Year)+'      Day:'+str(i), True, [0,0,0], green)

        if i<=50:
            #w "roku" występuje podział na okresy
            sight(village,stack)
            eat(village, stack)
            run_away(wolfpack)
        if i>50 and i <=100:
            sight(wolfpack,village)
            hide(village,forts)
            eat(wolfpack, village)
            protected(forts,village)
            eat(village, stack)
        if i>100 and i<=150:
            village.update()
            run_away(wolfpack)
            eat(village, stack)
            go_outside(safe,village)
            run_away(wolfpack)
        if i>150:
            sight(village,stack)
            eat(village,stack)

        if i%5 == 0:
            grow_food(stack)
            pass
        if i%100 == 0 :
            multiply(village)
            multiply(safe)
        if i==(days-1):
            multiply(wolfpack, grey)
        if i == 50:
            redeploy(wolfpack)
        drawscreen(screen)
    Year = Year +1
