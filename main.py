 #!/usr/bin/env python
import pygame as pg
import src.model.game as g
import src.model.menu as m
import src.model.fin as f
import src.model.credit as c
from src.model.stateEnum import StateEnum

def main():
    pg.init()
    pg.display.set_caption("Jeux super mega bien") # nom fenêtre
    screen_size = (1024, 768) # Taille écran
    screen = pg.display.set_mode(screen_size)
    clock = pg.time.Clock() # horloge

    # Etat
    game_state = StateEnum.in_menu

    # Instance
    game = g.Game(screen)
    menu = m.Menu(screen)
    fin = f.Fin(screen)
    credit = c.Credit(screen)

    # Ajout sprite de l'ecran de jeu dans all_sprite
    all_sprites = pg.sprite.Group()
    addSprite(game,all_sprites)

    running = True
    while running:
        # --- Gestion des événements selon l'état---
        for event in pg.event.get():
            if event.type == pg.QUIT: # Fermer le Jeu
                running = False
            if event.type == pg.KEYDOWN:
                # Event dans le menu
                if game_state == StateEnum.in_menu:
                    match event.key:
                        case pg.K_DOWN:
                            menu.select_next()
                        case pg.K_UP:
                            menu.select_prev()
                        case pg.K_RETURN:
                            match menu.selected_option:
                                case 0:
                                    game_state = StateEnum.playing
                                case 1:
                                    running = False
                                case 2:
                                    game_state = StateEnum.in_credit
                # Event dans l'écran de jeu
                elif game_state == StateEnum.playing:
                    match event.key:
                        case pg.K_SPACE:
                            game.bard.invisible()
                        case pg.K_DOWN:
                            game.boss.take_damage(10)  # Pour tester les degat au boss
                        case pg.K_b:
                            game.bard.take_damage(1)  # Pour tester les degat au barde
                        case pg.K_j:
                            game.spawnSonicBoom(all_sprites)
                        case pg.K_ESCAPE:
                            game_state = StateEnum.in_menu # Mettre en pause
                        case _:
                            game.handle_key(event.key)
                # Event de l'écran de Victoire/Défaite
                elif game_state == StateEnum.finished:
                    match event.key:
                        case pg.K_SPACE:
                            # Reinitialisation de la partie
                            all_sprites.empty()
                            game = g.Game(screen)
                            addSprite(game, all_sprites)
                            # retour au menu
                            game_state = StateEnum.in_menu
                # Event de l'ecran de crédit
                elif game_state == StateEnum.in_credit:
                    game_state = StateEnum.in_menu # Les inputs toutes les touches font revenir au menu

        #---- Mise à jour et dessin selon l'état ---
        # Update et Draw du Menu
        if game_state == StateEnum.in_menu:
            menu.draw()
        # Update et Draw de l'écran de jeux
        elif game_state == StateEnum.playing:
            game.update(all_sprites)
            game.draw(all_sprites)
            if game.isfinish():
                game_state = StateEnum.finished
        # Update et Draw de l'écran de Victoir/Défaite
        elif game_state == StateEnum.finished:
            fin.update(game)
            fin.draw()
        # Draw les Crédit
        elif game_state == StateEnum.in_credit:
            credit.draw()
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