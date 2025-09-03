import pygame as pg
from src.model.bard import Bard
class Game:
    def __init__(self, screen: pg.Surface):
        self.screen = screen

        # background
        self.background = pg.Surface(self.screen.get_size())
        self.background = pg.image.load("assets/menu_image.jpg")
        self.background = pg.transform.scale(self.background, screen.get_size())
        self.screen.blit(self.background, (0, 0))
        self.barde = Bard(y=100,x=100)
        self.isEnded = False
