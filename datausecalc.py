#!/usr/bin/python3

# datausecalc.py -  A data usage calculator for Tello users
# kjh9000@github.com

''' Instructions - Copy and paste the wall of text rom the website and paste it 
into datausecalc.txt. Note the potential for fencepost errors. You are responsible for choosing what days to include in the calculation.

Note there is a bug. The data needs to be a float. For example, 700 MB needs to be changed to 700.0 MB.
'''

import re

try:
    testtext = open('datausecalc.txt')
except (NameError, FileNotFoundError):
    print("This program requires a datausecalc.txt file. You can either create it or download it.")
else:
    sum = 0
    count = 0
    for i in re.compile(r'''
        (\d{1,5}\.\d{1,2})
        ''', re.VERBOSE).findall(testtext.read()):
        count += 1
        sum += float(i)
    print("You have used about", round(sum, 2), "MB of data in", count, "days.")
