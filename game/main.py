import time

import pygame


class Color:  # Création de la classe des couleurs.
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


class Path:  # Chargement de toutes les entités / musique / police
    def __init__(self):
        self.ICON = pygame.image.load('resources/images/pacman.png')
        self.PACMAN = pygame.image.load('resources/images/pacman.png')
        self.BLINKY = pygame.image.load('resources/images/Blinky.png')
        self.CLYDE = pygame.image.load('resources/images/Clyde.png')
        self.INKY = pygame.image.load('resources/images/Inky.png')
        self.PINKY = pygame.image.load('resources/images/Pinky.png')
        self.FONT = 'resources/font/arcade.ttf'
        self.MUSIC = 'resources/music/pac-man-theme.wav'


class Wall(pygame.sprite.Sprite):  # Création de la classe "Wall" (Mur) qui va permettre d'implanter les murs que l'on souhaite
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        # pygame.draw.rect(screen, color, coords)


class Fantom:  # Création de la classe "Fantom" qui va permettre d'implanter les fantômes du jeu
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y


class Hero(pygame.sprite.Sprite):  # Création de la classe "Hero" qui va permettre d'implanter Pac-Man
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/images/pacman.png')
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.x = x
        self.y = y
        self.prev_x = x
        self.prev_y = y
        self.moving = False
        self.moving_direction = "x"
        self.moving_speed = 25


class Game:  # Classe la plus importante, celle qui implante les murs / choisis les spawns des fantômes et de Pac-Man
    def __init__(self):
        self.color = Color()
        self.path = Path()
        self.screen = pygame.display.set_mode((535, 600))
        self.walls = [
            [0, 0, 600, 10],  # Ligne tout en haut
            [0, 0, 10, 600],  # Ligne tout à gauche
            [525, 0, 10, 600],  # Ligne tout à gauche
            [0, 590, 600, 10],  # Ligne tout en bas
            [265, 0, 10, 160],  # Ligne verticale centrale haut
            [265, 450, 10, 150],  # Ligne verticale centrale bas
            [0, 295, 150, 10],  # Ligne horizontale centrale gauche
            [390, 295, 150, 10],  # Ligne horizontale centrale droite
            [330, 270, 10, 60],  # Cage, mur droite
            [200, 270, 10, 60],  # Cage, mur gauche
            [200, 330, 140, 10],  # Cage, mur bas
            [200, 270, 45, 10],  # Cage, mur haut gauche
            [295, 270, 45, 10],  # Cage, mur haut droite
            [200, 390, 140, 10],  # Ligne horizontale centrale bas
            [200, 210, 140, 10],  # Ligne horizontale centrale haut
            [200, 65, 10, 150],  # Ligne verticale centrale gauche haut
            [330, 65, 10, 150],  # Ligne verticale centrale droite haut
            [200, 390, 10, 145],  # Ligne verticale centrale gauche bas
            [330, 390, 10, 145],  # Ligne verticale centrale droite bas
            [65, 65, 10, 175],  # Ligne verticale gauche gauche haut
            [460, 65, 10, 175],  # Ligne verticale droite droite haut
            [65, 360, 10, 175],  # Ligne verticale gauche gauche bas
            [460, 360, 10, 175],  # Ligne verticale droite droite bas
            [65, 65, 80, 10],  # Ligne horizontale gauche haut
            [130, 130, 10, 110],  # Ligne verticale gauche haut seule
            [65, 525, 80, 10],  # Ligne horizontale gauche bas
            [130, 360, 10, 110],  # Ligne verticale gauche bas seule
            [392, 65, 75, 10],  # Ligne horizontale droite haut
            [395, 130, 10, 110],  # Ligne verticale droite haut seule
            [392, 525, 75, 10],  # Ligne horizontale droite bas
            [395, 360, 10, 110],  # Ligne verticale droite bas seule
        ]
        self.fantoms = [  # Coordonnées des points de spawns des fantômes
            Fantom(self.path.BLINKY, 280, 289),
            Fantom(self.path.CLYDE, 280, 289),
            Fantom(self.path.INKY, 230, 289),
            Fantom(self.path.PINKY, 230, 289)
        ]
        self.heros = [  # Coordonnées des points de spawn de Pac-Man
            #[self.path.PACMAN, 220, 550]
            Hero(220, 550)
        ]
        self.wall_sprites = pygame.sprite.Group()

    def init(self):
        pygame.init()
        pygame.display.set_icon(self.path.ICON)
        pygame.display.set_caption("Pac-Man")
        pygame.display.set_mode((535, 600))
        self.screen.fill(self.color.BLACK)
        while True:
            self.screen.fill(self.color.BLACK)

            # Spawn les fantômes
            # Spawn Pac-Man
            for hero in self.heros:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP and self.update(self.wall_sprites):
                            hero.moving = True
                            hero.moving_direction = "y"
                            hero.moving_speed = -25
                        if event.key == pygame.K_DOWN:
                            hero.moving = True
                            hero.moving_direction = "y"
                            hero.moving_speed = 25
                        if event.key == pygame.K_LEFT:
                            hero.moving = True
                            hero.moving_direction = "x"
                            hero.moving_speed = -25
                        if event.key == pygame.K_RIGHT:
                            hero.moving = True
                            hero.moving_direction = "x"
                            hero.moving_speed = 25
                    if event.type == pygame.KEYUP:
                        if hero.moving:
                            hero.moving = False
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                if hero.moving:
                    time.sleep(0.09)
                    if hero.moving_direction == "x":
                        hero.x = hero.x + hero.moving_speed
                    if hero.moving_direction == "y":
                        hero.y = hero.y + hero.moving_speed

                self.screen.blit(hero.image, (hero.x, hero.y))

            for fantom in self.fantoms:
                self.screen.blit(fantom.image, (fantom.x, fantom.y))
            for wall in self.walls:
                mur = Wall(*wall, self.color.CIEL)
                self.wall_sprites.add(mur)
                self.wall_sprites.draw(self.screen)

            pygame.display.update()

    def update(self, wall_sprites):
        for hero in self.heros:
            if not hero.moving:
                return False
            x_prev = hero.rect.left
            y_prev = hero.rect.top
            is_collide = pygame.sprite.spritecollide(hero, wall_sprites, False)
            if is_collide:
                self.rect.left = x_prev
                self.rect.top = y_prev
                return False
            return True

#pygame.mixer.init()
#pygame.mixer.music.load(Path().MUSIC)
#pygame.mixer.music.play(-1)
#pygame.mixer.music.set_volume(0.1)

game = Game()
game.init()
