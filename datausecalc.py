#!/usr/bin/python3

# datausecalc.py
# kjh9000@github.com

'''My ISP only gives me the data used for each day, not the total for the 
cycle. This program extracts the data used from the wall of text provided,
adds it and returns the sum and the number of days into the plan one is.
'''

import re

testtext= '''
# Begin edit

Replace this wall of example text with your own. In the example, the cycle
starts on 03/03/2021, and the current day is 03/09/2021. Double check what
days are used in the calculation, since this is prone to fence post errors
that affect the days count.

03/09/2021 			18.85 MB 	Custom Plan 	-
03/08/2021 			630.98 MB 	Custom Plan 	-
03/07/2021 			654.05 MB 	Custom Plan 	-
03/06/2021 			717.54 MB 	Custom Plan 	-
03/05/2021 			939.73 MB 	Custom Plan 	-
03/04/2021 			660.44 MB 	Custom Plan 	-
03/03/2021 			1014.72 MB 	Custom Plan 	-
# End of edit
'''

# extracts the data and adds it, then returns the sum along with the days
sum = 0
count = 0
for i in re.compile(r'''
    (\d{1,5}\.\d{1,2}) # This currently will search for data up to not including 10GB per day
    ''', re.VERBOSE).findall(testtext):
    count += 1
    sum += float(i)
print("You have used about", round(sum / 1000, 2), "GB of data in", count, "days.")
