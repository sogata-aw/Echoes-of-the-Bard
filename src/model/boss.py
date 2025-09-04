import pygame as pg
import os

class Boss(pg.sprite.Sprite):
    def __init__(self, x, y,game, max_hp=1000, difficulte=1, base_damage=1):
        super().__init__()

        # HP
        self.BASE_DAMAGE = base_damage
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.difficulte = difficulte  # 0 facile, 1 normal, 2 moyen, 3 difficile

        self.attack_speed = 6000  #/ difficulte
        # Etats possibles : 'basic', 'hurt', 'dead'
        self.state = 'basic'
        self.game = game
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
        self.last_attack = pg.time.get_ticks()

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
            print("Boss Mort")
            self.kill()
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
            self.image = frames[self.frame_index]
        if self.state != 'dead' and now - self.last_attack >= self.attack_speed:
            self.attack(self.game.bard)
            self.last_attack = now

    def attack(self, bard):
        """Attaque le barde, lui infligeant des dégâts"""
        if self.state != 'dead':
            bard.take_damage(self.BASE_DAMAGE) #* (1 + (self.difficulte / 10)))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
