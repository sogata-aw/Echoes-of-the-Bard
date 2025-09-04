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
        self.rect.topleft = (self.boss.rect.x - 45, self.boss.rect.y - 75)

        self.update()

    def update(self):
        # Supprimer la barre si le boss est mort
        if self.boss.hp == 0:
            self.kill()

    def draw(self):
        pg.draw.rect(self.image, (76, 69, 103), (120, 36, 507, 29))
        # dessiner le cadre
        self.image.blit(self.image, (0, 0))
        # Dessiner la barre
        fill_width = int((self.boss.hp / self.boss.max_hp) * 507)
        # Dessiner la barre verte (hp restant)
        pg.draw.rect(self.image, (0, 255, 0), (120, 36, fill_width, 29))

        if self.boss.hp == 0:
            self.kill()

