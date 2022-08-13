import pygame
import numpy
import math


def toDeg(num):
    return num * (180.0/math.pi)


#Calculation variables
T = (0, 6)

R = (3, 0)

C = (4, 3)

TZ = 3

TR = 1

A = toDeg(math.asin(T[1]/(math.sqrt(T[1]**2 + R[0]**2))))

B = toDeg(math.asin(C[1]/math.sqrt(C[1]**2 + (C[0] - R [0])**2)))
print(B)

#Delta variables
DELTA_X = 180 - A - B
X = 0

DELTA_Y = math.sqrt(T[1]**2+R[0]**2) - math.sqrt((C[0]-R[0])**2 + C[1]**2)
Y = 0

DELTA_Z = TZ
Z = 0


FX = None

FY = (DELTA_Y - 1)/DELTA_Y



screen = pygame.display.set_mode((900, 800))
pygame.font.init()
timer = pygame.time.Clock()
RUNNING = True

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)

font = pygame.font.SysFont('arial', 50)


screen.fill(WHITE)


def paint():

    dx = font.render(str(X), False, BLACK)
    screen.blit(dx, (X, 200))
    dy = font.render(str(Y), False, BLACK)
    screen.blit(dy, (Y, 400))
    dz = font.render(str(Z), False, BLACK)
    screen.blit(dz, (Z, 600))  
    pygame.display.flip()

paint()



while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        timer.tick(60)
