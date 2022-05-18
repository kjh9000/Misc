#!/usr/bin/python3
# hangman.py
# github.com/kjh9000

import random

# you can extend the word list. 
wordlist = ['california', 'programming', 'washington', 'multiplication']
mysteryword = wordlist[random.randint(0,len(wordlist))]


obscuredword = "_" * len(mysteryword)
hangman  = ""
parts = ['  |  \n', '  0\n', ' /', '|', '\\\n', ' /',' \\']
while parts:
    if "_" not in obscuredword:
        print("You win! Game over.")
        break
    print("the word is %s." % obscuredword)
    guess = input("Give me a lowercase letter: ")
    if guess in obscuredword:
        print("You already guessed %s." % guess)
    elif guess in mysteryword:
        print("The letter %s in in the mystery word" % guess)
        temp = ""
        counter = 0
        for i in mysteryword:
            if i == guess:
                temp += i
            else:
                if obscuredword[counter] == "_":
                    temp += "_"
                else:
                    temp += i
            counter += 1
        obscuredword = temp
    else:
        print("sorry, but the letter %s in not in the mystery word." % guess)
        hangman += parts[0]
        parts.pop(0)
        print(hangman)
if not parts:
    print("Sorry you lose. Game over.")
