import pygame
from pygame.locals import *
import sys, random , os , time
from benchcode import resize_image, create_quiz_library

pygame.init()

current_directory = os.path.dirname(__file__)
file_back = "IMAGE/back_button.png"
file_proceed = "IMAGE/proceed_button.png"
file_plus = "IMAGE/plus.png"
file_minus = "IMAGE/minus.png"
file_replay = "IMAGE/replay_button.png"

file_path_back = os.path.join(current_directory,file_back)
file_path_proceed = os.path.join(current_directory,file_proceed)
file_path_plus = os.path.join(current_directory,file_plus)
file_path_minus = os.path.join(current_directory,file_minus)
file_path_replay = os.path.join(current_directory,file_replay)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("QuickGame")

# Use a font that supports special characters
font_style = pygame.font.Font(pygame.font.get_default_font(), 40)

global num_player, quiz_num, quiz_library, quiz, score

# QUIZ VAR
num_player = 2
quiz_num = 1

# Read the quiz file with UTF-8 encoding
def create_quiz_library(filename):
    with open(filename, encoding='utf-8') as f:
        content = f.readlines()
    quiz_list = [line.strip().split(' | ') for line in content if line.strip()]
    return quiz_list

quiz_library = create_quiz_library("quiz.txt")
random.shuffle(quiz_library)
quiz = quiz_library[quiz_num]

# TIMER VAR
display_timer = 0
DISPLAY_DURATION = 200

def get_turn(num_player, turn_num):
    turn_num_calc = turn_num % num_player
    if turn_num_calc == 0:
        return num_player
    else:
        return turn_num_calc

def check_answer(ans1, ans2):
    return ans1 == ans2

def check_answer_new(ans1, ans2):
    return ans1 == ans2

def display_message_key_pressed(message, color, position, duration):
    screen.fill(color)
    text_surface = font_style.render(message, True, (250, 250, 250))
    screen.blit(text_surface, position)
    pygame.display.flip()
    pygame.time.delay(duration)

def display_message(message, color, position):
    text_surface = font_style.render(message, True, color)
    screen.blit(text_surface, position)

def add_score(num_player, turn_num):
    global score
    if score[-1] < quiz_num:
        print("add score")
        team = get_turn(num_player, turn_num)
        score[team-1] += 1
        score[-1] += 1

def display_correct_message(input_answer, correct_answer):
    global display_timer, score_added
    if check_answer(input_answer, correct_answer):
        if not score_added:
            add_score(num_player, quiz_num)
            score_added = True
        display_message("CORRECT!", (255, 255, 255), (500, 370))
    else:
        first_buzz = True
        display_message("INCORRECT!", (255, 255, 255), (500, 370))
    display_timer = pygame.time.get_ticks()

def display_correct_message_buzzed(input_answer, correct_answer):
    global display_timer
    if check_answer(input_answer, correct_answer):
        add_score(player_buzz, quiz_num)
        display_message("CORRECT!", (255, 255, 255), (500, 370))
    else:
        display_message("INCORRECT!", (255, 255, 255), (500, 370))
    display_timer = pygame.time.get_ticks()

def number_team():
    from main import main_menu
    global num_player, score, quiz_num
    quiz_num = 1
    score = [0] * (num_player+1)
    proceedbutton = pygame.image.load(file_path_proceed)
    backbutton = pygame.image.load(file_path_back)
    plus = pygame.image.load(file_path_plus)
    minus = pygame.image.load(file_path_minus)
    item1Text = font_style.render("COMBIEN D'EQUIPE?", True, (255, 255, 255))
    item2Text = font_style.render(str(num_player), True, (255, 255, 255))
    resized_back = resize_image(backbutton, 50, 50)
    resized_proceed = resize_image(proceedbutton, 50, 50)
    resized_plus = resize_image(plus, 50, 50)
    resized_minus = resize_image(minus, 50, 50)
    while True:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(event.button == 1):
                    mouse_pos = pygame.mouse.get_pos()
                    if resized_minus.get_rect(topleft=(310, 250)).collidepoint(mouse_pos):
                        print("minus")
                        if num_player <= 2:
                            None
                        else:
                            num_player -= 1
                            score.pop()
                        item2Text = font_style.render(str(num_player), True, (255, 255, 255))
                    elif resized_plus.get_rect(topleft=(1000, 250)).collidepoint(mouse_pos):
                        print("add")
                        if num_player >= 4:
                            None
                        else:
                            num_player += 1
                            score.append(0)
                        item2Text = font_style.render(str(num_player), True, (255, 255, 255))
                    elif resized_back.get_rect(topleft=(30, 650)).collidepoint(mouse_pos):
                        main_menu()
                    elif resized_proceed.get_rect(topleft=(1200, 650)).collidepoint(mouse_pos):
                        game()
            screen.fill((0, 155, 155))
            screen.blit(item1Text, (310, 100))
            screen.blit(item2Text, (650, 250))
            screen.blit(resized_minus, (310, 250))
            screen.blit(resized_plus, (1000, 250))
            screen.blit(resized_back, (30, 650))
            screen.blit(resized_proceed, (1200, 650))
            pygame.display.update()
            pygame.display.flip()

