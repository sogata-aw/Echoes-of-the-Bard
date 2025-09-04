import pygame as pg
import os

class Boss(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # HP
        self.max_hp = 100
        self.hp = self.max_hp

        # Etats possibles : 'basic', 'hurt', 'dead'
        self.state = 'basic'

        # Frames pour chaque état
        self.animations = {
            'basic': [],
            'hurt': [],
            'dead': [],
        }

        for i in range(0, 5):
            img = pg.image.load(os.path.join("assets","boss","ogre", f"frame_{i}.png")).convert_alpha()
            img = pg.transform.scale_by(img, 1.0)
            self.animations['basic'].append(img)

        for i in range(0,1):
            img = pg.image.load(os.path.join("assets", "boss", "ogre", "hurt", f"frame_{i}.png")).convert_alpha()
            img = pg.transform.scale_by(img, 1.0)
            self.animations['hurt'].append(img)

        for i in range(0,1):
            img = pg.image.load(os.path.join("assets", "boss", "ogre", "hurt", f"frame_{i}.png")).convert_alpha()
            img = pg.transform.scale_by(img, 1.0)
            self.animations['dead'].append(img)

        self.frame_index = 0
        self.image = self.animations['basic'][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))

        self.animation_speed = 200
        self.last_update = pg.time.get_ticks()

    def take_damage(self, amount):
        """Inflige des dégâts au boss"""
        if amount > self.hp:
            self.hp = 0
        else:
            self.hp -= amount
        if self.hp > 0:
            self.state = 'hurt'
        else:
            self.state = 'dead'
            print("mort")
        self.frame_index = 0

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update >= self.animation_speed:
            self.last_update = now
            frames = self.animations[self.state]
            self.frame_index += 1

            # Boucle selon l'état
            if self.frame_index >= len(frames):
                if self.state == 'basic':
                    self.frame_index = 0
                elif self.state == 'hurt':
                    # Retour à basic après hurt
                    self.state = 'basic'
                    self.frame_index = 0
                # Supprimer le boss si il est mort
                elif self.state == 'dead':
                    self.frame_index = 0
                    self.kill()

            self.image = frames[self.frame_index]

    def draw(self, surface):
        surface.blit(self.image, self.rect)
