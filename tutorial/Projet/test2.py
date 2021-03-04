import pygame
from pygame.locals import *

SIZE = 600, 600
RED = (255, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.init()
w, h = 600, 600
screen = pygame.display.set_mode((w, h))
running = True

img = pygame.image.load('bird.png')
img.convert()
rect = img.get_rect()
rect.center = w, h = 400, 330
moving = False


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False
            
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
            
    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, rect)
#     pygame.draw.rect(screen, BLUE, rect2)
    
    pygame.draw.ellipse(screen, RED, (50, 20, 160, 100))
    pygame.draw.ellipse(screen, WHITE, (200, 60, 160, 100))
    pygame.draw.ellipse(screen, BLUE, (350, 100, 160, 100))    

#     pygame.draw.rect(screen, RED, rect1, 1)
    screen.blit(img, rect)
    pygame.display.flip()
    
pygame.quit()