def game():
    global quiz_num, quiz_library, quiz, input_answer, score, player_buzz, first_buzz, score_added
    correct_answer = quiz[5]
    print(score)
    item1Text = font_style.render(quiz[0], True, (255, 255, 255))
    item3Text = font_style.render(quiz[1], True, (255, 255, 255))
    item4Text = font_style.render(quiz[2], True, (255, 255, 255))
    item5Text = font_style.render(quiz[3], True, (255, 255, 255))
    item6Text = font_style.render(quiz[4], True, (255, 255, 255))
    first_buzz = False
    score_added = False
    key_pressed = False
    button_enabled = False
    player_buzz = None
    stop_display = False
    timer_started = False  
    start_time = 0 
    timer_duration = 20
    while True:
        for event in pygame.event.get():
            screen.fill((0, 155, 155))
            if not quiz_num < 15:
                scoreboard()
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if(event.type == pygame.KEYDOWN) and not key_pressed and button_enabled:
                if event.key == K_1:
                    key_pressed = True
                    player_buzz = 1
                    display_message_key_pressed("RED", (255, 0, 0), (500, 370), 500)
                elif event.key == K_2:
                    key_pressed = True
                    player_buzz = 2
                    display_message_key_pressed("BLUE", (0, 0, 255), (500, 370), 500)
                elif event.key == K_3 and len(score) >= 4:
                    key_pressed = True
                    player_buzz = 3
                    display_message_key_pressed("YELLOW", (255, 255, 0), (500, 370), 500)
                elif event.key == K_4 and len(score) >= 5:
                    key_pressed = True
                    player_buzz = 4
                    display_message_key_pressed("GREEN", (0, 255, 0), (500, 370), 500)
            if not timer_started:   
                timer_started = True
                start_time = time.time()
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(event.button == 1):
                    mouse_pos = pygame.mouse.get_pos()
                    if item1Text.get_rect(topleft=(310, 100)).collidepoint(mouse_pos):
                        quiz_num += 1
                        quiz = quiz_library[quiz_num]
                        item1Text = font_style.render(quiz[0], True, (255, 255, 255))
                        item3Text = font_style.render(quiz[1], True, (255, 255, 255))
                        item4Text = font_style.render(quiz[2], True, (255, 255, 255))
                        item5Text = font_style.render(quiz[3], True, (255, 255, 255))
                        item6Text = font_style.render(quiz[4], True, (255, 255, 255))
                        team_turn()
                    elif item3Text.get_rect(topleft=(100, 200)).collidepoint(mouse_pos):
                        input_answer = quiz[1]
                        print("ANSWER 1 PRESSED")
                        if key_pressed:
                            display_correct_message_buzzed(input_answer, correct_answer)
                        else:
                            display_correct_message(input_answer, correct_answer) 
                        key_pressed = False
                    elif item4Text.get_rect(topleft=(800, 200)).collidepoint(mouse_pos):
                        input_answer = quiz[2]
                        print("ANSWER 2 PRESSED")
                        if key_pressed:
                            display_correct_message_buzzed(input_answer, correct_answer)
                        else:
                            display_correct_message(input_answer, correct_answer) 
                        key_pressed = False
                    elif item5Text.get_rect(topleft=(100, 500)).collidepoint(mouse_pos):
                        input_answer = quiz[3]
                        print("ANSWER 3 PRESSED")
                        if key_pressed:
                            display_correct_message_buzzed(input_answer, correct_answer)
                        else:
                            display_correct_message(input_answer, correct_answer) 
                        key_pressed = False
                    elif item6Text.get_rect(topleft=(800, 500)).collidepoint(mouse_pos):
                        input_answer = quiz[4]
                        print("ANSWER 4 PRESSED")
                        if key_pressed:
                            display_correct_message_buzzed(input_answer, correct_answer)
                        else:
                            display_correct_message(input_answer, correct_answer) 
                        key_pressed = False
            if (time.time() - start_time >= timer_duration and not stop_display) or first_buzz: 
                display_message_key_pressed("JEOPARDY", (255, 0, 255), (500, 370), 500) 
                button_enabled = True
                timer_started = False
                stop_display = True
            screen.blit(item1Text, (310, 100))
            screen.blit(item3Text, (100, 200))
            screen.blit(item4Text, (800, 200))
            screen.blit(item5Text, (100, 500))
            screen.blit(item6Text, (800, 500))
            if pygame.time.get_ticks() - display_timer < DISPLAY_DURATION:
                display_correct_message(input_answer, correct_answer)
            pygame.display.flip()

