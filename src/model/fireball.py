import os
import pygame as pg

class Fireball(pg.sprite.Sprite):
    def __init__(self, boss, bard):
        super().__init__()

        #Image Boule de feu
        self.image = pg.image.load(os.path.join("assets", "boss", "ogre", "fireball.png")).convert_alpha()
        self.image = pg.transform.scale_by(self.image, 1)
        self.rect = self.image.get_rect(topleft=boss.rect.center)

        # Déplacement
        self.pos = pg.math.Vector2(boss.rect.center)# position de la boule de feu
        self.target = pg.math.Vector2(bard.rect.center)# cible
        self.speed = 5  # pixels par frame

    def update(self):
        # Calcul de la direction
        direction = self.target - self.pos
        if direction.length() > 0:  # éviter division par zéro
            direction = direction.normalize()  # vecteur de direction unitaire
            self.pos += direction * self.speed  # avance vers la cible

            # Option : stop net quand on atteint ou dépasse la cible
            if self.pos.distance_to(self.target) < self.speed:
                self.kill()

            # Mise à jour de la position du rect
            self.rect.center = (round(self.pos.x), round(self.pos.y))
    def draw(self, surface):
        surface.blit(self.image, self.rect)
