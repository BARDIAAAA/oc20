"""Place a rectangle with the mouse."""

# 1) Ajouter KEYDOWN : RGBY --> changer la couleur
# 2) Ajouter KEYDOWN : 01234 --> changer l'épaisseur

import pygame
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

start = (0, 0)
size = (0, 0)
drawing = False
running = True

color = GREEN
thickness = 1

pygame.init()
screen = pygame.display.set_mode((640, 240))

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            print(event.unicode)
            
            if event.unicode == '0':
                thickness = 0
            elif event.unicode == '1':
                thickness = 10
            elif event.unicode == '2':
                thickness = 20
            elif event.unicode == '3':
                thickness = 30
            elif event.unicode == '4':
                thickness = 40
                
            elif event.unicode == 'r' :
                color = RED
            elif event.unicode == 'g' :
                color = GREEN
            elif event.unicode == 'b' :
                color = GRAY
            elif event.unicode == 'y' :
                color = WHITE
            print(color)

                
        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            size = 0, 0
            print('start =', start)
            drawing = True
            
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            print('size =', size)

    screen.fill(WHITE)
    pygame.draw.rect(screen, color, (start, size), thickness)
    pygame.display.update()

pygame.quit()