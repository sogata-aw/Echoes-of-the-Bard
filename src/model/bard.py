import os

import pygame as pg

from src.utilitaire import init_sprite


class Bard(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Path
        self.ASSETS = os.path.join("assets", "game", "bard")
        self.ASSETS_HP = os.path.join(self.ASSETS, "hp")

        self.hp = 3
        self.state = 'alive'  # 'alive','invisible' ,'dead','hurt'

        # Image normale
        self.alive_image = pg.image.load(os.path.join(self.ASSETS, "bard.png")).convert_alpha()
        self.alive_image = pg.transform.scale_by(self.alive_image, 0.7)
        self.rect = self.alive_image.get_rect(topleft=(x, y))
        self.image = self.alive_image

        # Image de coup
        self.hurt_image = pg.image.load(os.path.join(self.ASSETS, "bard-hurt.png")).convert_alpha()
        self.hurt_image = pg.transform.scale_by(self.hurt_image, 0.7)

        # Animation coup
        self.hurt_timer = 0
        self.hurt_duration = 10  # durée en ticks

        # Animation invisible
        self.opacity = 51  # opacité du barde quand il est "invisible"
        self.invisible_timer = 0
        self.invisible_duration = 50  # durée en ticks (frames)
        self.last_invisible = 0  # dernière utilisation du mode invisible
        self.cd_invisible = 3000  # cooldown avant réutilisation su mode invisible

        # Groupe de Sprite de la Barre de vie
        self.health_sprites = pg.sprite.Group()
        self.update_hp()

        # --- Effet sonore ---
        self.hit_sound = pg.mixer.Sound(os.path.join("sounds", "sound_effect", "bard-hit.wav"))
        self.hit_sound.set_volume(0.1)

    def invisible(self):
        """initialise la periode d'invisibilité"""
        # Applique un cooldown
        if (pg.time.get_ticks() - self.last_invisible) > self.cd_invisible:
            self.last_invisible = pg.time.get_ticks()
            self.state = 'invisible'
            self.invisible_timer = 0
            self.image.set_alpha(self.opacity)

    def hurt(self):
        """initialise la periode avec l'animation coup"""
        self.state = 'hurt'
        self.image = self.hurt_image
        self.hit_sound.play()
        self.hurt_timer = 0

    def update(self):
        match self.state:
            case 'alive':
                if self.image == self.hurt_image:
                    self.image = self.alive_image
            case 'hurt':
                self.hurt_timer += 1
                if self.hurt_timer >= self.hurt_duration:
                    self.state = 'alive'
                    self.image = self.alive_image
            case 'invisible':
                self.invisible_timer += 1
                if self.invisible_timer >= self.invisible_duration:
                    self.state = 'alive'
                    self.image.set_alpha(255)
        self.update_hp()

    def draw(self, surface):
        # Affiche le Barde s'il est vivant
        if self.state != 'dead':
            surface.blit(self.image, self.rect)
        # Affiche la barre de vie
        self.health_sprites.draw(surface)

    def take_damage(self, amount):
        """Inflige des dégâts au barde"""
        if self.state != 'invisible':
            self.hurt()
            self.hp -= amount
            if self.hp <= 0:
                self.hp = 0
                self.state = 'dead'
                self.kill()
                self.health_sprites.empty()

    def update_hp(self):
        """Met a jour les vies du bard"""
        # Vide le groupe
        self.health_sprites.empty()
        # Ajoute le cadre
        self.health_sprites.add(init_sprite(os.path.join(self.ASSETS_HP, "frame.png"), -5, 680, (200, 90)))
        # Ajoute les cœurs
        for i in range(self.hp):
            health = init_sprite(os.path.join(self.ASSETS_HP, "heart.png"), 57 * i, 675, (75, 75))
            self.health_sprites.add(health)
