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

    # Ajout sprite
    all_sprites = pg.sprite.Group()
    addSprite(game,all_sprites)

    running = True
    while running:
        dt = clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    game.bard.drinkPotion()

        # Maj de l'affichage
        all_sprites.update()
        screen.fill((30, 30, 30))
        screen.blit(game.background, (0, 0))
        all_sprites.draw(screen)
        pg.display.flip()
        clock.tick(60)
    pg.quit()

def addSprite(game,all_sprites):
    all_sprites.add(game.bard)
    all_sprites.add(game.boss)
    all_sprites.add(game.note01)
    all_sprites.add(game.note02)
    all_sprites.add(game.note03)
    all_sprites.add(game.note04)

if __name__ == "__main__":
    main()