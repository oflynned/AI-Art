import pygame
import random


class Screen(object):
    WIDTH = 56
    HEIGHT = 56
    WHITE = (254, 254, 254)

    def __init__(self):
        self.display = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT), 0, 24)
        self.display.fill(Screen.WHITE)
        self.square = pygame.Surface((2, 2))

    def draw(self, color):
        x = random.randint(0, Screen.WIDTH)
        y = random.randint(0, Screen.HEIGHT)

        draw_me = pygame.Rect(x, y, 2, 2)
        pygame.draw.rect(self.display, color, draw_me)

        pygame.display.update()

    def returnSurfaceArray(self):
        pass