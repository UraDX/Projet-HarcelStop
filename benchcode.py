import os
import pygame

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


with open(file_quiz, newline='', encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    data = list(reader)


def resize_image(image, new_width, new_height):

    resized_image = pygame.transform.scale(image, (new_width, new_height))
    return resized_image


import keyboard

def print_pressed_keys():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(f"Key Pressed: {event.name}")




