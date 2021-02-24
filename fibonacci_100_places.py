#!/usr/bin/python3
#############################
#    fibbonaci_100_places   #
#     github.com/kjh900     #
#############################

index = 1
temp0 = 0
temp1 = 1
counter = 1
while counter < 51:
    print(index, " - ", temp0)
    index += 1
    print(index, " - ", temp1)
    index += 1
    counter += 1
    temp0 += temp1
    temp1+=temp0
