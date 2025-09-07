import os
import pygame
from src.utilitaire import init_sprite


class Explanation(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()

        # Dimensions écran
        self.screen = screen
        self.screen_w = screen.get_width()
        self.screen_h = screen.get_height()

        # Paths
        self.NOTE = os.path.join("assets", "game", "notes")
        self.LETTERS = os.path.join("assets", "game", "letters")
        self.input_group = pygame.sprite.Group()

        # --- Bloc 1 : attaque (notes + touches) ---
        spacing = 90
        base_y_attack = self.screen_h // 3  # 1/3 hauteur écran

        keys = ["j.png", "k.png", "l.png", "m.png"]
        notes = ["note-01.svg", "note-02.svg", "note-03.svg", "note-04.svg"]

        start_x = self.screen_w // 2 - ((len(keys) - 1) * spacing // 2)

        for i, (k, n) in enumerate(zip(keys, notes)):
            key_sprite = init_sprite(os.path.join(self.LETTERS, k), start_x + i * spacing, base_y_attack, (40,40) )
            note_sprite = init_sprite(os.path.join(self.NOTE, n), start_x + i * spacing, base_y_attack+ 50, (60,60))
            key_sprite.add(self.input_group)
            note_sprite.add(self.input_group)

        # --- Bloc 2 : esquive (barde + espace) ---
        base_y_avoid = 2 * self.screen_h // 3  # 2/3 hauteur écran

        bard = init_sprite(
            os.path.join("assets", "game", "bard", "tete-bard.png"),
            self.screen_w // 2 - 130, base_y_avoid + 50,
            (64, int(64 * 298 / 258))
        )
        bard.image.set_alpha(51)

        space_input = init_sprite(
            os.path.join(self.LETTERS, "space.svg"),
            self.screen_w // 2 - 50, base_y_avoid + 50,
            (180, 60)
        )

        bard.add(self.input_group)
        space_input.add(self.input_group)

        # --- Texte ---
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 40, bold=True)

        # Textes blocs
        self.text_attack = self.font.render(
            "Attack the boss in time with your music", True, (255, 255, 255)
        )
        self.text_avoid = self.font.render(
            "Avoid the boss's projectiles by becoming invisible", True, (255, 255, 255)
        )

        # Position des textes (centrés)
        self.text_attack_rect = self.text_attack.get_rect(center=(self.screen_w // 2, base_y_attack - 40))
        self.text_avoid_rect = self.text_avoid.get_rect(center=(self.screen_w // 2, base_y_avoid - 40))

    def draw(self):
        # Texte
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.text_attack, self.text_attack_rect)
        self.screen.blit(self.text_avoid, self.text_avoid_rect)

        # Sprites
        self.input_group.draw(self.screen)