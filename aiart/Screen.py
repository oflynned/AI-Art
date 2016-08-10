import pygame
import random


class Screen(object):
    WIDTH = 640
    HEIGHT = 480
    WHITE = (254, 254, 254)
    BOX_SIZE = 5

    def __init__(self):
        self.display = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT), 0, 24)
        self.display.fill(Screen.WHITE)
        self.square = pygame.Surface((Screen.BOX_SIZE, Screen.BOX_SIZE))

    def draw(self, color):
        x = random.randint(0, Screen.WIDTH)
        y = random.randint(0, Screen.HEIGHT)

        draw_me = pygame.Rect(x, y, Screen.BOX_SIZE, Screen.BOX_SIZE)
        pygame.draw.rect(self.display, color, draw_me)

        pygame.display.update()

    def returnSurfaceArray(self):
        pass