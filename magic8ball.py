#!/usr/bin/python3
# A basic magic 8 ball program. Ask a question, and run the program.

import random
number = random.randint(1,8)

def shake_it_baby():
    if number == 1:
        print("Absolutely!")
    elif number == 2:
        print("Ask again later.")
    elif number == 3:
        print("Absolutely not.")
    elif number == 4:
        print("The magic 8 ball is uncertain.")
    elif number == 5:
        print("Probably not.")
    elif number == 6:
        print("Probably.")
    elif number == 7:
        print("No.")
    elif number == 8:
        print("Yes.")

shake_it_baby()
