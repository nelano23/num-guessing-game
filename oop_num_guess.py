#Modified Number Guessing Game 
#Difficulty: Easy
#Concepts: Conditional Statements, Functions, Loops, Random Number Generation, Input/Output, Exception Handlng
# Lists, String Manipulation, Exiting the Program, Main function
#----------------------------------------------------------------

import random
import time 

attempts = []

def see_score():
    if not attempts:
        print ("There is currently no highscore! ")
    else: 
        print (f"The highscore is currently {min(attempts)} ")

def play_game():
    random.seed(time.time())
    number = random.randint(1,5)
    tries = 0 
    print( f"Welcome to the Number Guessing Game! Let's test how good your guessing skills are.")
    player_name = input("What is your name? ")
    print(f"Welcome {player_name}!")
    ask_play = input("Do you want to play the game? (Enter yes or no )" )
    if ask_play.lower() != 'yes':
        print("See ya later!")
        exit()
    while ask_play.lower() == "yes":
        try:
            x = int(input("To begin enter a number from 1 to 5: "))
            if x < 1 or x > 5:
                raise ValueError("Number out of range")
            tries += 1
            attempts.append(tries)
            if x != number:
                print("Wrong! Try again")
                print("Guess a number between 1 and 5")
            if x == number:
                 print ("You are correct! You win")
                 print(f"It took you {tries} tries")
                 see_score()
                 y = input("Would you like to play again? (Enter yes or no)")
                 if y.lower() == 'yes':
                     tries = 0
                     continue
                 else:
                     print("Thanks for playing see ya!")
                     see_score()
                     exit()
        

        except ValueError as err:
            print('Oh no!, that is not a valid value. Try again...')
            print(err)

if __name__ == '__main__':
    play_game()