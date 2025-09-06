import os

import pygame

from src.utilitaire import init_sprite


class InputUi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Path
        self.NOTE = os.path.join("assets", "game", "notes")
        self.LETTERS = os.path.join("assets", "game", "letters")
        self.input_group = pygame.sprite.Group()

        note_01 = init_sprite(os.path.join(self.NOTE, "note-01.svg"), 750, 725)
        note_02 = init_sprite(os.path.join(self.NOTE, "note-02.svg"), 825, 722)
        note_03 = init_sprite(os.path.join(self.NOTE, "note-03.svg"), 885, 723)
        note_04 = init_sprite(os.path.join(self.NOTE, "note-04.svg"), 940, 722)
        bard = init_sprite(os.path.join("assets", "game", "bard", "tete-bard.png"), 600, 720, (32, int(32*298 / 258)))
        bard.image.set_alpha(51)

        w_input = init_sprite(os.path.join(self.LETTERS, "W.svg"), 785, 720)
        x_input = init_sprite(os.path.join(self.LETTERS, "X.svg"), 850, 722)
        c_input = init_sprite(os.path.join(self.LETTERS, "C.svg"), 905, 723)
        v_input = init_sprite(os.path.join(self.LETTERS, "V.svg"), 965, 720)
        space_input = init_sprite(os.path.join(self.LETTERS, "space.svg"), 640, 727, (80,26))

        bard.add(self.input_group)
        space_input.add(self.input_group)

        w_input.add(self.input_group)
        note_01.add(self.input_group)

        x_input.add(self.input_group)
        note_02.add(self.input_group)

        c_input.add(self.input_group)
        note_03.add(self.input_group)

        v_input.add(self.input_group)
        note_04.add(self.input_group)
