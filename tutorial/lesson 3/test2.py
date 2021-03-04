import pygame
from pygame.locals import *

SIZE = 600, 600
RED = (255, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode(SIZE)

rect = Rect(200, 220, 90, 90)
rect2 = Rect(300, 300, 200, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, rect)
    pygame.draw.rect(screen, BLUE, rect2)
    
    pygame.draw.ellipse(screen, RED, (50, 20, 160, 100))
    pygame.draw.ellipse(screen, WHITE, (200, 60, 160, 100))
    pygame.draw.ellipse(screen, BLUE, (350, 100, 160, 100))    

    pygame.display.flip()
    
pygame.quit()
