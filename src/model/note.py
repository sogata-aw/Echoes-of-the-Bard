import os
import pygame as pg

class Note(pg.sprite.Sprite):
    def __init__(self,x,y,type):
        super().__init__()
        self.type = type
        # Images normales
        self.image = pg.transform.scale(pg.image.load(os.path.join("assets","notes", f"note-0{type}.svg")).convert_alpha(), (100, 100))
        self.base_img = self.image.copy()

        # Image "gold"
        self.image_gold = pg.transform.scale(pg.image.load(os.path.join("assets", "notes", f"note-0{type}-golden.svg")).convert_alpha(), (100, 100))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Animation
        self.start_time = pg.time.get_ticks() #temps où la note est créée
        self.duration = 2000 #ms
        self.perfect_start = None
        self.alive = True
        self.state = 0
        # Démarrer à 20% d'opacité
        self.image.set_alpha(int(0.2 * 255))


    def update(self):
        now = pg.time.get_ticks()

        # Cas : déjà en mode "gold"
        if self.perfect_start is not None:
            if now -self.perfect_start > 250:
                self.alive = False
            return

        cooldown = now - self.start_time
        if cooldown > self.duration:
            # Faire disparaitre la note
            self.image = self.image_gold.copy()
            self.perfect_start = now
            return

        progress = max(0.0, min(1.0, cooldown / self.duration))
        # La note apparait à 20% d'opacité (environ 51/255)
        opacity = int(51 + (204 * progress)) #255-51=204

        self.image = self.base_img.copy()
        self.image.set_alpha(opacity)

        #Màj de la state
        percent = opacity * 100 / 255
        if 20 <= percent <= 45:
            self.state = 1
        elif 46 <= percent <= 95:
            self.state = 2
        elif 96 <= percent <= 100:
            self.state = 3

    def draw(self, surface):
        if self.alive:
            surface.blit(self.image, self.rect)