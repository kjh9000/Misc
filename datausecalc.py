#!/usr/bin/python3

# datausecalc.py
# kjh9000@github.com
'''My ISP only gives me the data used for each day, not the total. This program
extracts the data used from the wall of text provided, adds it and returns the 
sum and the number of days into the plan one is. Note the current day counts as
one complete day
'''
import re

testtext= '''


--replace this wall of example text with your own	-
03/09/2021 			888.85 MB 	Custom Plan 	-
03/08/2021 			630.98 MB 	Custom Plan 	-
03/07/2021 			654.05 MB 	Custom Plan 	-
03/06/2021 			717.54 MB 	Custom Plan 	-
03/05/2021 			939.73 MB 	Custom Plan 	-
03/04/2021 			660.44 MB 	Custom Plan 	-
03/03/2021 			1014.72 MB 	Custom Plan 	-


'''

# extracts the data and adds it, then returns the sum along with the days
sum = 0
count = 0
for i in re.compile(r'''
    (\d{1,4}\.\d{1,2}) # this is currently set to less than 10GB data per day
    ''', re.VERBOSE).findall(testtext):
    count += 1
    sum += float(i)
print("You have used about", round(sum / 1000, 2), "GB of data in", count, "days.")
