#!usr/bin/env python3

import os
import time

def clear_console():
    # Clear console based on the platform
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    questionsAndAnswers = {
        'Stoping looking at me SWAN!': {
            'A': 'Billy Madison', 
            'B': 'Happy Gilmore', 
            'C': 'Just Go With It', 
            'D': '50 first dates'
        },
        'Why, Johnny Ringo, you look like somebody just walked over your grave.': {
            'A': '3:10 to Yuma', 
            'B': 'Django', 
            'C': 'Tombstone', 
            'D': 'True Grit'
        },
        'You call that a knife? This is a knife!': {
            'A': 'A bugs life',
            'B': 'Crocodile  Dundee',
            'C': 'Anaconda', 
            'D': 'Terminator 2'
        },
        'Hello. My name is Inigo Montoya. You killed my father. Prepare to die.': {
            'A': 'The Mask of Zorro',
            'B': 'The Princess Bride',
            'C': 'The Hunger Games',
            'D': 'This is not from a movie'
        },
        'I Have To Go See About A Girl.': {
            'A': 'Stand by me',
            'B': 'The Other Guys',
            'C': 'Good Will Hunting',
            'D': 'Cast Away'
        }, 
        'Honey? Where\'s my super suit': {
            'A': 'Man of Steel',
            'B': 'Justice League',
            'C': 'Avengers',
            'D': 'Incredibles'
        },
        'Nope, but I can clean your colon quicker than one of them burrito with extra guacamole sauce!': {
            'A': 'Bulletproof',
            'B': 'Major Payne',
            'C': 'White Chicks',
            'D': 'Scary Movie'
        }
    }

    answerList = ['A', 'C', 'B', 'B', 'C', 'D', 'B']
       
    correct_answers = 0

    for (question, options), correct_answer in zip(questionsAndAnswers.items(), answerList):    #The "zip" function combines iterables and allows you to loop through them
        clear_console() 
        print(f"\nQuestion: {question}")    #"f" is like telling python this is a "template literal" - my translation
        for option, movie in options.items():   #Loop through the "Object"/dictionary, attached to the movie quote  
            print(f"{option}. {movie}")     #display the options as "Key/Value" pair 

        user_answer = input("Your answer (A/B/C/D): ").upper() #break the sceond for loop and ask for the users input.

        if user_answer == correct_answer:   #While inside the outer for loop, compare the user's answer to the first answer in the answerlist
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Incorrect! The correct answer is {correct_answer}: {options[correct_answer]}\n")

        time.sleep(2)   #Pause for a few seconds before moving to the next question

    print(f"You got {correct_answers} out of {len(questionsAndAnswers)} questions correct.")

if __name__ == "__main__":
    main()