#!usr/bin/env python3

import os
import time

def clear_console():
    # Clear console based on the platform
    os.system('cls' if os.name == 'nt' else 'clear')

def save_score(username, score):
    with open("scoreboard.txt", "a") as file:
        file.write(f"{username}: {score}\n")

def show_scoreboard():
    with open("scoreboard.txt", "r") as file:
        scoreboard = file.read()
        print("\nScoreboard:\n" + scoreboard)
        
def welcome():
    print("Welcome to movie quote trivia. You will be shown quotes from movies and you will be able to pick from 4 options and guess which one it is. Your score will be the total number of movies you guessed correctly\n")
    
    ask_scoreboard =  input("Would you like to see the scoreboard(y/n)")
    if ask_scoreboard == 'y':
        show_scoreboard()
        input("Press any key to continue...")
        clear_console()
    
    input("Press enter when you're ready to begin...")

def main():
    
    welcome()
     
    questionsAndAnswers = {
        'Stop looking at me Swan!': {
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
        'Thats not a knife, Thats a knife!': {
            'A': 'A bugs life',
            'B': 'Crocodile  Dundee',
            'C': 'Anaconda', 
            'D': 'Terminator 2'
        },
        'Hello. My name is Inigo Montoya. You killed my father. Prepare to die.': {
            'A': 'The Mask of Zorro',
            'B': 'The Princess Bride',
            'C': 'The Hunger Games',
            'D': 'Demolition Man'
        },
        'I Have To Go See About A Girl.': {
            'A': 'Stand by me',
            'B': 'The Other Guys',
            'C': 'Good Will Hunting',
            'D': 'Cast Away'
        }, 
        'Honey? Where\'s my super suit!': {
            'A': 'Man of Steel',
            'B': 'Justice League',
            'C': 'Avengers',
            'D': 'Incredibles'
        },
        'Heathcote. You know, you remind me of the pilsbury doughboy. If I poke your stomach, will it make you go oh-hoh-hoh-hoh!': {
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
        print(f"\nQuote: '{question}'\n")    #"f" is like telling python this is a "template literal" - my translation
        print("What is the movie?\n")
        for option, movie in options.items():   #Loop through the "Object"/dictionary, attached to the movie quote  
            print(f"{option}) {movie}")     #display the options as "Key/Value" pair 
            
        user_answer = input("\nYour answer (A/B/C/D): ").upper() #break the sceond for loop and ask for the users input.

        if user_answer == correct_answer:   #While inside the outer for loop, compare the user's answer to the first answer in the answerlist
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Incorrect! The correct answer is {correct_answer}: {options[correct_answer]}\n")

        time.sleep(2)   #Pause for a few seconds before moving to the next question

    print(f"You got {correct_answers} out of {len(questionsAndAnswers)} questions correct.")
    saveName = input("Would you like to save your score(y/n): ")
    
    if saveName.lower() == 'y':
        username = input("Enter your name: ")
        save_score(username, correct_answers)
        
    show_scoreboard_option = input("Would you like to see the scoreboard (y/n): ")
    if show_scoreboard_option.lower() == 'y':
        show_scoreboard()
        input("Press Enter to continue...")
        
if __name__ == "__main__":
    main()
