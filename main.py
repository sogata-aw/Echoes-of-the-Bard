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
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    game.bard.drinkPotion()
                if event.key == pg.K_DOWN:
                    game.boss.take_damage(10)
                if event.key == pg.K_b: # Pour tester les degat au barde
                    game.bard.take_damage(1)
                if event.key == pg.K_F11:
                    pg.display.toggle_fullscreen()
                if event.key == pg.K_ESCAPE:
                    running = False
                else:
                    game.handle_key(event.key)

        game.update(all_sprites)
        screen.fill((30, 30, 30))
        screen.blit(game.background, (0, 0))
        all_sprites.draw(screen)
        game.bard.draw(screen)
        pg.display.flip()
        clock.tick(60)
    pg.quit()

def addSprite(game,all_sprites):
    all_sprites.add(game.boss)
    all_sprites.add(game.bosshp)
    all_sprites.add(game.bard)
    all_sprites.add(game.inputUi.input_group)
if __name__ == "__main__":
    main()