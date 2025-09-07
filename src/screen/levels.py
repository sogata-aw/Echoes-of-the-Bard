import os

import pygame as pg


class Levels:
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        self.selected_level =1

        # Background avec proportion
        levels_img = pg.image.load(os.path.join("assets","menu", "level_choices.jpg"))
        screen_w, screen_h = screen.get_size()
        img_w, img_h = levels_img.get_size()
        scale_factor = max(screen_w / img_w, screen_h / img_h)
        new_w = int(img_w * scale_factor)
        new_h = int(img_h * scale_factor)
        self.background = pg.transform.scale(levels_img, (new_w, new_h))

        # --- Level 1 ---
        level1 = pg.image.load(os.path.join("assets","menu","buttons","level1.png"))
        self.level1 = pg.transform.scale_by(level1, 0.17)
        self.rect1 = level1.get_rect()
        self.rect1.center = (830, 1020)
        self.level1_selected = pg.transform.scale_by(level1, 0.21)

        # --- Level 2 ---
        level2 = pg.image.load(os.path.join("assets","menu","buttons","level2.png"))
        self.rect2 = level2.get_rect()
        self.rect2.center = (500,500)
        self.level2 = pg.transform.scale_by(level2, 0.17)
        self.level2_selected = pg.transform.scale_by(level2, 0.21)

    def draw(self):
        pos_level1=(370, 555)
        pos_level2=(250,300)
        self.screen.blit(self.background, (0, 0))
        if self.selected_level == 1:
            self.screen.blit(self.level1_selected, (pos_level1[0]-20,pos_level1[1]-20) )
            self.screen.blit(self.level2, pos_level2)
        elif self.selected_level == 2:
            self.screen.blit(self.level1, pos_level1)
            self.screen.blit(self.level2_selected, (pos_level2[0]-20,pos_level2[1]-20) )
