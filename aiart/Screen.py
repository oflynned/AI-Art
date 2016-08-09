import pygame
import random


class Screen(object):
    WIDTH = 640
    HEIGHT = 480
    WHITE = (254, 254, 254)

    def __init__(self):
        self.display = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT), 0, 32)
        pygame.display.set_caption("AI Art")
        self.display.fill(Screen.WHITE)
        self.square = pygame.Surface((1, 1))

    def draw(self, color):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        self.display.set_at((x, y), color)
        draw_me = pygame.Rect(x, y, 1, 1)
        self.display.blit(self.square, draw_me)
        pygame.display.update()

    def returnSurfaceArray(self):
        pass