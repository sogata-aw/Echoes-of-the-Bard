import pygame as pg
from src.model.bard import Bard
from src.model.note import Note


class Game:
    def __init__(self, screen: pg.Surface):
        self.screen = screen

        # background
        self.background = pg.Surface(self.screen.get_size())
        self.background = pg.image.load("assets/menu_image.jpg")
        self.background = pg.transform.scale(self.background, screen.get_size())
        self.screen.blit(self.background, (0, 0))
        self.barde = Bard(y=100,x=100)
        self.note01 = Note(x=300,y=300,type=1)

        self.isEnded = False
