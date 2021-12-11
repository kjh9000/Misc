#!/usr/bin/python3

# powerballnumbergen.py - A powerball number picker
# github.com/kjh9000

# I recall the story of a man who developed a strategy for playing the lottery. He played the
# most frequently occuring numbers. He started to win small amounts before winning the 
# jackpot.

# This programs sifts through the latest x amount Powerball number sets entered into powerballnumbers.txt 
# and returns the  most frequently occuring numbers. If you happen to win big money with the help of this
# program, share some wealth with me. ;)

# Instructions:
# 1) Copy the block of numbers from https://powerfall.com/PastWinningLotteryNumbers/powerball/last50/
# into powerballnumbers.txt and run this file. (The website doesn't allow scrapers. Connection refused.)
# 2) Run powerballnumbergen.py  and it will return two lists containing tuples.
# How to interpret the results: [(number) (how many occurances)] 
# For example [('22', 9)] means the number 22 occured nine times

import re
from collections import Counter

numbers = {}
powerball = {}

testtext = open('powerballnumbers.txt')
for i in re.compile(r'(\d{1,2}),(\d{1,2}),(\d{1,2}),(\d{1,2}),(\d{1,2}),(\d{1,2})').findall(testtext.read()):
    count = 0
    for j in i:
        if count == 5:
            powerball.setdefault(j, 0)
            powerball[j] += 1
        else:
            numbers.setdefault(j, 0)
            numbers[j] += 1
            count += 1
try:
    numbers_counter = Counter(numbers)
    pball_numbers_counter = Counter(powerball)
    temp = []
    for i in numbers_counter.most_common(5):
        temp.append(i[0])
    temp.sort()
    temp = " ".join(temp)

    pball = pball_numbers_counter.most_common(1)[0][0]
except IndexError:
    print("There seems to be a problem with powerballnumbers.txt. \n\
Please ensure it contains at least one set of numbers and try again.")
else:
    print("Most common whiteball numbers:")
    # You can change the number of results to display from the default 20
    print(numbers_counter.most_common(20))

    print("\nMost common Powerballs:")
    # You can change the number of results to display from the default 5
    print(pball_numbers_counter.most_common(5))

    print("\nThe quick pick: " +temp + " Powerball: " + str(pball))

