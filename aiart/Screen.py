import pygame
import random
import numpy as np


class Screen(object):
    WIDTH = 730
    HEIGHT = 480
    WHITE = (255, 255, 255)

    def __init__(self):
        self.display = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT), 0, 24)
        # pygame.display.set_caption("AI Art")
        self.display.fill(Screen.WHITE)
        self.square = pygame.Surface((1, 1)).convert()
        self.imageArray = []
        self.row = 0
        self.col = 0
        self.temp = []

    def draw(self, X, Y, color):
        x = random.randint(0, Screen.HEIGHT)
        y = random.randint(0, Screen.WIDTH)
        draw_me = pygame.Rect(X, Y, 20, 20)
        pygame.draw.rect(self.display, color, draw_me)
        pygame.display.update()

    def draw1(self, color):
        if self.col >= Screen.HEIGHT:
            self.row += 20
            self.col = 0
        else:
            draw_me = pygame.Rect(self.row, self.col, 20, 20)
            pygame.draw.rect(self.display, color, draw_me)
            pygame.display.update()
            self.col += 20

    def updateImageArray(self, color):
        if self.col >= Screen.WIDTH:
            self.imageArray.append(list(self.temp))
            self.temp.clear()
            self.col = 0
        else:
            self.temp.append(color)
            self.col += 1