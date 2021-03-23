#!/usr/bin/python3

# datausecalc.py
# kjh9000@github.com
'''My ISP only gives me the data used for each day, not the total.
This program extracts the data used from the wall of text provided, adds it
and returns the sum and the number of days into the plan one is.
'''
import re

testtext= '''
03/23/2021 			0.23 MB 	Custom Plan 	-
03/22/2021 			1073.47 MB 	Custom Plan 	-
03/21/2021 			629.51 MB 	Custom Plan 	-
03/20/2021 			831.77 MB 	Custom Plan 	-
03/19/2021 			898.57 MB 	Custom Plan 	-
03/18/2021 			898.72 MB 	Custom Plan 	-
03/17/2021 			754.21 MB 	Custom Plan 	-
03/16/2021 			1062.01 MB 	Custom Plan 	-
03/15/2021 			646.99 MB 	Custom Plan 	-
03/14/2021 			805.52 MB 	Custom Plan 	-
03/13/2021 			807.76 MB 	Custom Plan 	-
03/12/2021 			879.24 MB 	Custom Plan 	-
03/11/2021 			677.79 MB 	Custom Plan 	-
03/10/2021 			745.45 MB 	Custom Plan 	-
03/09/2021 			888.85 MB 	Custom Plan 	-
03/08/2021 			630.98 MB 	Custom Plan 	-
03/07/2021 			654.05 MB 	Custom Plan 	-
03/06/2021 			717.54 MB 	Custom Plan 	-
03/05/2021 			939.73 MB 	Custom Plan 	-
03/04/2021 			660.44 MB 	Custom Plan 	-
03/03/2021 			1014.72 MB 	Custom Plan 	-
'''

# extracts the data and adds it, then returns the sum along with the days
# note the current day counts as one complete day
sum = 0
count = 0
for i in re.compile(r'''
    (\d{1,4}\.\d{1,2}) # this is currently set to less than 10GB data per day
    ''', re.VERBOSE).findall(testtext):
    count += 1
    sum += float(i)
print("You have used about", sum, "GB of data in", count, "days.")
