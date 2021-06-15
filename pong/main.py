import pygame
import random
import sys


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
        self.WHITE = (255, 255, 255)
        self.RED = (200, 0, 0),
        self.BLACK = (0, 0, 0),
        self.BLUE = (65, 105, 225)
        self.GREEN = (0, 120, 75)


class Paddle:
    def __init__(self):
        self.position = [0, 0]
        self.score_position = [0, 0]
        self.score = 0
        self.color = Color().BLACK
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

    def ball_start(self, right):
        self.horz = random.randrange(2, 4)
        self.vert = random.randrange(1, 3)

        if not right:
            self.horz = -self.horz

        self.ball_rapidity = [self.horz, -self.vert]

    def show(self):
        self.screen.fill(self.color.GREEN)
        pygame.draw.line(self.screen, self.color.WHITE, [self.settings.WIDTH / 2, 0], [self.settings.WIDTH / 2, self.settings.HEIGHT], 1)
        pygame.draw.circle(self.screen, self.color.WHITE, [self.settings.WIDTH / 2, self.settings.HEIGHT / 2], 70, 1)
        pygame.draw.circle(self.screen, self.color.WHITE, self.ball_pos, 20, 0)
        for paddle in self.paddles:
            pygame.draw.polygon(self.screen, paddle.color,  [[paddle.position[0] - self.settings.HALF_PAD_WIDTH, paddle.position[1] - self.settings.HALF_PAD_HEIGHT], [paddle.position[0] - self.settings.HALF_PAD_WIDTH, paddle.position[1] + self.settings.HALF_PAD_HEIGHT], [paddle.position[0] + self.settings.HALF_PAD_WIDTH, paddle.position[1] + self.settings.HALF_PAD_HEIGHT], [paddle.position[0] + self.settings.HALF_PAD_WIDTH, paddle.position[1] - self.settings.HALF_PAD_HEIGHT]], 0)

    def init(self):
        paddle = Paddle()
        paddle.position = [self.settings.HALF_PAD_WIDTH, self.settings.HEIGHT / 2]
        paddle.key_up = pygame.K_w
        paddle.key_down = pygame.K_s
        paddle.color = self.color.BLUE
        self.paddles.append(paddle)
        paddle = Paddle()
        paddle.position = [self.settings.WIDTH - self.settings.HALF_PAD_WIDTH, self.settings.HEIGHT / 2]
        paddle.color = self.color.RED
        self.paddles.append(paddle)
        if random.randrange(0, 2) == 0:
            self.ball_start(True)
        else:
            self.ball_start(False)


pygame.init()
pygame.display.set_caption("Pong !")
game = Game()
game.init()
game.show()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
