import pygame as pg


class Credit:
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        self.width, self.height = self.screen.get_size()

        # font
        self.font = pg.font.SysFont("Courier", 30, bold=True)

        self.texts = []
        data = [
            ("Sprite : Zorax, Samuel Pascall, Юлия Мартовская, ArKeid0s", -50),
            ("Maxime, Aline,", 0),
            ("Code : Aline, Maxim, Thomas, Nils", 50),
            ("Music/song:", 100),
        ]
        for content, offset in data:
            text = self.font.render(content, True, (200, 200, 200))
            rect = text.get_rect(center=(self.width // 2, self.height // 2 + offset))
            self.texts.append((text, rect))

    def draw(self):
        self.screen.fill((0, 0, 0))
        for surf, rect in self.texts:
            self.screen.blit(surf, rect)
