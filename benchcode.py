import os
import pygame
from pyexcel_ods import get_data


def create_quiz_library(file):
    library = []
    question = []
    txtfile = open(file,"r")

    for line in txtfile.readlines():
        split_text = line.split("|")
        
        for text in split_text:
            question.append(text.strip())

        if len(question) != 6 :
            pass
        else:    
            library.append(question.copy())
            question.clear()
    print(library)
    txtfile.close()
    return library 


import csv

current_directory = os.path.dirname(__file__)
file_quiz = "quiz.csv"
file_quiz_path = os.path.join(current_directory,file_quiz)
with open(file_quiz, newline= "",encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)


with open(file_quiz, newline='', encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)


                 

def create_quiz_library_ods(filename):
    Q = []
    BR = []
    MR = []
    #for c in filename:
        #c{"QUESTION"}
        #c{"BONNES_REPONSES"}
        #c{"MAUVAISES_REPONSES"}
    #print("QST",Q)
    #print("BR", BR)
    #print("MR", MR)

#print(create_quiz_library_ods(reader))


def resize_image(image, new_width, new_height):

    resized_image = pygame.transform.scale(image, (new_width, new_height))
    return resized_image


def quiz_create():
    quiz_list = create_quiz_library("quiz.txt")
    #random.shuffle(quiz_list)
    #print(quiz_list)
    #print(quiz_list[0])

#quiz_create()


import keyboard

def print_pressed_keys():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(f"Key Pressed: {event.name}")

# Call the function to start printing pressed keys
#print_pressed_keys()


