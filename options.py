import pygame
from pygame.locals import*
import sys
import os



pygame.init()

current_directory = os.path.dirname(__file__)
file_name = "IMAGE\\back_button.png"
file_path = os.path.join(current_directory,file_name)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Game Options")


#OPTIONS est une scène qui présente la configuration que vous pouvez manipuler

def options():
    from main import main_menu
    from benchcode import resize_image
    back_button = pygame.image.load(file_path)
    font_style=pygame.font.SysFont("chalkduster",100)

    item1Text=font_style.render("EFFETS SONORES",True,(255,255,255))
    item2Text=font_style.render("MUSIQUE DE FOND", True,(255,255,255))
    item3Text=font_style.render("VOIX OFF", True,(255,255,255))
    item4Text=font_style.render("AJOUTER QUIZZES", True,(255,255,255))
    
    while True:

        resized_image = resize_image(back_button, 50, 50)

        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()
            if(event.type==pygame.MOUSEBUTTONDOWN):
                if(event.button==1):
                    mouse_pos = pygame.mouse.get_pos()

                    #Besoin d'implémenter une barre de volume SFX et d'obtenir des SFX
                    if item1Text.get_rect(topleft=(150, 100)).collidepoint(mouse_pos):
                        print("SFX Volume")
                    
                    #Besoin d'implémenter une barre de volume BGM et d'obtenir de la musique de fond
                    elif item2Text.get_rect(topleft=(150, 180)).collidepoint(mouse_pos):
                        print("BGM Volume")

                    #Besoin d'implémenter une barre de volume VO et d'obtenir de la VO
                    elif item3Text.get_rect(topleft=(150, 260)).collidepoint(mouse_pos):
                        print("VO Volume")

                    #Besoin d'implémenter une section ajouter un quiz qui ouvre un fichier texte et le fusionne ou ouvre simplement un txt
                    elif item4Text.get_rect(topleft=(150, 340)).collidepoint(mouse_pos):
                        print("Add Quiz")

                    elif resized_image.get_rect(topleft=(30,650)).collidepoint(mouse_pos):
                        main_menu()

            
            screen.fill((0,155,155))

            screen.blit(item1Text,(150,100))
            screen.blit(item2Text,(150,180))
            screen.blit(item3Text,(150,260))
            screen.blit(item4Text,(150,340))

            screen.blit(resized_image,(30,650))

            pygame.display.flip()

