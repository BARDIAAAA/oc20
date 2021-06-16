# Importations
import pygame
import random
import sys


# Création d'une classe "Settings" qui présente les valeurs initales des différents caractéristiques du jeux.
class Settings:
    WIDTH = 1000
    HEIGHT = 700
    BALL_RADIUS = 20
    PAD_WIDTH = 8
    PAD_HEIGHT = 80
    HALF_PAD_WIDTH = PAD_WIDTH / 2
    HALF_PAD_HEIGHT = PAD_HEIGHT / 2


# Création de la classe "Color". Couleur que nous allons utiliser par la suite.
class Color:
    def __init__(self):
        self.WHITE = (255, 255, 255)
        self.RED = (200, 0, 0),
        self.BLACK = (0, 0, 0),
        self.BLUE = (65, 105, 225)
        self.GREEN = (0, 120, 75)
        self.ORANGE = (255, 69, 0)
        self.GRAY = (169,169,169)


# Création de la classe "Paddle" qui va donner les valeurs par défaut aux raquettes (Position de la raquette / Score / etc...).
class Paddle:
    def __init__(self):
        self.position = [0, 0]
        self.score_position = (0, 0)
        self.score = 0
        self.color = Color().BLACK
        self.key_up = pygame.K_UP
        self.key_down = pygame.K_DOWN
        self.rapidity = 0


class Ball:
    def __init__(self):
        self.settings = Settings()
        self.position = [(self.settings.WIDTH / 2), (self.settings.HEIGHT / 2)]
        self.rapidity = [0, 0]


