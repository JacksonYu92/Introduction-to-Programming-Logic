"""
Name: Qichun Yu
Student ID: 0361980
Assignment No.3
Date: November 17, 2021
Description: Create a loop that will start at one, increment by eight and end at my grandma Zhuoxian's age 90.
"""
#Create variables to store number and quote
startedNumber = 1
incrementNumber = 8
ageOfZhuoxian = 90
quote = "Live your life and forget your age."

# Using for loop for increment
for number in range(startedNumber,ageOfZhuoxian, incrementNumber):
    print number
print quote

#Using while loop for increment
while startedNumber < ageOfZhuoxian:
    print startedNumber
    startedNumber += incrementNumber
print quote
