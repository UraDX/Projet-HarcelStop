import pygame
from pygame.locals import*
import sys
import os



pygame.init()

current_directory = os.path.dirname(__file__)
file_name = "IMAGE\logo.png"
file_path = os.path.join(current_directory,file_name)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Game Menu")


#MAIN_MENU a scene that showcase QUICK_GAME, CUSTOM_GAME and SETTINGS

def main_menu():
    from options import options
    from quick_game import number_team

    font_style=pygame.font.SysFont("chalkduster",100)
    logo= pygame.image.load(file_path)


    item1Text=font_style.render("PARTIE RAPIDE",True,(255,255,255))
    item2Text=font_style.render("PARTIE PERSONNALISE", True,(255,255,255))
    item3Text=font_style.render("PARAMETRE", True,(255,255,255))


    while True:

        for event in pygame.event.get():
            
            if(event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()
            if(event.type==pygame.MOUSEBUTTONDOWN):
                if(event.button==1):
                    mouse_pos = pygame.mouse.get_pos()

                    #IMPLEMENTED STILL NEED WORKS
                    if item1Text.get_rect(topleft=(400, 400)).collidepoint(mouse_pos):
                        number_team()

                    #NOT IMPLEMENTED 
                    elif item2Text.get_rect(topleft=(250, 480)).collidepoint(mouse_pos):
                        print("CUSTOM GAME")
                    
                    #IMPLEMENTED STILL NEED WORKS
                    elif item3Text.get_rect(topleft=(450, 560)).collidepoint(mouse_pos):
                        options()
            
            screen.fill((0,155,155))

            screen.blit(item1Text,(400,400))
            screen.blit(item2Text,(250,480))
            screen.blit(item3Text,(450,560))
            screen.blit(logo,(470,20))

            pygame.display.flip()


main_menu()

