import random

import os

import pygame as pg
from src.model.bard import Bard
from src.model.boss import Boss
from src.model.bossHp import BossHp

from src.model.note import Note


class Game:
    def __init__(self, screen: pg.Surface):
        self.screen = screen

        # background
        self.background = pg.Surface(self.screen.get_size())
        self.background = pg.image.load(os.path.join("assets","menu_image.jpg"))
        self.background = pg.transform.scale(self.background, screen.get_size())
        self.screen.blit(self.background, (0, 0))

        self.degatsTot=0

        self.bard = Bard(y=100,x=100)
        self.notesPos = [(200, 300), (300, 250), (400, 320), (500, 380)]
        self.keys = [pg.K_w, pg.K_x, pg.K_c, pg.K_v]

        # Difficulté
        # TODO à changer en fonction de la difficulté du boss
        # if easy
        self.min_delay, self.max_delay = 5000, 7000 #ms
        # if normal (2000,3500)
        # if normal (1000,2000)

        # Notes actives
        self.notes = [None, None, None, None]
        self.next_ready = [0, 0, 0, 0]

        now = pg.time.get_ticks()

        first_slot = random.randint(0,3)
        self.spawn_in_slot(first_slot)

        # On démarre le timer
        i = 0
        while i < 4:
            self.arm_timer(i, now)
            i+=1
        self.boss = Boss(y=350,x=650)
        self.bosshp = BossHp(self.boss)
        self.isEnded = False

    def active_types(self):
        # Retourne les types de note déjà utilisés par les notes actives
        types = []
        i = 0
        while i < 4:
            n = self.notes[i]
            if n is not None and n.alive:
                types.append(n.type)
            i += 1
        return types

    def choose_type(self):
        used = self.active_types()
        possible = []
        t = 1
        while t <=4:
            if t not in used:
                possible.append(t)
            t +=1
        if len(possible) == 0:
            return None
        return random.choice(possible)

    def arm_timer(self, slot, base_time=None):
        if base_time is None:
            base_time = pg.time.get_ticks()
        delay = random.randint(self.min_delay, self.max_delay)
        self.next_ready[slot] = base_time + delay

    def spawn_in_slot(self, slot):
        # pas de spawn si note déjà là
        if self.notes[slot] is not None and self.notes[slot].alive:
            return False
        # pas deux notes du même type en même temps
        note_type = self.choose_type()
        if note_type is None:
            return False
        pos = self.notesPos[slot]
        key = self.keys[slot]
        self.notes[slot] = Note(pos[0], pos[1], note_type,key)
        # On arme le prochain timer de ce slot
        self.arm_timer(slot)
        return True

    def update(self, listSprite):
        if self.degatsTot >= 100: # TODO à changer en fonction des pv du boss
            self.isEnded = True
            return

        # 1) Update des notes existantes et nettoyage
        i = 0
        while i < 4:
            n = self.notes[i]
            if n is not None:
                if n.alive:
                    listSprite.add(n)
                else:
                    self.notes[i] = None
            i += 1

        # 2) Spawns différés : au plus UN spawn par frame
        now = pg.time.get_ticks()
        spawned_this_frame = False

        order = [0, 1, 2, 3]
        random.shuffle(order)

        k = 0
        while k < 4:
            i = order[k]
            # slot vide et timer prêt
            if not spawned_this_frame:
                if self.notes[i] is None:
                    if self.next_ready[i] != 0 and now >= self.next_ready[i]:
                        if self.spawn_in_slot(i):
                            spawned_this_frame = True
            k += 1
        listSprite.update()


    def draw(self):
        self.screen.blit(self.background, (0,0))
        self.barde.draw(self.screen)

        i = 0
        while i < 4:
            n = self.notes[i]
            if n is not None:
                n.draw(self.screen)
            i += 1

        print(self.degatsTot)

    def handle_key(self, key):
        for note in self.notes:
            if note is not None and note.key == key and note.alive:
                self.degatsTot += note.hit()
                print ("Score total:"+str(self.degatsTot))