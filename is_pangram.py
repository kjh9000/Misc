#!/usr/bin/python
#####################
#  is_pangram.py    #
# github.com/kjh900 #
#####################
def is_pangram(test_string):
    test_string = test_string.lower()
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i in test_string:
            continue
        else:
            print("The string is not a pangram.")
            return False
    print("The string is a pangram.")
is_pangram("The quick, brown fox jumps over the lazy dog!")
is_pangram("How much wood could a woodchuck chuck if a woodchuck could chuck wood?")
