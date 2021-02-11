#!/usr/bin/python3
#######################
#   guessinggame.py   #
# github.com/kjh9000  #
#######################

import random
guesses = 5
print("Welcome to the guessing game. The program is thinking of a number " + 
"between 1 and 20. You have five attempts to guess the number. Enter q to quit.")

number= random.randint(1,20)

while guesses:
    try:
        guess = int(input("Guess: "))
        if guess < 1 or guess > 20:
            print("The range of numbers to guess from is between 1 and 20.")
            continue
        guesses -=1
        if guess == 'q':
            break
        if guess == number:
            print("You guessed it! The number was " + str(number) + ".")
            break
        if number < guess:
            print("Your guess was too high.")
        if number > guess:
            print("Your guess was too low.")
        if guesses == 0:
            print("You're out of guesses. Game over. The number was " + str(number)
            + ". Thanks for playing!.")

    except ValueError:
        print("This program accepts whole numbers only.")

