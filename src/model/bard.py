import os

import pygame as pg
import pygame.sprite
from utilitaire import init_sprite



class Bard(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.hp = 3
        self.state = 'alive' # 'alive','invisible' ,'dead'

        # Image normale
        self.idle_image = pg.image.load(os.path.join("assets","bard","bard.png")).convert_alpha()
        self.idle_image = pg.transform.scale_by(self.idle_image, 0.7)
        self.rect = self.idle_image.get_rect(topleft=(x, y))
        self.image = self.idle_image

        # Image potion
        self.potion_image = pg.image.load(os.path.join("assets","bard","bard-potion-alt.png")).convert_alpha()
        self.potion_image = pg.transform.scale_by(self.potion_image, 0.2)

        # Animation potion
        self.drinking = False
        self.drink_timer = 0
        self.drink_duration = 20  # durée en ticks (frames)

        # Barre de vie
        self.frameHealth = init_sprite(os.path.join("assets", "frame.png"), -5, 680, (200,90))
        self.health_sprites = pygame.sprite.Group()
        self.frameHealth.add(self.health_sprites)
        print(self.frameHealth)
        print(self.frameHealth.rect)
        self.update_hp()

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
        self.update_hp()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def take_damage(self, amount):
        """Inflige des dégâts au boss"""
        if self.state != 'dead':
            if amount > self.hp:
                self.hp = 0
            else:
                self.hp -= amount
            if self.hp == 0:
                self.state = 'dead'
        self.update_hp()


    def update_hp(self):
        for sprite in self.health_sprites:
            sprite.kill()
        self.health_sprites = pygame.sprite.Group() # Réinitialisation du groupe de sprite
        self.frameHealth.add(self.health_sprites)

        for i in range(0,self.hp):
            health = init_sprite(os.path.join("assets", "heart.png"), 54 * i, 680, (75, 75))
            health.add(self.health_sprites)
