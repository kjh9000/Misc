#!/usr/bin/python3
# temperature_conversion.py
# https://github.com/kjh9000

def tempconvert():
    print("Welcome to the temperature conversion program.")
    try:
        system = input("Which system are you converting? (c for celsius to " +
        "fahrenheit, or f for fahrenheit to celsius: ")
        system = system.lower()
        temp = input("Please enter the temperature that you wish to convert: ")
        temp = int(temp)
    except ValueError:
        print("Invalid input. Exiting.")
        exit()
    else:
        if system == 'c' or system == 'C':
            print(temp * 1.8 + 32)
        elif system == 'f' or system == 'f':
            print((temp - 32) / 1.8)
        else:
            print("Invalid input. Exiting.")
            exit()
tempconvert()
