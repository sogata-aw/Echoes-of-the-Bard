#!/usr/bin/env python
import pygame as pg

class Game:
    def __init__(self, screen: pg.Surface):
        self.screen = screen

        # background
        self.background = pg.Surface(self.screen.get_size())
        self.background = pg.image.load("assets/menu_image.jpg")
        self.background = pg.transform.scale(self.background, screen.get_size())
        self.screen.blit(self.background, (0, 0))

        self.isEnded = False

# Fonction principale : pas de varaibles globales
def main():
    pg.init()
    pg.display.set_caption("Jeux") # nom fenêtre
    screenSize = (1024, 768) # Taille écran
    screen = pg.display.set_mode(screenSize)
    clock = pg.time.Clock() # horloge
    dt = 0 # Nombre de millisecondes entre deux images

    # Instance
    game = Game(screen)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        pg.display.update()
    pg.quit()

if __name__ == "__main__":
    main()