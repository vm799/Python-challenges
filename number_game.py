"""
Get a random umber from a range
Capture a guess
evaluate the guess

"""
import random

random_num =  random.randint(0,100)
def guessing_game():
    while True:
        user_guess = int(input("Type in your guess, a number between 0-100:  "))
    
        if user_guess < random_num:
            print("Nope! Too low!!, Try again")
            
        elif user_guess > random_num:
            print("Nope! Too high!!, Try again")
        
        else:
            print("You got it!!! well done")
            break

guessing_game()