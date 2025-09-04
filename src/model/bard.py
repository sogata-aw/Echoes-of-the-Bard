import os
import pygame as pg
from utilitaire import init_sprite

class Bard(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.hp = 3
        self.state = 'alive' # 'alive','invisible' ,'dead'

        # Image normale
        self.alive_image = pg.image.load(os.path.join("assets", "bard", "bard.png")).convert_alpha()
        self.alive_image = pg.transform.scale_by(self.alive_image, 0.7)
        self.rect = self.alive_image.get_rect(topleft=(x, y))
        self.image = self.alive_image

        # Animation invisible
        self.opacity = 51 #opacité du barde quand il est "invisible"
        self.invisible_timer = 0
        self.invisible_duration = 20  # durée en ticks (frames)

        # Groupe de Sprite de la Barre de vie
        self.health_sprites = pg.sprite.Group()
        self.update_hp()

    def invisible(self):
        """ fait devenir le barde invisible et invulnerable pour un temp"""
        print("invisible")
        self.state = 'invisible'
        self.invisible_timer = 0
        self.image.set_alpha(self.opacity)

    def update(self):
        if self.state == 'invisible':
            print(f"invible depuis {self.invisible_timer}")
            self.invisible_timer += 1
            if self.invisible_timer >= self.invisible_duration:
                self.state = 'alive'
                self.image.set_alpha(255)
        self.update_hp()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.health_sprites.draw(surface)

    def take_damage(self, amount):
        """Inflige des dégâts au barde"""
        if self.state != 'invisible':
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