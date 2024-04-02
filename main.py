import pygame
from pygame.locals import*
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Game Menu")

def main_menu():
    item1=pygame.Rect(200,200,200,50)
    item2=pygame.Rect(200,270,200,50)
    item3=pygame.Rect(200,340,200,50)
    
    font_style=pygame.font.SysFont("chalkduster",100)
    logo= pygame.image.load("C:\\Users\\limce\\OneDrive\\Desktop\\HarcelStop\\HarcelStop\\logo.png").convert()
    #header=font_style.render("Main Menu", True,(255,255,0))


    item1Text=font_style.render("PLAY",True,(255,255,255))
    item2Text=font_style.render("OPTION", True,(255,255,255))
    item3Text=font_style.render("EXIT", True,(255,255,255))
    while True:
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()
            if(event.type==pygame.MOUSEBUTTONDOWN):
                if(event.button==1):
                    mouse_pos=pygame.mouse.get_pos()
                    if(item1.collidepoint(mouse_pos)):
                        print("Playing Game")
                    elif(item2.collidepoint(mouse_pos)):
                        print("Game Options")
                    elif(item3.collidepoint(mouse_pos)):
                        pygame.quit()
                        sys.exit()
            screen.fill((0,155,155))
            #screen.blit(header,(215,150))

            pygame.draw.rect(screen,(214,0,79),item1)
            pygame.draw.rect(screen,(214,0,79),item2)
            pygame.draw.rect(screen,(214,0,79),item3)

            screen.blit(item1Text,(250,210))
            screen.blit(item2Text,(220,280))
            screen.blit(item3Text,(250,350))
            screen.blit(logo,(250,250))

            pygame.display.flip()

main_menu()

