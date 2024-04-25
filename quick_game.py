import pygame
import subprocess
import sys
import os


pygame.init()

current_directory = os.path.dirname(__file__)
file_back = "IMAGE\\back_button.png"
file_proceed = "IMAGE\\proceed_button.png"
file_plus = "IMAGE\\plus.png"
file_minus = "IMAGE\\minus.png"

file_path_back = os.path.join(current_directory,file_back)
file_path_proceed = os.path.join(current_directory,file_proceed)
file_path_plus = os.path.join(current_directory,file_plus)
file_path_minus = os.path.join(current_directory,file_minus)


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("QuickGame")

font_style=pygame.font.SysFont("chalkduster",100)


def resize_image(image, new_width, new_height):

    resized_image = pygame.transform.scale(image, (new_width, new_height))
    return resized_image


def number_team():
    from main import main_menu

    global num_player
    num_player = 2

    proceedbutton = pygame.image.load(file_path_proceed)
    backbutton = pygame.image.load(file_path_back)
    plus = pygame.image.load(file_path_plus)
    minus = pygame.image.load(file_path_minus)
    item1Text=font_style.render("COMBIEN D'EQUIPE?",True,(255,255,255))
    
    item2Text=font_style.render(str(num_player),True,(255,255,255))

    resized_back = resize_image(backbutton,50,50)
    resized_proceed = resize_image(proceedbutton,50,50)
    resized_plus = resize_image(plus,50,50)
    resized_minus = resize_image(minus,50,50)

    while True:

        for event in pygame.event.get():

            if(event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()

            if(event.type==pygame.MOUSEBUTTONDOWN):

                if(event.button==1):
                    mouse_pos = pygame.mouse.get_pos()

                    if resized_minus.get_rect(topleft=(310, 250)).collidepoint(mouse_pos):
                        print("minus")
                        if num_player <= 2 :
                            None
                        else:
                            num_player -= 1
                        item2Text=font_style.render(str(num_player),True,(255,255,255))

                    elif resized_plus.get_rect(topleft=(1000, 250)).collidepoint(mouse_pos):
                        print("add")
                        if num_player >= 4 :
                            None
                        else:
                            num_player += 1
                        item2Text=font_style.render(str(num_player),True,(255,255,255))

                    elif resized_back.get_rect(topleft=(30,650)).collidepoint(mouse_pos):
                        main_menu()

                    elif resized_proceed.get_rect(topleft=(1200,650)).collidepoint(mouse_pos):
                        game()

            screen.fill((0,155,155))

            screen.blit(item1Text,(310,100))
            screen.blit(item2Text,(650,250))
            screen.blit(resized_minus,(310,250))
            screen.blit(resized_plus,(1000,250))
            screen.blit(resized_back,(30,650))
            screen.blit(resized_proceed,(1200,650))

            pygame.display.flip()


def game():
    
    import random
    from benchcode import create_quiz_library
    quiz_num = 0
    quiz_library = create_quiz_library("quiz.txt")
    random.shuffle(quiz_library)
    quiz = quiz_library[quiz_num]
    
    item1Text=font_style.render(quiz[0],True,(255,255,255))
    

    item3Text=font_style.render(quiz[1],True,(255,255,255))
    item4Text=font_style.render(quiz[2],True,(255,255,255))
    item5Text=font_style.render(quiz[3],True,(255,255,255))
    item6Text=font_style.render(quiz[4],True,(255,255,255))

    while True:
        
        for event in pygame.event.get():

            if not quiz_num < 15:
                scoreboard()

            if(event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()

            if(event.type==pygame.MOUSEBUTTONDOWN):

                if(event.button==1):
                    mouse_pos = pygame.mouse.get_pos()
                    if item1Text.get_rect(topleft=(310,100)).collidepoint(mouse_pos):
                        quiz_num += 1
                        quiz = quiz_library[quiz_num]
                        item1Text=font_style.render(quiz[0],True,(255,255,255))
                        

                        item3Text=font_style.render(quiz[1],True,(255,255,255))
                        item4Text=font_style.render(quiz[2],True,(255,255,255))
                        item5Text=font_style.render(quiz[3],True,(255,255,255))
                        item6Text=font_style.render(quiz[4],True,(255,255,255))

            screen.fill((0,155,155))

            screen.blit(item1Text,(310,100))


            screen.blit(item3Text,(100,200))
            screen.blit(item4Text,(800,200))
            screen.blit(item5Text,(100,500))
            screen.blit(item6Text,(800,500))

              
            pygame.display.flip()
    

def scoreboard():

    item1Text=font_style.render("SCOREBOARD",True,(255,255,255))
   
    while True:
        
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()

            screen.fill((0,155,155))
            screen.blit(item1Text,(310,100))
       
              
            pygame.display.flip()
    

