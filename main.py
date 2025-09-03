#!/usr/bin/env python

import pygame as pg

# Variable globale pour débug
pause = False

class Game:
    def __init__(self, screen: pg.Surface):
        # Conserve le lien vers l'objet surface ecran du jeux
        self.screen = screen

        # Crée une surface pour le fond du jeu de même taille que la fenêtre
        self.background = pg.Surface(self.screen.get_size())
        self.background.fill("purple")

        # Dessine le font d'écran une première fois
        self.screen.blit(self.background, (0, 0))

        # Vrai si le jeu est fini
        self.isEnded = False

    def isRunning(self):
        global pause
        if self.isEnded:
            return False
        return True

# Fonction principale : pas de varaibles globales
def main():
    # Initialisation de pygame
    pg.init()

    # Donne un nom à la fenêtre
    pg.display.set_caption("Jeux")
    # Taille de l'écran imposée
    screenSize = (1024, 768)
    # Crée la surface qui va servir de surface de jeu
    screen = pg.display.set_mode(screenSize)
    # Creé un objet horloge pour gerer le temps entre deux images
    clock = pg.time.Clock()
    # Nombre de millisecondes entre deux images
    dt = 0

    # Instance
    game = Game(screen)

    #Boucles
    while game.isRunning():
        # Limite la vitesse à 6O images max par secondes
        # Calcule le temps réel entre deux images en millisecondes
        dt = clock.tick(60)

        # Affiche le nouvel état de l'écran
        pg.display.flip()

        # Fin utilisation de pygame
        pg.quit()

if __name__ == "__main__":
    main()