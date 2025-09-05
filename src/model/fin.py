import pygame as pg


class Fin:
    def __init__(self, screen: pg.Surface):
        self.screen = screen

        # Police principale (tu peux mettre un .ttf dans assets/fonts/)
        font_path = pg.font.match_font("freesansbold")  # remplace par os.path.join("assets","fonts","maPolice.ttf") si tu veux une perso
        self.font = pg.font.Font(font_path, 80)   # titre principal
        self.font_secondaire = pg.font.Font(font_path, 30)  # instructions

        # text secondaire
        self.text_secondaire = self.font_secondaire.render("Appuyez sur la barre d'espace pour revenir au menu", True,
                                                      (200, 200, 200))
        self.text = text = self.font.render("", True, (255, 255, 255))
    def update(self, game):
        # Choix du texte principal
        if game.boss.state == 'dead':
            self.text = self.font.render("Victoire !", True, (255, 255, 255))
        else:
            self.text = self.font.render("Défaite !", True, (255, 255, 255))

    def draw(self):
        # Efface l’écran
        self.screen.fill((0, 0, 0))
        # Centre le texte principal
        text_rect = self.text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 50))
        self.screen.blit(self.text, text_rect)
        # Centre le texte secondaire en bas
        text2_rect = self.text_secondaire.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() - 80))
        self.screen.blit(self.text_secondaire, text2_rect)


