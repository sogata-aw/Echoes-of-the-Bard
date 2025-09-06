import os

import pygame as pg


class SonicBoom(pg.sprite.Sprite):
    def __init__(self, boss, bard):
        super().__init__()
        self.animations = []
        self.bard = bard

        self.frame_index = 0
        for i in range(0, 15):
            img = pg.image.load(
                os.path.join("assets", "game", "boss", "ogre", "sonic_boom", f"sonic_boom_{i}.png")).convert_alpha()
            img = pg.transform.scale_by(img, 8.0)
            self.animations.append(img)

        self.image = self.animations[self.frame_index]
        # self.image = pg.transform.scale_by(self.image, 1)
        self.rect = self.image.get_rect(topleft=boss.rect.center)
        # Déplacement
        self.pos = pg.math.Vector2(boss.rect.center)  # position de la boule de feu
        self.target = pg.math.Vector2(bard.rect.center)  # cible
        self.speed = 6  # pixels par frame

        self.animation_speed = 150  # ms entre les frames
        self.last_update = pg.time.get_ticks()

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update >= self.animation_speed:
            self.last_update = now
            self.frame_index += 1
            # Boucle selon l'état
            if self.frame_index >= len(self.animations):
                self.frame_index = 0
            self.image = self.animations[self.frame_index]
        # Calcul de la direction
        direction = self.target - self.pos
        if direction.length() > 0:  # éviter division par zéro
            direction = direction.normalize()  # vecteur de direction unitaire
            self.pos += direction * self.speed  # avance vers la cible

            # Option : stop net quand on atteint ou dépasse la cible
            if self.pos.distance_to(self.target) < self.speed:
                self.kill()
                self.bard.take_damage(1)  # Inflige des dégâts au barde

            # Mise à jour de la position du rect
            self.rect.center = (round(self.pos.x), round(self.pos.y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
