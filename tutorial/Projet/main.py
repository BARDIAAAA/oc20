import pygame
from pygame.locals import *

class color:
    def __init__(self):
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.gray = (150, 150, 150)
        self.green = (0, 255, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 0, 255)
        
class segment:
    def __init__(self):
        self.start = (0, 0)
        self.end = (0, 0)
        
    def setStart(position):
        segment.start = position
        
    def setEnd(position):
        segment.end = position
    
    def getSegment():
        list = []
        list.append(segment.start)
        list.append(segment.end)
        return list

class main:
    "Lancement du logiciel"
    def __init__(self):
        self.color = color()
        self.segment = segment()
        self.undo = []
        self.list_lines = []
        self.background = self.color.white
        
        # Brouillon
        key_dict = {K_r:self.color.red, K_g:self.color.gray, K_v:self.color.green, K_w:self.color.white, K_b:self.color.blue}
        pygame.init()
        screen = pygame.display.set_mode((800, 800))
        img = pygame.image.load('bird.')
        img.convert()
        rect = img.get_rect()
        rect.center = w, h = 400, 400
        moving = False

        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    
                    if event.key == K_n:
                        if (moving):
                            moving = False
                        else:
                            moving = True
                            
                    elif event.key == K_z:
                        if (len(self.list_lines) > 0):
                            self.undo.append(self.list_lines[-1])
                            self.list_lines.pop()
                            
                    elif event.key == K_y:
                        if (len(self.undo) > 1):
                            self.list_lines.append(self.undo[-1])
                            self.undo.pop()
                    else:
                        for key in key_dict.keys():
                            if event.key == key:
                                self.background = key_dict.get(key)
                                
                elif event.type == MOUSEMOTION and moving:
                    rect.move_ip(event.rel)
                    
                elif event.type == MOUSEBUTTONDOWN:
                    segment.setStart(event.pos)                  
                elif event.type == MOUSEBUTTONUP:
                    segment.setEnd(event.pos)
                    self.list_lines.append(segment.getSegment())
                    
            screen.fill(self.background)
            screen.blit(img, rect)
            
            if len(self.list_lines) > 0:
                for line_i in self.list_lines:
                    pygame.draw.lines(screen, self.color.black, True, line_i, 3)
                    
            pygame.display.update()
            
    pygame.quit()

print(main.__doc__)
main()