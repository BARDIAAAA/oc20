import pygame


class Color: # Création de la classe des couleurs.
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


class Path: # Chargement de toutes les entités / musique / police
    def __init__(self):
        self.ICON = pygame.image.load('resources/images/pacman.png')
        self.PACMAN = pygame.image.load('resources/images/pacman.png')
        self.BLINKY = pygame.image.load('resources/images/Blinky.png')
        self.CLYDE = pygame.image.load('resources/images/Clyde.png')
        self.INKY = pygame.image.load('resources/images/Inky.png')
        self.PINKY = pygame.image.load('resources/images/Pinky.png')
        self.FONT = 'resources/font/arcade.ttf'
        self.MUSIC = 'resources/music/pac-man-theme.wav'


class Wall: # Création de la classe "Wall" (Mur) qui va permettre d'implanter les murs que l'on souhaite
    def __init__(self, screen, color, coords):
        pygame.draw.rect(screen, color, coords)


class Fantom: # Création de la classe "Fantom" qui va permettre d'implanter les fantômes du jeu
    def __init__(self, screen, image, x, y):
        self.x = x
        self.y = y
        screen.blit(image, (x, y))


class Hero: # Création de la classe "Hero" qui va permettre d'implanter Pac-Man
    def __init__(self, screen, image, x, y):
        self.pacman = pygame.image.load('resources/images/pacman.png')
        self.x = x
        self.y = y
        self.moving = False
        screen.blit(image, (x, y))

 #   def setMoving(self, boolean):
  #      self.moving = boolean

   # def getX(self):
    #    return self.x

    #def getY(self):
     #   return self.y

    #def canMove(self):
     #   return self.moving

    #def setX(self, int):
     #   self.x = int

    #def setY(self, int):
     #   self.y = int

class Game: # Classe la plus importante, celle qui implante les murs / choisis les spawns des fantômes et de Pac-Man
    def __init__(self):
        self.color = Color()
        self.path = Path()
        self.screen = pygame.display.set_mode((535, 600))
        self.walls = [
            (0, 0, 600, 10), # Ligne tout en haut
            (0, 0, 10, 600), # Ligne tout à gauche
            (525, 0, 10, 600), # Ligne tout à gauche
            (0, 590, 600, 10), # Ligne tout en bas
            (265, 0, 10, 160), # Ligne verticale centrale haut
            (265, 450, 10, 150), # Ligne verticale centrale bas
            (0, 295, 150, 10), # Ligne horizontale centrale gauche
            (390, 295, 150, 10), # Ligne horizontale centrale droite
            (330, 270, 10, 60), # Cage, mur droite
            (200, 270, 10, 60), # Cage, mur gauche
            (200, 330, 140, 10), # Cage, mur bas
            (200, 270, 45, 10), # Cage, mur haut gauche
            (295, 270, 45, 10), # Cage, mur haut droite
            (200, 390, 140, 10), # Ligne horizontale centrale bas
            (200, 210, 140, 10), # Ligne horizontale centrale haut
            (200, 65, 10, 150), # Ligne verticale centrale gauche haut
            (330, 65, 10, 150), # Ligne verticale centrale droite haut
            (200, 390, 10, 145), # Ligne verticale centrale gauche bas
            (330, 390, 10, 145), # Ligne verticale centrale droite bas
            (65, 65, 10, 175), # Ligne verticale gauche gauche haut
            (460, 65, 10, 175), # Ligne verticale droite droite haut
            (65, 360, 10, 175), # Ligne verticale gauche gauche bas
            (460, 360, 10, 175), # Ligne verticale droite droite bas
            (65, 65, 80, 10), # Ligne horizontale gauche haut
            (130, 130, 10, 110), # Ligne verticale gauche haut seule
            (65, 525, 80, 10), # Ligne horizontale gauche bas
            (130, 360, 10, 110), # Ligne verticale gauche bas seule
            (392, 65, 75, 10), # Ligne horizontale droite haut
            (395, 130, 10, 110), # Ligne verticale droite haut seule
            (392, 525, 75, 10), # Ligne horizontale droite bas
            (395, 360, 10, 110), # Ligne verticale droite bas seule
        ]
        self.fantoms = [#Coordonnées des points de spawns des fantômes
            [self.path.BLINKY, 280, 289],
            [self.path.CLYDE, 280, 289],
            [self.path.INKY, 230, 289],
            [self.path.PINKY, 230, 289]
        ]
        self.heros = [#Coordonnées des points de spawn de Pac-Man
            [self.path.PACMAN, 220, 550]
        ]

    def init(self):
        pygame.init()
        pygame.display.set_icon(self.path.ICON)
        pygame.display.set_caption("Pac-Man")
        pygame.display.set_mode((535, 600))
        self.screen.fill(self.color.BLACK)
        while True:
            for wall in self.walls:
                Wall(self.screen, self.color.CIEL, wall)
            # Spawn les fantômes
            for fantom in self.fantoms:
                Fantom(self.screen, fantom[0], fantom[1], fantom[2])
            # Spawn Pac-Man
            for hero in self.heros:
                player = Hero(self.screen, hero[0], hero[1], hero[2])
         #   for event in pygame.event.get():
          #          if event.type == pygame.KEYDOWN:
           #             if event.key == pygame.K_LEFT:
            #                player.setMoving(True)
             #               player.setX(player.getX() - 1)
              #      if event.type == pygame.KEYUP:
               #         if player.canMove():
                #            player.setMoving(False)
                #            player.setMoving(False)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()



pygame.mixer.init()
pygame.mixer.music.load(Path().MUSIC)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

game = Game()
game.init()