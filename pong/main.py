import pygame


class Settings:
    WIDTH = 1000
    HEIGHT = 700
    BALL_RADIUS = 20
    PAD_WIDTH = 8
    PAD_HEIGHT = 80
    HALF_PAD_WIDTH = PAD_WIDTH / 2
    HALF_PAD_HEIGHT = PAD_HEIGHT / 2
    ball_rapidity = [0, 0]


class Color:
    def __init__(self):
        WHITE = (255, 255, 255)
        RED = (255, 0, 0),
        BLACK = (0, 0, 0),
        BLUE = (65, 105, 225)


class Paddle:
    def __init__(self):
        self.position = [0, 0]
        self.score_position = [0, 0]
        self.score = 0
        self.key_up = pygame.K_UP
        self.key_down = pygame.K_DOWN
        self.rapidity = 0


class Game:
    def __init__(self):
        self.settings = Settings()
        self.color = Color()
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        self.ball_pos = [(self.settings.WIDTH / 2), (self.settings.HEIGHT / 2)]
        self.horz = 0
        self.vert = 0
        self.ball_rapidity = [0, 0]
        self.paddles = []


pygame.init()
pygame.display.set_caption("Pong!")
