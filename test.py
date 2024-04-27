import pygame
import subprocess
import sys, random , os , time
from benchcode import resize_image, create_quiz_library


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

global num_player, quiz_num, quiz_library, quiz
num_player = 2
quiz_num = 1
quiz_library = create_quiz_library("quiz.txt")
random.shuffle(quiz_library)
quiz = quiz_library[quiz_num]



def get_turn(num_player,turn_num):

    turn_num_calc = turn_num % num_player
    if turn_num_calc == 0:
        return num_player
    else:
        return turn_num_calc
    
def check_answer(ans1,ans2):
    return ans1==ans2

def display_message():
    message = font_style.render("CORRECT!", True, (255, 255, 255))
    screen.blit(message, (500, 370))

def display_message_2():
    message = font_style.render("INCORRECT!", True, (255, 255, 255))
    screen.blit(message, (500, 370))

def display_correct_message(input_answer,correct_answer):
    if check_answer(input_answer,correct_answer):
        display_message()
        
    else:
        display_message_2()




#NUMBER_TEAM is a scene that let you put how many team will be player

def number_team():
    from main import main_menu
    global num_player

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


#GAME is a scene that showcase the quiz and the answers available !!!NEED TO IMPLEMENT A TIMER FOR THE QUIZ

def game():
    
    global quiz_num, quiz_library, quiz, input_answer

    correct_answer = quiz[5]
    item1Text=font_style.render(quiz[0],True,(255,255,255))
    

    item3Text=font_style.render(quiz[1],True,(255,255,255))
    item4Text=font_style.render(quiz[2],True,(255,255,255))
    item5Text=font_style.render(quiz[3],True,(255,255,255))
    item6Text=font_style.render(quiz[4],True,(255,255,255))

    while True:
        
        for event in pygame.event.get():

            screen.fill((0,155,155))

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
                        team_turn()

                    elif item3Text.get_rect(topleft=(100,200)).collidepoint(mouse_pos):
                        input_answer = quiz[1]
                        print("ANSWER 1 PRESSED")
                        display_correct_message(input_answer,correct_answer)

                    elif item4Text.get_rect(topleft=(800,200)).collidepoint(mouse_pos):
                        input_answer = quiz[2]
                        print("ANSWER 2 PRESSED")
                        display_correct_message(input_answer,correct_answer)

                    elif item5Text.get_rect(topleft=(100,500)).collidepoint(mouse_pos):
                        input_answer = quiz[3]
                        print("ANSWER 3 PRESSED")
                        display_correct_message(input_answer,correct_answer)

                    elif item6Text.get_rect(topleft=(800,500)).collidepoint(mouse_pos):
                        input_answer = quiz[4]
                        print("ANSWER 4 PRESSED")
                        display_correct_message(input_answer,correct_answer)



            screen.blit(item1Text,(310,100))


            screen.blit(item3Text,(100,200))
            screen.blit(item4Text,(800,200))
            screen.blit(item5Text,(100,500))
            screen.blit(item6Text,(800,500))

              
            pygame.display.flip()


#TEAM_TURN is a scene that displays what team is playing also should add and update scoreboard to it later

def team_turn():

    global num_player, quiz_num

    player_turn = get_turn(num_player,quiz_num)
    total_team_list = ["RED", "BLUE", "YELLOW", "GREEN"]
    game_team_list = total_team_list[:num_player]

    item1Text=font_style.render("Tour d'Equipe " + game_team_list[player_turn-1] ,True,(255,255,255))
    proceedbutton = pygame.image.load(file_path_proceed)
    resized_proceed = resize_image(proceedbutton,50,50)
    
    while True:

        for event in pygame.event.get():

            if(event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()
            
            if(event.type==pygame.MOUSEBUTTONDOWN):
                
                if(event.button==1):
                    mouse_pos = pygame.mouse.get_pos()

                    if resized_proceed.get_rect(topleft=(1200,650)).collidepoint(mouse_pos):
                        game()
        

        screen.fill((0,155,155))
        screen.blit(resized_proceed,(1200,650))
        screen.blit(item1Text,(310,100))
        pygame.display.flip()


#Scorboard is a scene that displays the scoreboard !!!SCORE SYSTEM NOT IMPLEMENTED YET

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
    

