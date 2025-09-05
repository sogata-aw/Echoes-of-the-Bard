import random
import os
import pygame as pg
from src.model.bard import Bard
from src.model.boss import Boss
from src.model.sonicBoom import SonicBoom
from src.model.inputUI import InputUi
from src.model.bossHp import BossHp
from src.model.note import Note


class Game:
    def __init__(self, screen: pg.Surface, listeSprite: pg.sprite.Group, bossType):
        self.screen = screen
        self.listeSprite = listeSprite
        background = pg.image.load(os.path.join("assets","combat_ogre_image.jpg"))
        self.background = pg.transform.scale(background, screen.get_size())


        self.boss = Boss(x=400, y=100, game=self, max_hp=100, difficulte=1, base_damage=1, type=bossType)
        self.bosshp = BossHp(self.boss)

        self.bard = Bard(x=30, y=400)
        self.inputUi = InputUi()
        self.notesPos = [(120, 250), (230, 250), (340, 290), (420, 380)]
        self.type_to_keys = {1:pg.K_w, 2:pg.K_x, 3:pg.K_c, 4:pg.K_v}
        # Difficulté
        # TODO à changer en fonction de la difficulté du boss
        # if easy
        self.min_delay, self.max_delay = 1500, 2000 #ms
        # if normal (2000,3500)
        # if normal (1000,2000)

        # --- Musique ---
        pg.mixer.music.load(os.path.join("sounds", "music", f"battle-song.mp3"))
        pg.mixer.music.play(-1)

        # --- Effet sonore ---
        self.hit_sound = pg.mixer.Sound(os.path.join("sounds", "sound_effect", "note01.mp3"))
        self.hit_sound.set_volume(0.3)
        # Notes actives
        self.notes = [None, None, None, None]
        self.compteur = 0
        self.next_spawn = 0
        self.arm_global_timer()

    def isfinish(self):
        """Indique si la partie est finie"""
        if self.bard.state == 'dead' or self.boss.state == 'dead':
            return True
        else:
            return False
    def spawnSonicBoom(self):
        """fait apparaitre une onde sonore qui vas du boss au barde"""
        sonic = SonicBoom(self.boss, self.bard)
        self.listeSprite.add(sonic)

    # --- Fonction d'update et de Draw ---
    def update(self, listSprite):
        # Update des notes existantes et nettoyage
        i = 0
        while i < 4:
            note = self.notes[i]
            if note is not None:
                if note.alive:
                    listSprite.add(note)
                else:
                    self.notes[i] = None
            i += 1
        # Spawns différés : au plus UN spawn par frame
        now = pg.time.get_ticks()
        if now >= self.next_spawn:
            if self.spawn_note():
                self.arm_global_timer()
        # Update des autre sprite
        listSprite.update()

    def draw(self, listSprite):
        self.screen.fill((0, 0, 0)) # Remise a zero
        self.bosshp.draw()
        self.screen.blit(self.background, (0, 0))
        listSprite.draw(self.screen)
        self.bard.draw(self.screen)

    # --- Key Handler ---
    def handle_key(self, key):
        for note in self.notes:
            if note is not None and note.key == key and note.alive:
                self.boss.take_damage(note.hit())
                self.bosshp.draw()
                self.compteur +=1

                self.hit_sound.play()

    # --- Gestion des Notes ---
    def spawn_note(self):
        # pas deux notes du même type en même temps
        note_type = self.choose_type()
        if note_type is None:
            return False

        empty_slots = []
        i = 0
        while i < 4:
            if self.notes[i] is None or not self.notes[i].alive:
                empty_slots.append(i)
            i += 1
        if not empty_slots:
            return False

        slot = random.choice(empty_slots)
        pos = self.notesPos[slot]
        key = self.type_to_keys[note_type]
        self.notes[slot] = Note(pos[0], pos[1], note_type,key)
        return True

    def arm_global_timer(self):
        """Planifie le prochain spawn global"""
        delay = random.randint(self.min_delay, self.max_delay)
        self.next_spawn = pg.time.get_ticks() + delay

    def choose_type(self):
        """Choisit un type de note libre"""
        used = self.active_types()
        possible = []
        t = 1
        while t <=4:
            if t not in used:
                possible.append(t)
            t +=1
        if not possible:
            return None
        return random.choice(possible)

    def active_types(self):
        """Retourne les types de note déjà utilisés par les notes actives"""
        types = []
        for n in self.notes:
            if n is not None and n.alive:
                types.append(n.type)
        return types