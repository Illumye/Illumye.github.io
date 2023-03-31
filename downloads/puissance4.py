import pygame

# Initialisation de pygame
pygame.init()

# Largeur et hauteur de l'écran
size = (700, 500)
screen = pygame.display.set_mode(size)

# Pour faire une boucle jusqu'à ce que le joueur clique sur la croix pour fermer
done = False

# Pour gérer le temps de rafraichissement de l'écran
clock = pygame.time.Clock()

# Initialisation des couleurs
red = (255, 0, 0)
yellow = (255, 255, 0)
player1= 'Joueur rouge'
player2= 'Joueur jaune'
# Liste de liste représentant le plateau
board = [[0 for i in range(7)] for j in range(6)]

turn = 1

# Boucle du jeu
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Rafraichissement de l'écran
    screen.fill((255, 255, 255))

    # Création du "plateau" de jeu
    for i in range(6):
        for j in range(7):
            pygame.draw.rect(screen, (0, 0, 0), [j*100, i*75, 100, 75], 2)
            if board[i][j] == 1:
                pygame.draw.circle(screen, red, (j*100+50, i*75+37), 25)
            elif board[i][j] == 2:
                pygame.draw.circle(screen, yellow, (j*100+50, i*75+37), 25)

    # --- Affiche les dernières modifications
    pygame.display.flip()

    # --- Limitation du rafraichissement de l'écran à 60 fps
    clock.tick(60)
    # --- Boucle principale (placement des pièces et conditions de victoire)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtient la position x et y du curseur de la souris
            pos = pygame.mouse.get_pos()
            # Trouver position x du curseur et donc la colonne 
            # (nécéssite que chaque colonne est une largeur de 100 pixels)
            col = pos[0] // 100
            # Trouve le premier emplacement vide de la colonne
            for i in range(5, -1, -1):
                if board[i][col] == 0:
                    # Placement de la pièce
                    if turn % 2 == 1:
                        board[i][col] = 1
                        pygame.display.set_caption("Joueur actuel : jaune")
                    else:
                        board[i][col] = 2
                        pygame.display.set_caption("Joueur actuel : rouge")
                    turn += 1
                    break
            # Vérification des possibles victoires
            for i in range(6):
                for j in range(7):
                    if board[i][j] != 0:
                        # Vérification des lignes horizontales
                        if j <= 3 and board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3]:
                            print("Player", board[i][j], "wins!")
                            done = True
                        # Vérification des lignes verticales
                        if i <= 2 and board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j]:
                            print("Player", board[i][j], "wins!")
                            done = True
                        # Vérification des lignes diagonales
                        if i <= 2 and j <= 3 and board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]:
                            print("Player", board[i][j], "wins!")
                            done = True
                        if i <= 2 and j >= 3 and board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3]:
                            print("Player", board[i][j], "wins!")
                            done = True
    if done:
        # Réinitialisation de l'écran
        screen.fill((255, 255, 255))
        # Ecriture du message de victoire
        font = pygame.font.Font(None, 30)
        if turn % 2 == 1:
          text = font.render("Le {} a gagné !".format(player2), True, (0, 0, 0))
        else:
          text = font.render("Le {} a gagné !".format(player1), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (size[0] // 2, size[1] // 2)
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()