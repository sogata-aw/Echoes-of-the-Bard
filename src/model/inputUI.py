import pygame
import os

class InputUi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.input_group = pygame.sprite.Group()

        x_input = pygame.sprite.Sprite()
        w_input = pygame.sprite.Sprite()
        c_input = pygame.sprite.Sprite()
        v_input = pygame.sprite.Sprite()

        note_01 = pygame.sprite.Sprite()
        note_01.image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "notes", "note-01.svg")), (32,32))
        note_01.rect = note_01.image.get_rect()
        note_01.rect.topleft = (750, 725)

        note_02 = pygame.sprite.Sprite()
        note_02.image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "notes", "note-02.svg")),(32, 32))
        note_02.rect = note_02.image.get_rect()
        note_02.rect.topleft = (825, 722)

        note_03 = pygame.sprite.Sprite()
        note_03.image = pygame.image.load(os.path.join("assets", "notes", "note-03.svg"))
        note_03.rect = note_03.image.get_rect()
        note_03.rect.topleft = (885, 723)

        note_04 = pygame.sprite.Sprite()
        note_04.image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "notes", "note-04.svg")),(32, 32))
        note_04.rect = note_04.image.get_rect()
        note_04.rect.topleft = (940, 722)

        x_input.image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "letters", "X.svg")),(32, 32))
        x_input.rect = x_input.image.get_rect()
        x_input.rect.topleft = (850, 722)

        w_input.image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "letters", "W.svg")),(32, 32))
        w_input.rect = w_input.image.get_rect()
        w_input.rect.topleft = (785, 720)

        c_input.image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "letters", "C.svg")),(32, 32))
        c_input.rect = c_input.image.get_rect()
        c_input.rect.topleft = (905, 723)

        v_input.image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "letters", "V.svg")), (32,32))
        v_input.rect = v_input.image.get_rect()
        v_input.rect.topleft = (965, 720)


        w_input.add(self.input_group)
        note_01.add(self.input_group)
        x_input.add(self.input_group)
        note_02.add(self.input_group)
        c_input.add(self.input_group)
        note_03.add(self.input_group)
        v_input.add(self.input_group)
        note_04.add(self.input_group)