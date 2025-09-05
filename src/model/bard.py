import os
import pygame as pg
from utilitaire import init_sprite

class Bard(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.hp = 3
        self.state = 'alive' # 'alive','invisible' ,'dead','hurt'

        # Image normale
        self.alive_image = pg.image.load(os.path.join("assets", "bard", "bard.png")).convert_alpha()
        self.alive_image = pg.transform.scale_by(self.alive_image, 0.7)
        self.rect = self.alive_image.get_rect(topleft=(x, y))
        self.image = self.alive_image

        # Image de coup
        self.hurt_image = pg.image.load(os.path.join("assets", "bard", "bard-hurt.png")).convert_alpha()
        self.hurt_image = pg.transform.scale_by(self.hurt_image, 0.7)

        #Animation coup
        self.hurt_timer = 0
        self.hurt_duration = 10  # durée en ticks

        # Animation invisible
        self.opacity = 51 #opacité du barde quand il est "invisible"
        self.invisible_timer = 0
        self.invisible_duration = 50  # durée en ticks (frames)
        self.last_invisible = 0# dérniére uttilisation du mode invisible
        self.cd_invisible = 3000# cooldown avant réutilisation su mode invisible

        # Groupe de Sprite de la Barre de vie
        self.health_sprites = pg.sprite.Group()
        self.update_hp()

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
        self.hurt_timer = 0

    def update(self):
        match self.state:
            case 'dead':
                self.kill()
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
        # Affiche le Barde si il est vivant
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
                self.hp=0
                self.state = 'dead'

    def update_hp(self):
        """Met a jour les vies du bard"""
        # Vide le groupe
        self.health_sprites.empty()
        # Ajoute le cadre
        self.health_sprites.add(init_sprite(os.path.join("assets", "frame.png"), -5, 680, (200, 90)))
        # Ajoute les cœurs
        for i in range(self.hp):
            health = init_sprite(os.path.join("assets", "heart.png"), 54 * i, 680, (75, 75))
            self.health_sprites.add(health)