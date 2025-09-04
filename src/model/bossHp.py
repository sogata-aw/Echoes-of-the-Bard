import os.path

import pygame as pg

class BossHp(pg.sprite.Sprite):
    def __init__(self, boss):
        super().__init__()
        self.boss = boss
        self.width = boss.rect.width
        self.height = 100

        # Charger le cadre décoratif
        self.image = pg.image.load(os.path.join("assets", "boss", "ogre", "hp", "bar.png")).convert_alpha()
        self.image = pg.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.boss.rect.x - 45, self.boss.rect.y +150)

        self.update()

    def update(self):
        # dessiner le cadre
        self.image.blit(self.image, (0, 0))
        # Dessiner la barre
        fill_width = int((self.boss.hp / self.boss.max_hp) * self.width)
        # Dessiner la barre verte (hp restant)
        if fill_width > 0:
            pg.draw.rect(self.image, (0, 255, 0), (120, 36, fill_width - 165, 29))
        # Supprimer la barre si le boss est mort
        if self.boss.hp == 0:
            self.kill()

