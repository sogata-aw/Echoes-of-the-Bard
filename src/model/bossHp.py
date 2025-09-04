import os.path

import pygame as pg

class BossHp(pg.sprite.Sprite):
    def __init__(self, boss):
        super().__init__()
        self.boss = boss
        self.width = boss.rect.width
        self.height = 100

        # Charger le cadre décoratif
        self.cadre = pg.image.load(os.path.join("assets","boss","ogre","hp", "bar.png")).convert_alpha()
        self.cadre = pg.transform.scale(self.cadre, (self.width, self.height))

        self.rect = self.cadre.get_rect()
        self.rect.topleft = (self.boss.rect.x, self.boss.rect.y +150)

        self.update()

    def update(self):
        # dessiner le cadre
        self.cadre.blit(self.cadre, (0, 0))
        # Dessiner la barre
        fill_width = int((self.boss.hp / self.boss.max_hp) * self.width)
        # Dessiner la barre verte (hp restant)
        if fill_width > 0:
            pg.draw.rect(self.cadre, (0, 255, 0), (10, 10, fill_width -50, self.height -50))
        # Supprimer la barre si le boss est mort
        if self.boss.hp == 0:
            self.kill()

