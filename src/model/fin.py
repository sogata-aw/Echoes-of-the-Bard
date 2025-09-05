import os

import pygame as pg


class Fin:
    def __init__(self, screen: pg.Surface):
        self.image = None
        self.screen = screen

        # Police principale (tu peux mettre un .ttf dans assets/fonts/)
        font_path = pg.font.match_font("freesansbold")  # remplace par os.path.join("assets","fonts","maPolice.ttf") si tu veux une perso
        self.font= pg.font.Font(font_path, 30)  # instructions

        # text secondaire
        self.text_secondaire = self.font.render("Appuyez sur la barre d'espace pour revenir au menu", True,(200, 200, 200))

    def update(self, game):
        # Choix du texte principal
        if game.boss.state == 'dead':
            self.image = pg.image.load(os.path.join("assets","victoire.png")).convert_alpha()
        else:
            self.image = pg.image.load(os.path.join("assets", "defaite.png")).convert_alpha()

    def draw(self):
        # Efface l’écran
        self.screen.fill((0, 0, 0))
        # Centre le texte principal
        text_rect = self.image.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 50))
        self.screen.blit(self.image, text_rect)
        # Centre le texte secondaire en bas
        text2_rect = self.text_secondaire.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() - 80))
        self.screen.blit(self.text_secondaire, text2_rect)


