import os

import pygame as pg


class Fin:
    def __init__(self, screen: pg.Surface):
        self.image = None
        self.screen = screen
        self.ASSETS = os.path.join("assets", "end")
        # Police principale (tu peux mettre un .ttf dans assets/fonts/)
        font_path = pg.font.match_font("freesansbold")
        self.font = pg.font.Font(font_path, 30)  # instructions

        # text secondaire
        self.text_secondaire = self.font.render("Press the space bar to return to the level choice menu", True,
                                                (10, 10, 10))

        # --- Effet sonore ---
        self.victory_sound = pg.mixer.Sound(os.path.join("sounds", "music", "victory.mp3"))
        self.defeat_sound = pg.mixer.Sound(os.path.join("sounds", "music", "defeat.mp3"))

        # flag pour éviter de relancer en boucle
        self.sound_player = False

    def update(self, game):
        # Choix du texte principal
        if game.boss.state == 'dead':
            self.image = pg.transform.scale(pg.image.load(os.path.join(self.ASSETS, "victory.png")).convert_alpha(),
                                            (600, 300))
            game.win(True)
            if not self.sound_player:
                self.victory_sound.play(loops=0)
                self.sound_player = True
        else:
            self.image = pg.transform.scale(pg.image.load(os.path.join(self.ASSETS, "defeat.png")).convert_alpha(),
                                            (600, 300))
            game.win(False)
            if not self.sound_player:
                self.defeat_sound.play(loops=0)
                self.sound_player = True

    def draw(self):
        blured = self.blur_screen()
        self.screen.blit(blured, (0, 0))
        # Centre le texte principal
        text_rect = self.image.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 50))
        self.screen.blit(self.image, text_rect)
        # Centre le texte secondaire en bas
        text2_rect = self.text_secondaire.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() - 80))
        self.screen.blit(self.text_secondaire, text2_rect)

    def blur_screen(self):
        """floute l'écran"""
        w, h = self.screen.get_size()
        # Crée une version réduite de l'écran
        small_screen = pg.transform.smoothscale(self.screen, (int(w * 0.075), int(h * 0.075)))
        # Agrandis l'image réduite a la taille de l'écran actuelle
        blured = pg.transform.smoothscale(small_screen, (w, h))
        return blured
