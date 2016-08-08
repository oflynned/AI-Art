import pygame

SCREEN_X = 50
SCREEN_Y = 50
WHITE = (255, 255, 255)

class DisplayScreen(object):

    def __init__(self):
        self.display = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        self.square = pygame.Surface((SCREEN_X, SCREEN_Y))
        self.display.fill(WHITE)