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

    def getSegment():
        line = []
        line.append(segment.start)
        line.append(segment.end)
        return line


class image:
    def __init__(self):
        self.img = pygame.image.load('bird.png')
        self.moving = False
        self.rect = self.img.get_rect()
        self.x = 250
        self.y = 250


class main:
    def __init__(self):
        self.color = color()
        self.segment = segment()
        self.image = image()
        self.undo = []
        self.list_lines = []
        self.background = self.color.white
        self.key_dict = {
            K_r: self.color.red,
            K_g: self.color.gray,
            K_v: self.color.green,
            K_w: self.color.white,
            K_b: self.color.blue
        }
        self.screen = pygame.display.set_mode((800, 800))

        pygame.init()
        self.image.img.convert()

        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_n:
                        if (self.image.moving):
                            self.image.moving = False
                        else:
                            self.image.moving = True

                    elif event.key == K_UP:
                        self.image.y -= 10
                    elif event.key == K_DOWN:
                        self.image.y += 10
                    elif event.key == K_LEFT:
                        self.image.x -= 10
                    elif event.key == K_RIGHT:
                        self.image.x += 10

                    elif event.key == K_k:
                        self.image.x = 250
                        self.image.y = 250

                    elif event.key == K_z:
                        if (len(self.list_lines) > 0):
                            self.undo.append(self.list_lines[-1])
                            self.list_lines.pop()
                    elif event.key == K_y:
                        if (len(self.undo) > 0):
                            self.list_lines.append(self.undo[-1])
                            self.undo.pop()

                    else:
                        for key in self.key_dict.keys():
                            if event.key == key:
                                self.background = self.key_dict.get(key)

                elif event.type == MOUSEMOTION and self.image.moving:
                    convert = self.image.img.convert()
                    h, w = convert.get_height(), convert.get_width()
                    x, y = pygame.mouse.get_pos()

                    self.image.x, self.image.y = x - h / 2, y - w / 2

                elif not self.image.moving:
                    if event.type == MOUSEBUTTONDOWN:
                        segment.start = event.pos
                    elif event.type == MOUSEBUTTONUP:
                        segment.end = event.pos
                        self.list_lines.append(segment.getSegment())

            self.screen.fill(self.background)
            self.screen.blit(self.image.img, (self.image.x, self.image.y))

            if len(self.list_lines) > 0:
                for line_i in self.list_lines:
                    pygame.draw.lines(self.screen, self.color.black, True, line_i, 3)

            pygame.display.update()

    pygame.quit()


main()