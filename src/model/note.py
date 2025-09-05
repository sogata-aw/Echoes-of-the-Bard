import os
import pygame as pg

class Note(pg.sprite.Sprite):
    def __init__(self,x,y,type, key):
        super().__init__()
        self.type = type
        # Images normales
        self.image = pg.transform.scale(pg.image.load(os.path.join("assets","notes", f"note-0{type}.svg")).convert_alpha(), (100, 100))

        # Image "gold"
        self.image_gold = pg.transform.scale(pg.image.load(os.path.join("assets", "notes", f"note-0{type}-golden.svg")).convert_alpha(), (100, 100))
        if type == 3:
            self.image = pg.transform.scale_by(self.image, 1.2)
            self.image_gold = pg.transform.scale_by(self.image_gold, 1.2)

        self.base_img = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Son
        self.note_sound = pg.mixer.Sound(os.path.join("sounds", "sound_effect", f"note_sound.wav"))

        # Animation
        self.start_time = pg.time.get_ticks() #temps où la note est créée
        self.duration = 1000 #ms
        self.perfect_start = None
        self.alive = True
        self.state = 0

        self.key = key
        # Démarrer à 20% d'opacité
        self.image.set_alpha(int(0.2 * 255))


    def update(self):
        now = pg.time.get_ticks()

        # Cas : déjà en mode "gold"
        if self.perfect_start is not None:
            if now - self.perfect_start > 250:
                self.alive = False
                self.kill()
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
        if 20 <= percent <= 70:
            self.state = 1
        elif 71 <= percent <= 95:
            self.state = 2
        elif 96 <= percent <= 100:
            self.state = 3

    def hit(self) -> int:
        degats = 0
        if not self.alive:
            return degats
        match self.state:
            case 1:
                pg.mixer.Sound.play(self.note_sound)
                degats = 1
            case 2:
                pg.mixer.Sound.play(self.note_sound)
                degats = 5
            case 3:
                pg.mixer.Sound.play(self.note_sound)
                degats = 10
        self.alive = False
        self.kill()
        return degats

    def draw(self, surface):
        if self.alive:
            surface.blit(self.image, self.rect)