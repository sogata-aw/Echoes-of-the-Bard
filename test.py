# Example file showing a circle moving on screen
import pygame
import src.model.game as g
# Programme principal du jeux
def main():
    # Démmarre le module
    pygame.init()
    # définit l'écran et sa taille, retourne la surface pour le dessin
    screen = pygame.display.set_mode((1024, 768))
    menu_img = pygame.image.load("assets/menu_image.jpg")
    menu_image_redimensionnee = pygame.transform.scale(menu_img, (1280, 720))
    btn_play = pygame.transform.scale(pygame.image.load("assets/buttons/play_button.png"), (800, 400))
    btn_play_cho = pygame.transform.scale(pygame.image.load("assets/buttons/play_button_choosen.png"), (800, 400))
    btn_quit = pygame.transform.scale(pygame.image.load("assets/buttons/quit_button.png"), (800, 400))
    btn_quit_cho = pygame.transform.scale(pygame.image.load("assets/buttons/quit_button_choosen.png"), (800, 400))
    # Définit l'horloge pour connaitre le temps qui a passé
    clock = pygame.time.Clock()
    # Pour savoir quand la boucle du jeu se termine
    running = True
    in_menu = True
    # Le temps passé entre deux rafraichissement de l'écran en millisecondes
    dt = 0

    # 0 = Play, 1 =Quit
    selected_option = 0 ;

    # La position du joueur : au milieu de l'écran
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    # Boucle de l'animation
    while running:
        # Limite le frame rate à 60 images par secondes et retourne le temps réel passé
        dt = clock.tick(60)
        screen.blit(menu_image_redimensionnee,(0,0))

        # Parcourt tous les évenements pour les traiter
        for event in pygame.event.get():
            # QUIT signifie que l'utilisateur a fermé la fenêtre
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and in_menu:
                if event.key == pygame.K_DOWN:
                    selected_option = 1
                elif event.key == pygame.K_UP:
                    selected_option = 0
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        in_menu = False
                    elif selected_option == 1:
                        running = False

        if in_menu:
            if selected_option == 0:
                screen.blit(btn_play_cho, (screen.get_width() / 2 - 400, 130))
                screen.blit(btn_quit, (screen.get_width() / 2 - 400, 230))
            else:
                screen.blit(btn_play, (screen.get_width() / 2 - 400, 130))
                screen.blit(btn_quit_cho, (screen.get_width() / 2 - 400, 230))
        else:
            screen.fill((0, 0, 0))  # Efface l'écran (fond noir)
            print("Lancer le jeu")

        # Mettre à jour l'affichage
        pygame.display.flip()

    # Termine proprement le module
    pygame.quit()
# Appel au programme principal
main()