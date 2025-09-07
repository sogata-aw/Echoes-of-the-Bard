import os

import pygame as pg


class Menu:
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        self.selected_option = 0  # 0 = Play, 1 = Quit, 2 = Credit
        self.music_playing = False

        # --- Constantes ---
        self.ASSETS = os.path.join("assets", "menu")
        self.ASSETS_BTN = os.path.join(self.ASSETS, "buttons")
        self.TITLE_SIZE = (500, 135)
        self.TITLE_X = (self.screen.get_width() // 2 - self.TITLE_SIZE[0] // 2)
        self.TITLE_Y = 30
        self.BTN_SIZE = (300, 150)
        self.BTN_X = self.screen.get_width() // 2 - self.BTN_SIZE[0] // 2
        self.PLAY_Y = 230
        self.CREDIT_Y = 390
        self.QUIT_Y = 550

        # --- Fond ---
        menu_img = pg.image.load(os.path.join(self.ASSETS, "img_menu.jpeg"))
        # Respecter le ratio de l'image...
        screen_w, screen_h = screen.get_size()
        img_w, img_h = menu_img.get_size()
        scale_factor = max(screen_w / img_w, screen_h / img_h)
        new_w = int(img_w * scale_factor)
        new_h = int(img_h * scale_factor)
        self.background = pg.transform.scale(menu_img, (new_w, new_h))
        self.bg_rect = self.background.get_rect(center=(screen_w // 2, screen_h // 2))

        # --- Musique ---
        self.menu_sound = pg.mixer.Sound(os.path.join("sounds", "music", f"menu-song.mp3"))

        # --- Boutons ---
        self.btn_play = pg.transform.scale(pg.image.load(os.path.join(self.ASSETS_BTN, "play_button.png")),
                                           self.BTN_SIZE)
        self.btn_play_selected = pg.transform.scale(
            pg.image.load(os.path.join(self.ASSETS_BTN, "play_button_choosen.png")), self.BTN_SIZE)
        self.btn_quit = pg.transform.scale(pg.image.load(os.path.join(self.ASSETS_BTN, "quit_button.png")),
                                           self.BTN_SIZE)
        self.btn_quit_selected = pg.transform.scale(
            pg.image.load(os.path.join(self.ASSETS_BTN, "quit_button_choosen.png")), self.BTN_SIZE)
        self.btn_credit = pg.transform.scale(pg.image.load(os.path.join(self.ASSETS_BTN, "credit_button.png")),
                                             self.BTN_SIZE)
        self.btn_credit_selected = pg.transform.scale(
            pg.image.load(os.path.join(self.ASSETS_BTN, "credit_button_choosen.png")), self.BTN_SIZE)

        # --- Titre ---
        self.title = pg.transform.scale(pg.image.load(os.path.join(self.ASSETS, "title.webp")), self.TITLE_SIZE)

    def select_prev(self):
        """ selection le bouton au-dessus de l'actuel"""
        if self.selected_option != 0:
            self.selected_option -= 1

    def select_next(self):
        """ selection le bouton au-dessous de l'actuel"""
        if self.selected_option != 2:
            self.selected_option += 1

    def start_music(self):
        if not self.music_playing:
            pg.mixer.Sound.play(self.menu_sound, loops=-1)
            self.music_playing = True

    def stop_music(self):
        if self.music_playing:
            self.menu_sound.stop()
            self.music_playing = False

    def draw(self):
        """Affiche le menu à l’écran"""
        self.screen.blit(self.background, self.bg_rect)
        self.screen.blit(self.title, (self.TITLE_X, self.TITLE_Y))

        # --- Bouton Play ---
        if self.selected_option == 0:
            self.screen.blit(self.btn_play_selected, (self.BTN_X, self.PLAY_Y))
        else:
            self.screen.blit(self.btn_play, (self.BTN_X, self.PLAY_Y))

        # --- Bouton Quit ---
        if self.selected_option == 2:
            self.screen.blit(self.btn_quit_selected, (self.BTN_X, self.QUIT_Y))
        else:
            self.screen.blit(self.btn_quit, (self.BTN_X, self.QUIT_Y))

        # --- Bouton Credit ---
        if self.selected_option == 1:
            self.screen.blit(self.btn_credit_selected, (self.BTN_X, self.CREDIT_Y))
        else:
            self.screen.blit(self.btn_credit, (self.BTN_X, self.CREDIT_Y))
