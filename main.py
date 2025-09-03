#!/usr/bin/env python
import pygame as pg
import src.model.game as g

# Fonction principale : pas de varaibles globales
def main():
    pg.init()
    pg.display.set_caption("Jeux") # nom fenêtre
    screen_size = (1024, 768) # Taille écran
    screen = pg.display.set_mode(screen_size)
    clock = pg.time.Clock() # horloge
    dt = 0 # Nombre de millisecondes entre deux images

    # Instance
    game = g.Game(screen)
    running = True
    while running:
        dt = clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.blit(game.background, (0, 0))

        game.note01.update()

        game.barde.draw(screen)
        game.note01.draw(screen)

        pg.display.flip()
        clock.tick(60)
    pg.quit()

if __name__ == "__main__":
    main()