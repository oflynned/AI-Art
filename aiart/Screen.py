import pygame
import random
import numpy as np


class Screen(object):
    WIDTH = 640
    HEIGHT = 480
    WHITE = (255, 255, 255)

    def __init__(self):
        self.display = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT), 0, 24)
        # pygame.display.set_caption("AI Art")
        self.display.fill(Screen.WHITE)
        self.square = pygame.Surface((1, 1))
        self.imageArray = np.zeros((Screen.WIDTH, Screen.HEIGHT), dtype=np.uint8)
        # self.x = 0
        # self.y = 0
        # self.row = 0
        # self.col = 0

    # def draw(self, color):
    #     x = random.randint(0, 100)
    #     y = random.randint(0, 100)
    #     self.display.set_at((x, y), color)
    #     draw_me = pygame.Rect(x, y, 1, 1)
    #     self.display.blit(self.square, draw_me)
    #     pygame.display.update()

    def draw(self, X, Y, color):
        x = random.randint(0, Screen.HEIGHT)
        y = random.randint(0, Screen.WIDTH)
        # self.display.set_at((self.x, self.y), color)
        draw_me = pygame.Rect(X, Y, 7, 7)
        # self.x += 1
        # self.y += 1
        # self.display.blit(self.square, draw_me)
        pygame.draw.rect(self.display, color, draw_me)
        pygame.display.update()

    def fillImageArray(self, x, y):
        pass