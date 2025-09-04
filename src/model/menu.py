import pygame as pg

class Menu:
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        self.selected_option = 0  # 0 = Play, 1 = Quit

        # --- Constantes ---
        self.BTN_SIZE = (800, 400)
        self.BTN_X = self.screen.get_width() // 2 - self.BTN_SIZE[0] // 2
        self.PLAY_Y = 130
        self.QUIT_Y = 230

        # --- Fond ---
        menu_img = pg.image.load("assets/menu_image.jpg")
        self.background = pg.transform.scale(menu_img, screen.get_size())

        # --- Boutons ---
        self.btn_play = pg.transform.scale(pg.image.load("assets/buttons/play_button.png"), self.BTN_SIZE)
        self.btn_play_selected = pg.transform.scale(pg.image.load("assets/buttons/play_button_choosen.png"), self.BTN_SIZE)
        self.btn_quit = pg.transform.scale(pg.image.load("assets/buttons/quit_button.png"), self.BTN_SIZE)
        self.btn_quit_selected = pg.transform.scale(pg.image.load("assets/buttons/quit_button_choosen.png"), self.BTN_SIZE)

    def update(self):
        """Affiche le menu à l’écran"""
        self.screen.blit(self.background, (0, 0))

        # --- Bouton Play ---
        if self.selected_option == 0:
            self.screen.blit(self.btn_play_selected, (self.BTN_X, self.PLAY_Y))
        else:
            self.screen.blit(self.btn_play, (self.BTN_X, self.PLAY_Y))

        # --- Bouton Quit ---
        if self.selected_option == 1:
            self.screen.blit(self.btn_quit_selected, (self.BTN_X, self.QUIT_Y))
        else:
            self.screen.blit(self.btn_quit, (self.BTN_X, self.QUIT_Y))
