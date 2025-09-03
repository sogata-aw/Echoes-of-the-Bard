import pygame as pg

class Bard(pg.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.pv = 100
        self.image = pg.image.load("assets/Bard-front.png").convert_alpha()
        self.image = pg.transform.scale_by(self.image, 0.2)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)