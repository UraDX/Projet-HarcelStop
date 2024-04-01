import random 

def create_quiz_library(file):
    library = []
    question = []
    txtfile = open(file,"r")

    for line in txtfile.readlines():
        split_text = line.split("|")
        
        for text in split_text:
            question.append(text.strip())

        if len(question) != 5:
            pass
        else:    
            library.append(question.copy())
            question.clear()

    print(library)
    txtfile.close()
    return library 



def show_random_quiz(list):
    question = random.choice(list)
    print(question)
    return question

def main():
    quiz_list = create_quiz_library("quiz.txt")
    show_random_quiz(quiz_list)

main()