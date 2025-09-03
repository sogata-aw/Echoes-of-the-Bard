import pygame as pg
import os

class Boss(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Initialisation des frame
        self.frames = []
        for i in range(0, 4):
            img = pg.image.load(os.path.join("assets","boss","ogre", f"frame_{i}.png")).convert_alpha()
            img = pg.transform.scale_by(img, 0.5)
            self.frames.append(img)

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))

        self.animation_speed = 300  # ms
        self.last_update = pg.time.get_ticks()

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update >= self.animation_speed:
            self.last_update = now
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]

    def draw(self, surface):
        surface.blit(self.image, self.rect)
