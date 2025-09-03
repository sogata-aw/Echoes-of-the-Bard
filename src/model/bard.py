import pygame as pg

class Bard(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.pv = 100

        # Image normale
        self.idle_image = pg.image.load("assets/bard/bard-front.png").convert_alpha()
        self.idle_image = pg.transform.scale_by(self.idle_image, 0.2)
        self.rect = self.idle_image.get_rect(topleft=(x, y))
        self.image = self.idle_image

        # Image potion
        self.potion_image = pg.image.load("assets/bard/bard-potion-alt.png").convert_alpha()
        self.potion_image = pg.transform.scale_by(self.potion_image, 0.2)

        # Animation potion
        self.drinking = False
        self.drink_timer = 0
        self.drink_duration = 20  # durée en ticks (frames)

    def drinkPotion(self):
        self.drinking = True
        self.drink_timer = 0
        self.image = self.potion_image

    def update(self):
        if self.drinking:
            self.drink_timer += 1
            if self.drink_timer >= self.drink_duration:
                self.drinking = False
                self.image = self.idle_image

    def draw(self, surface):
        surface.blit(self.image, self.rect)
