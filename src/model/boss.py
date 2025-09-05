import pygame as pg
import os

from src.model.BossEnum import BossEnum


class Boss(pg.sprite.Sprite):
    def __init__(self, x, y,game, max_hp=1000, difficulte=1, base_damage=1, type=BossEnum.ogre):
        super().__init__()

        # HP
        self.BASE_DAMAGE = base_damage
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.difficulte = difficulte  # 0 facile, 1 normal, 2 moyen, 3 difficile
        self.type = type
        self.attack_speed = 6000  #/ difficulte
        # Etats possibles : 'basic', 'hurt', 'dead'
        self.state = 'basic'
        self.game = game
        # Frames pour chaque état
        self.animations = {
            'basic': [],
            'attack': [],
            'hurt': [],
        }

        # --- Effet sonore ---
        self.attack_sound = pg.mixer.Sound(os.path.join("sounds", "sound_effect", "boss-attack.wav"))
        self.attack_sound.set_volume(0.1)

        if type == BossEnum.ogre:
            for i in range(0, 5):
                img = pg.image.load(os.path.join("assets","boss","ogre", f"frame_{i}.png")).convert_alpha()
                img = pg.transform.scale_by(img, 1.0)
                self.animations['basic'].append(img)
                self.animations['attack'].append(img)
            for i in range(0, 1):
                img = pg.image.load(os.path.join("assets", "boss", "ogre", "hurt", f"frame_{i}.png")).convert_alpha()
                img = pg.transform.scale_by(img, 1.0)
                self.animations['hurt'].append(img)

        elif type == BossEnum.mage:
            for i in range(0, 8):
                img = pg.image.load(os.path.join("assets", "boss", "mage", f"frame_{i}.png")).convert_alpha()
                img = pg.transform.scale_by(img, 2)
                self.animations['basic'].append(img)
            for i in range(0, 10):
                img = pg.image.load(os.path.join("assets", "boss", "mage", "attack", f"frame_{i}.png")).convert_alpha()
                img = pg.transform.scale_by(img, 2)
                self.animations['attack'].append(img)

            for i in range(0,2):
                img = pg.image.load(os.path.join("assets", "boss", "mage", "hurt", f"frame_{i}.png")).convert_alpha()
                img = pg.transform.scale_by(img, 2)
                self.animations['hurt'].append(img)

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
                elif self.state == 'attack':
                    # Retour à basic après hurt
                    self.state = 'basic'
                    self.frame_index = 0
            self.image = frames[self.frame_index]

            if self.frame_index == len(frames) // (2-0.5) and self.state == 'attack' and self.type==BossEnum.mage:
                self.game.spawnFireball()
                self.attack_sound.play()
                self.last_attack = now

            if self.state != 'dead' and now - self.last_attack >= self.attack_speed:
                """Attaque le barde, lui infligeant des dégâts"""
                self.state = 'attack'
                if self.type==BossEnum.ogre:
                    self.game.spawnSonicBoom()
                    self.attack_sound.play()
                    self.last_attack = now

    def draw(self, surface):
        surface.blit(self.image, self.rect)
