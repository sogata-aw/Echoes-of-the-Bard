import pygame as pg


class Credit:
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        self.width, self.height = self.screen.get_size()

        # font
        self.title_font = pg.font.SysFont("Georgia", 40, bold=True)
        self.text_font = pg.font.SysFont("Courier", 28, bold=True)

        self.data = [
            ("Code", self.title_font, (238, 195, 154)),
            ("Aline Rostagnat, Maxime Rastelli,", self.text_font, (220, 220, 220)),
            ("Nils Rayot, Thomas Reymond", self.text_font, (220, 220, 220)),
            ("", self.text_font, (220, 220, 220)),

            ("Visuals", self.title_font, (238, 195, 154)),
            ("Background images: Cupid.Cloud0 0, ChatGPT", self.text_font, (220, 220, 220)),
            ("Sprites: Aline Rostagnat, Maxime Rastelli,", self.text_font, (220, 220, 220)),
            ("ArKeid0s, indiedb.com, Юлия Мартовская", self.text_font, (220, 220, 220)),
            ("", self.text_font, (220, 220, 220)),

            ("Sound", self.title_font, (238, 195, 154)),
            ("Music: ljB0, uppbeat.io", self.text_font, (220, 220, 220)),
            ("Sound effects: deercowboy.com,", self.text_font, (220, 220, 220)),
            ("u_3bsnvt0dsu, floraphonic", self.text_font, (220, 220, 220)),


        ]

        self.texts = []
        total_height = len(self.data) * 50
        start_y = self.height // 2 - total_height // 2

        y = start_y
        for content, font, color in self.data:
            text = font.render(content, True, color)
            rect = text.get_rect(center=(self.width // 2, y))
            self.texts.append((text, rect))
            y += 50

    def draw(self):
        self.screen.fill((0, 0, 0))
        for surf, rect in self.texts:
            self.screen.blit(surf, rect)