# Création de la classe "Game" qui va lancer le jeu.
class Game:
    def __init__(self):
        self.settings = Settings()
        self.color = Color()
        self.ball = Ball()
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        self.horz = 0
        self.vert = 0
        self.paddles = []
        self.pause = False

    def ball_start(self, right):
        self.ball = Ball()
        self.horz = random.randrange(2, 4)
        self.vert = random.randrange(1, 3)

        if not right:
            self.horz = -self.horz

        self.ball.rapidity = [self.horz, -self.vert]

    def show(self):
        self.screen.fill(self.color.BLACK)

        pygame.draw.line(self.screen, self.color.WHITE, [500, 0], [500, 310], 1)  # Ligne verticale haute (A, B, épaisseur)
        pygame.draw.line(self.screen, self.color.WHITE, [500, 390], [500, 700], 1)  # Ligne verticale basse

        pygame.draw.circle(self.screen, self.color.WHITE, [500, 350], 40, 1)  # Cercle du milieu (C1, C2, rayon, épaisseur)
        pygame.draw.circle(self.screen, self.color.WHITE, [1000, 350], 150, 2)  # Cercle de droite
        pygame.draw.circle(self.screen, self.color.WHITE, [0, 350], 150, 2)  # Cercle de gauche
        pygame.draw.circle(self.screen, self.color.ORANGE, self.ball.position, 20, 0)  # Balle

        for pad in self.paddles:  # Tous les paddles sont concernés, donc les deux paddles sont dessinés.
            pygame.draw.polygon(self.screen, pad.color,
                                [[pad.position[0] - self.settings.HALF_PAD_WIDTH, pad.position[1] - self.settings.HALF_PAD_HEIGHT],  # Point 1 (Gauche bas)
                                 [pad.position[0] - self.settings.HALF_PAD_WIDTH, pad.position[1] + self.settings.HALF_PAD_HEIGHT],  # Point 2 (Gauche haut)
                                 [pad.position[0] + self.settings.HALF_PAD_WIDTH, pad.position[1] + self.settings.HALF_PAD_HEIGHT],  # Point 3 (Droite haut)
                                 [pad.position[0] + self.settings.HALF_PAD_WIDTH, pad.position[1] - self.settings.HALF_PAD_HEIGHT]], 0)  # Point 4 (Droite bas)

            font = pygame.font.SysFont("Georgia Pro", 50, False, False)
            text = font.render(str(pad.score), True, pad.color)
            self.screen.blit(text, pad.score_position)

            # Faire bouger les paddles
            if self.settings.HALF_PAD_HEIGHT < pad.position[1] < self.settings.HEIGHT - self.settings.HALF_PAD_HEIGHT:
                pad.position[1] += pad.rapidity
            elif pad.position[1] == self.settings.HALF_PAD_HEIGHT and pad.rapidity > 0:
                pad.position[1] += pad.rapidity
            elif pad.position[1] == self.settings.HEIGHT - self.settings.HALF_PAD_HEIGHT and pad.rapidity < 0:
                pad.position[1] += pad.rapidity

            # Mouvement de la balle
            self.ball.position[0] += self.ball.rapidity[0]
            self.ball.position[1] += self.ball.rapidity[1]
            if self.ball.position[1] <= self.settings.BALL_RADIUS:
                self.ball.rapidity[1] = - self.ball.rapidity[1]
            if self.ball.position[1] >= self.settings.HEIGHT + 1 - self.settings.BALL_RADIUS:
                self.ball.rapidity[1] = -self.ball.rapidity[1]

            # Collisions des murs
            hit_left_wall = self.ball.position[0] <= self.settings.BALL_RADIUS + self.settings.PAD_WIDTH
            hit_paddle_a = self.paddles[0].position[1] - self.settings.HALF_PAD_HEIGHT < self.ball.position[1] < self.paddles[0].position[1] + self.settings.HALF_PAD_HEIGHT

            if hit_left_wall and hit_paddle_a:
                self.ball.rapidity[0] = -self.ball.rapidity[0]
                self.ball.rapidity[0] *= 1.2
                self.ball.rapidity[1] *= 1.2
            elif self.ball.position[0] <= self.settings.BALL_RADIUS + self.settings.PAD_WIDTH:
                self.paddles[1].score += 1
                self.ball_start(True)

            hit_right_wall = self.ball.position[0] >= self.settings.WIDTH + 1 - self.settings.BALL_RADIUS - self.settings.PAD_WIDTH
            hit_paddle_b = self.paddles[1].position[1] - self.settings.HALF_PAD_HEIGHT < self.ball.position[1] < self.paddles[1].position[1] + self.settings.HALF_PAD_HEIGHT

            if hit_right_wall and hit_paddle_b:
                self.ball.rapidity[0] = -self.ball.rapidity[0]
                self.ball.rapidity[0] *= 1.2
                self.ball.rapidity[1] *= 1.2
            elif int(self.ball.position[0]) >= self.settings.WIDTH + 1 - self.settings.BALL_RADIUS - self.settings.PAD_WIDTH:
                self.paddles[0].score += 1
                self.ball_start(False)

            # Fin de partie, lorsque une des personnes est arrivée à 5 points.
            if pad.score == 5:
                font = pygame.font.SysFont("Georgia Pro", 75, False, False)
                text = font.render("Victoire !", True, pad.color)
                self.screen.blit(text, (380, 80))
                font = pygame.font.SysFont("Georgia Pro", 35, False, False)
                text = font.render("Pour recommencer : ENTER", True, self.color.GRAY)
                self.screen.blit(text, (310, 160))
                font = pygame.font.SysFont("Georgia Pro", 35, False, False)
                text = font.render("Pour quitter : ESC", True, self.color.GRAY)
                self.screen.blit(text, (400, 200))
                self.ball = Ball()
                self.pause = True
                pygame.draw.line(self.screen, self.color.BLACK, [500, 0], [500, 310], 1)  # Disparition de la ligne blanche haut
                pygame.draw.line(self.screen, self.color.BLACK, [500, 390], [500, 700], 1)  # Disparition de la ligne blanche basse

    def init(self):
        pad1 = Paddle()
        pad1.position = [self.settings.HALF_PAD_WIDTH, self.settings.HEIGHT / 2]
        pad1.key_up = pygame.K_w
        pad1.key_down = pygame.K_s
        pad1.color = self.color.BLUE
        pad1.score_position = ((self.settings.WIDTH / 2) - 40, 5)
        self.paddles.append(pad1)
        pad2 = Paddle()
        pad2.position = [self.settings.WIDTH - self.settings.HALF_PAD_WIDTH, self.settings.HEIGHT / 2]
        pad2.color = self.color.RED
        pad2.score_position = ((self.settings.WIDTH / 2) + 14, 5)
        self.paddles.append(pad2)
        if random.randrange(0, 2) == 0:
            self.ball_start(True)
        else:
            self.ball_start(False)

pygame.mixer.init()
pygame.mixer.music.load('resources/music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.075)
fps = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Pong !")
game = Game()
game.init()

while True:
    game.show()
    for event in pygame.event.get():
        for paddle in game.paddles:
            if not game.pause:
                if event.type == pygame.KEYDOWN:
                    if event.key == paddle.key_up:
                        paddle.rapidity = -8
                    if event.key == paddle.key_down:
                        paddle.rapidity = 8
                if event.type == pygame.KEYUP:
                    if event.key == paddle.key_up:
                        paddle.rapidity = 0
                    if event.key == paddle.key_down:
                        paddle.rapidity = 0
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game = Game()
                        game.init()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    fps.tick(60)
    pygame.display.update()