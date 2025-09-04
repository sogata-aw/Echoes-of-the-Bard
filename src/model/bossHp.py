import pygame as pg

class BossHp(pg.sprite.Sprite):
    def __init__(self, boss):
        super().__init__()
        self.boss = boss
        self.width = boss.rect.width
        self.height = 6
        self.image = pg.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.update()

    def update(self):
        # Mettre à jour la position au-dessus du boss
        self.rect.topleft = (self.boss.rect.x, self.boss.rect.y - 10)
        # Dessiner la barre
        self.image.fill((255, 0, 0))  # fond rouge
        fill_width = int((self.boss.hp / self.boss.max_hp) * self.width)
        if fill_width > 0:
            pg.draw.rect(self.image, (0, 255, 0), (0, 0, fill_width, self.height))

        # Supprimer la barre si le boss est mort
        if self.boss.hp == 0:
            self.kill()

