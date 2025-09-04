import pygame
import os
from utilitaire import init_sprite

class InputUi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.input_group = pygame.sprite.Group()

        note_01 = init_sprite(os.path.join("assets", "notes", "note-01.svg"), 750, 725)
        note_02 = init_sprite(os.path.join("assets", "notes", "note-02.svg"), 825, 722)
        note_03 = init_sprite(os.path.join("assets", "notes", "note-03.svg"), 885, 723)
        note_04 = init_sprite(os.path.join("assets", "notes", "note-04.svg"), 940, 722)

        w_input = init_sprite(os.path.join("assets", "letters", "W.svg"), 785, 720)
        x_input = init_sprite(os.path.join("assets", "letters", "X.svg"), 850, 722)
        c_input = init_sprite(os.path.join("assets", "letters", "C.svg"), 905, 723)
        v_input = init_sprite(os.path.join("assets", "letters", "V.svg"), 965, 720)

        w_input.add(self.input_group)
        note_01.add(self.input_group)

        x_input.add(self.input_group)
        note_02.add(self.input_group)

        c_input.add(self.input_group)
        note_03.add(self.input_group)

        v_input.add(self.input_group)
        note_04.add(self.input_group)