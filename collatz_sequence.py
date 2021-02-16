#!/usr/bin/python3
###############################
#     collatz_sequence.py     #
#     github.com/kjh9000      #
###############################

print("Please enter a number.")

def collatz():
    try:
        number=int(input())
        while number != 1:
            if number % 2 == 0:
                print(number)
                number = number //2
                continue
            if number % 2 != 0:
                print(number)
                number = number * 3 + 1
                continue
    except ValueError:
        print("This program accepts whole numbers only.")
collatz()
