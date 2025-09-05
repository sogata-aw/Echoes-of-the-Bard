import pygame as pg

class Credit:
    def __init__(self, screen: pg.Surface):
        self.screen = screen

    def draw(self):
        self.screen.fill((0, 0, 0))