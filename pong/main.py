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
    paddle1_rapidity = 0
    paddle2_rapidity = 0
    left_score = 0
    right_score = 0


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


pygame.init()
pygame.display.set_caption("Pong!")
