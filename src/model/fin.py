import pygame as pg


class Fin:
    def __init__(self, screen: pg.Surface):
        self.screen = screen

        # Police principale (tu peux mettre un .ttf dans assets/fonts/)
        font_path = pg.font.match_font("freesansbold")  # remplace par os.path.join("assets","fonts","maPolice.ttf") si tu veux une perso
        self.font = pg.font.Font(font_path, 80)   # titre principal
        self.font_secondaire = pg.font.Font(font_path, 30)  # instructions

    def update(self, game):
        # Choix du texte principal
        if game.boss.state == 'dead':
            text = self.font.render("Victoire !", True, (255, 255, 255))
        else:
            text = self.font.render("Défaite !", True, (255, 255, 255))

        # Texte secondaire
        text_secondaire = self.font_secondaire.render(
            "Appuyez sur la barre d'espace pour revenir au menu",
            True,
            (200, 200, 200)
        )

        # Efface l’écran
        self.screen.fill((30, 30, 30))

        # Centre le texte principal
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 50))
        self.screen.blit(text, text_rect)

        # Centre le texte secondaire en bas
        text2_rect = text_secondaire.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() - 80))
        self.screen.blit(text_secondaire, text2_rect)

