 #!/usr/bin/env python
import pygame as pg
import src.model.game as g
import src.model.menu as m
import src.model.fin as f
from src.model.stateEnum import StateEnum

def main():
    pg.init()
    pg.display.set_caption("Jeux") # nom fenêtre
    screen_size = (1024, 768) # Taille écran
    screen = pg.display.set_mode(screen_size)
    clock = pg.time.Clock() # horloge
    dt = 0 # Nombre de millisecondes entre deux images

    # Etat
    game_state = StateEnum.in_menu
    # Instance
    game = g.Game(screen)
    menu = m.Menu(screen)
    fin = f.Fin(screen)

    # Ajout sprite
    all_sprites = pg.sprite.Group()
    addSprite(game,all_sprites)

    while game_state != StateEnum.closing:
        while game_state == StateEnum.playing:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_state = StateEnum.closing
                if event.type == pg.KEYDOWN:
                    match event.key:
                        case pg.K_SPACE:
                            game.bard.invisible()
                        case pg.K_DOWN:
                            game.boss.take_damage(10) #Pour tester les degat au boss
                        case pg.K_b:
                            game.bard.take_damage(1)# Pour tester les degat au barde
                        case pg.K_F11:
                            pg.display.toggle_fullscreen()
                        case pg.K_ESCAPE:
                            game_state = StateEnum.in_menu
                        case _:
                            game.handle_key(event.key)
            game.update(all_sprites)
            screen.fill((0, 0, 0))
            screen.blit(game.background, (0, 0))
            all_sprites.draw(screen)
            game.bard.draw(screen)
            pg.display.flip()
            clock.tick(60)
            if game.bard.state == 'dead' or game.boss.state == 'dead':
                game_state = StateEnum.finished

        while game_state != StateEnum.closing and game_state == StateEnum.in_menu:
            for event in pg.event.get():
                # QUIT signifie que l'utilisateur a fermé la fenêtre
                if event.type == pg.QUIT:
                    game_state = StateEnum.closing
                if event.type == pg.KEYDOWN:
                    match event.key:
                        case pg.K_DOWN:
                            menu.selected_option = 1
                        case pg.K_UP:
                            menu.selected_option = 0
                        case pg.K_RETURN:
                            if menu.selected_option == 0:
                                game_state = StateEnum.playing
                            elif menu.selected_option == 1:
                                game_state = StateEnum.closing
            menu.update()
            pg.display.flip()
            clock.tick(60)

        while game_state != StateEnum.closing and game_state == StateEnum.finished:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_state = StateEnum.closing
                if event.type == pg.KEYDOWN:
                    match event.key:
                        case pg.K_SPACE:
                            # Reinitialisation de la partie
                            game = g.Game(screen)
                            all_sprites.empty()
                            # retour au menu
                            game_state = StateEnum.in_menu
            fin.update(game)
            addSprite(game,all_sprites)
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