def team_turn():
    global num_player, quiz_num, game_team_list, score
    player_turn = get_turn(num_player, quiz_num)
    total_team_list = ["RED", "BLUE", "YELLOW", "GREEN"]
    game_team_list = total_team_list[:num_player]
    if score[-1]+1 < quiz_num:
        score[-1] += 1
    item1Text = font_style.render("Tour d'Equipe " + game_team_list[player_turn-1] ,True,(255,255,255))
    proceedbutton = pygame.image.load(file_path_proceed)
    resized_proceed = resize_image(proceedbutton, 50, 50)
    team_texts = []
    for team_name in game_team_list:
        team_text = font_style.render("Team: " + team_name, True, (255, 255, 255))
        team_texts.append(team_text)
    team_score_texts = []
    for team_score in score[:-1]:
        team_score_text = font_style.render("Score: " + str(team_score), True, (255, 255, 255))
        team_score_texts.append(team_score_text)
    while True:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(event.button == 1):
                    mouse_pos = pygame.mouse.get_pos()
                    if resized_proceed.get_rect(topleft=(1200, 650)).collidepoint(mouse_pos):
                        game()
        screen.fill((0, 155, 155))
        screen.blit(resized_proceed, (1200, 650))
        screen.blit(item1Text, (310, 100))
        for idx, team_text in enumerate(team_texts):
            screen.blit(team_text, (100, 200 + idx * 100))
        for idx, team_text in enumerate(team_score_texts):
            screen.blit(team_text, (700, 200 + idx * 100))
        pygame.display.flip()

def scoreboard():
    from main import main_menu
    global num_player, game_team_list, score
    total_team_list = ["RED", "BLUE", "YELLOW", "GREEN"]
    game_team_list = total_team_list[:num_player]
    backbutton = pygame.image.load(file_path_back)
    replaybutton = pygame.image.load(file_path_replay)
    item1Text = font_style.render("SCOREBOARD", True, (255, 255, 255))
    resized_back = resize_image(backbutton, 50, 50)
    resized_replay = resize_image(replaybutton, 50, 50)
    team_texts = []
    for team_name in game_team_list:
        team_text = font_style.render("Team: " + team_name, True, (255, 255, 255))
        team_texts.append(team_text)
    team_score_texts = []
    for team_score in score[:-1]:
        team_score_text = font_style.render("Score: " + str(team_score), True, (255, 255, 255))
        team_score_texts.append(team_score_text)
    while True:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(event.button == 1):
                    mouse_pos = pygame.mouse.get_pos()
                    if resized_back.get_rect(topleft=(30, 650)).collidepoint(mouse_pos):
                        main_menu()
                    elif resized_replay.get_rect(topleft=(1200, 650)).collidepoint(mouse_pos):
                        number_team()
        screen.fill((0, 155, 155))
        screen.blit(item1Text, (310, 100))
        screen.blit(resized_back, (30, 650))
        screen.blit(resized_replay, (1200, 650))
        for idx, team_text in enumerate(team_texts):
            screen.blit(team_text, (100, 200 + idx * 100))
        for idx, team_text in enumerate(team_score_texts):
            screen.blit(team_text, (700, 200 + idx * 100))
        pygame.display.flip()
