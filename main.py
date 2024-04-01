import pygame

pygame.init()

#game window

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.dysplay.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variable

game_paused = False
menu_state = "main"

#define font

#define button img

#create button img

#game state

run = True
while run:

    screen.fill((52,78,91))
    if game_paused == True:
        if menu_state == "main":
            

pygame.quit()


