import pygame as pg
from src.model.bard import Bard
from src.model.boss import Boss
from src.model.note import Note


class Game:
    def __init__(self, screen: pg.Surface):
        self.screen = screen

        # background
        self.background = pg.Surface(self.screen.get_size())
        self.background = pg.image.load("assets/menu_image.jpg")
        self.background = pg.transform.scale(self.background, screen.get_size())
        self.screen.blit(self.background, (0, 0))
        self.bard = Bard(y=500,x=100)
        self.note01 = Note(x=200,y=200,type=1)
        self.note02 = Note(x=300,y=300, type=2)
        self.note03 = Note(x=400, y=400, type=3)
        self.note04 = Note(x=500, y=500, type=4)
        self.boss = Boss(y=350,x=650)

        self.isEnded = False
