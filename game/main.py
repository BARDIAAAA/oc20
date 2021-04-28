import os
import sys
import pygame
import levels as levels

class Paths:
    def __init__(self):
        self.ICON = os.path.join(os.getcwd(), 'resources/images/pacman.png')
        self.FONT = os.path.join(os.getcwd(), 'resources/font/arcade.ttf')
        self.PACMAN = os.path.join(os.getcwd(), 'resources/images/pacman.png')
        self.BLINKY = os.path.join(os.getcwd(), 'resources/images/Blinky.png')
        self.CLYDE = os.path.join(os.getcwd(), 'resources/images/Clyde.png')
        self.INKY = os.path.join(os.getcwd(), 'resources/images/Inky.png')
        self.PINKY = os.path.join(os.getcwd(), 'resources/images/Pinky.png')

class Colors:
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.GREY = (128, 128, 128)
        self.YELLOW = (255, 215, 0)
        self.BLUE = (65, 105, 225)
        self.CIEL = (0, 153, 153)
        self.PURPLE = (102, 102, 255)

class Game:
    def __init__(self):
        self.color = Colors()
        self.path = Paths()
        self.score = 0
        self.clock = pygame.time.Clock()

    def start(self, level, screen, font):
        walls = level.setupWalls(self.color.PURPLE)
        gate = level.setupGate(self.color.BLACK)
        heroes, ghost_sprites = level.setupPlayers(
            self.path.PACMAN,
            [self.path.BLINKY, self.path.CLYDE, self.path.INKY, self.path.PINKY]
        )
        foods = level.setupFood(self.color.CIEL, self.color.WHITE)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(-1)
                for hero in heroes:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            hero.changeSpeed([-1, 0])
                            hero.is_move = True
                            
                        elif event.key == pygame.K_RIGHT:
                            hero.changeSpeed([1, 0])
                            hero.is_move = True
                            
                        elif event.key == pygame.K_UP:
                            hero.changeSpeed([0, -1])
                            hero.is_move = True
                            
                        elif event.key == pygame.K_DOWN:
                            hero.changeSpeed([0, 1])
                            hero.is_move = True
                        
                        elif event.key == pygame.K_o:
                            pygame.mixer.music.pause()
                            
                        elif event.key == pygame.K_l:
                            pygame.mixer.music.unpause()

                    if event.type == pygame.KEYUP:
                        if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or \
                                (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
                            hero.is_move = False 
                            
            screen.fill(self.color.BLACK)
            for hero in heroes:
                hero.update(walls, gate)
                food_eaten = pygame.sprite.spritecollide(hero, foods, True)
            self.score += len(food_eaten)
            heroes.draw(screen)
            walls.draw(screen)
            gate.draw(screen)
            foods.draw(screen)
            for ghost in ghost_sprites:
                if ghost.tracks_loc[1] < ghost.tracks[ghost.tracks_loc[0]][2]:
                    ghost.changeSpeed(ghost.tracks[ghost.tracks_loc[0]][0: 2])
                    ghost.tracks_loc[1] += 1
                else:
                    if ghost.tracks_loc[0] < len(ghost.tracks) - 1:
                        ghost.tracks_loc[0] += 1
                    elif ghost.role_name == 'Clyde':
                        ghost.tracks_loc[0] = 2
                    else:
                        ghost.tracks_loc[0] = 0
                    ghost.changeSpeed(ghost.tracks[ghost.tracks_loc[0]][0: 2])
                    ghost.tracks_loc[1] = 0
                if ghost.tracks_loc[1] < ghost.tracks[ghost.tracks_loc[0]][2]:
                    ghost.changeSpeed(ghost.tracks[ghost.tracks_loc[0]][0: 2])
                else:
                    if ghost.tracks_loc[0] < len(ghost.tracks) - 1:
                        loc0 = ghost.tracks_loc[0] + 1
                    elif ghost.role_name == 'Clyde':
                        loc0 = 2
                    else:
                        loc0 = 0
                    ghost.changeSpeed(ghost.tracks[loc0][0: 2])
                ghost.update(walls, None)
            ghost_sprites.draw(screen)
            score_text = font.render("Score:%s" % self.score, True, self.color.WHITE)
            screen.blit(score_text, [10, 10])
            if len(foods) == 0:
                is_clearance = True
                break
            if pygame.sprite.groupcollide(heroes, ghost_sprites, False, False):
                is_clearance = False
                break
            pygame.display.flip()
            self.clock.tick(10)
        return is_clearance

def showText(screen, font, is_clearance, flag=False):
    clock = pygame.time.Clock()
    msg = 'Vous avez perdu.' if not is_clearance else 'Victoire !'
    positions = [[175, 233], [35, 303], [53, 333]] if not is_clearance else [[230, 233], [35, 303], [53, 333]]
    surface = pygame.Surface((400, 200))
    surface.set_alpha(10)
    surface.fill((128, 128, 128))
    screen.blit(surface, (100, 200))
    texts = [font.render(msg, True, Colors().WHITE),
             font.render('Appuyez sur ENTER pour rejouer.', True, Colors().WHITE),
             font.render('Appuyez sur ESC pour quitter.', True, Colors().WHITE)]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if is_clearance:
                        if not flag:
                            return
                        else:
                            main(initialize())
                    else:
                        main(initialize())
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
        for idx, (text, position) in enumerate(zip(texts, positions)):
            screen.blit(text, position)
        pygame.display.flip()
        clock.tick(10)

def initialize():
    pygame.init()
    icon_image = pygame.image.load(Paths().ICON)
    pygame.display.set_icon(icon_image)
    screen = pygame.display.set_mode([606, 606])
    pygame.display.set_caption('Pac-Man')
    return screen

def main(screen):
    pygame.font.init()
    font_small = pygame.font.Font(Paths().FONT, 15)
    font_big = pygame.font.Font(Paths().FONT, 18)
    for num_level in range(1, levels.NUMLEVELS + 1):
        level = getattr(levels, f'Level{num_level}')()
        is_clearance = Game().start(level, screen, font_small)
        if num_level == levels.NUMLEVELS:
            showText(screen, font_big, is_clearance, True)
        else:
            showText(screen, font_big, is_clearance)
            
pygame.mixer.init()
pygame.mixer.music.load("pac-man.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.025)

main(initialize())