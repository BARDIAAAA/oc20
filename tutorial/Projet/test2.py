import pygame
from pygame.locals import *

# Variables
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


drawing = False

key_dict = {K_r:RED, K_g:GRAY, K_v:GREEN, K_w:WHITE, K_b:BLUE}
start = (0, 0)
undo = []
line = []
list_lines = []



# Initialisation de PyGame
pygame.init()

# Taille de la fenêtre
screen = pygame.display.set_mode((800, 800))

img = pygame.image.load('ferrari.jpg')
img.convert()
rect = img.get_rect()
rect.center = w, h = 400, 400
moving = False
bg = WHITE

while True:
    for event in pygame.event.get():
        # Event (on appuie sur une touche)
        if event.type == KEYDOWN:
            if event.key == K_n:
                # Si true alors définir à false
                if (moving):
                    moving = False
                # Sinon définir à true
                else:
                    moving = True
            elif event.key == K_z:
                if (len(list_lines) > 0):
                    undo.append(list_lines[-1])
                    list_lines.pop()
            elif event.key == K_y:
                if (len(undo) > 1):
                    list_lines.append(undo[-1])
                    undo.pop()
            # Pour toutes les autres touches préssées
            # On vérifie si celle-ci change le fond d'écran
            else:
                for key in key_dict.keys():
                    if event.key == key:
                        bg = key_dict.get(key)
         
        # Si la souris bouge et que moving = true
        # Alors synchroniser les mouvement de la souris avec ceux de l'image
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
        
        # Quand on clique on pose le premier point du segment
        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            line.append(start)
            drawing = True
        
        # Quand on clique on créer un point A (bouton cliqué)
        # et le point b (relachement du bouton)
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            line.append(end)
            list_lines.append(line)
            line = []
            drawing = False
     
    screen.fill(bg)
    screen.blit(img, rect)
    
    # Si il y a des lignes alors on les affiches
    if len(list_lines) > 0:
        for line_i in list_lines:
            pygame.draw.lines(screen, BLACK, True, line_i, 3)
            
    pygame.display.update()
pygame.quit()