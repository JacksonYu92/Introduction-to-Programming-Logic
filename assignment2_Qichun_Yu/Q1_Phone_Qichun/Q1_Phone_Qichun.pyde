"""
Name: Qichun Yu
Student ID: 0361980
Assignment No.2
Date: November 02, 2021
Description: Using the Ask.py file to question the user for the conditions and then decide whether the user should answer the phone or not. 
"""
import Ask
# Create variables to store questions
isMorning = Ask.forBoolean("Is it morning?")
isMom = Ask.forBoolean("Is it Mom?")
isAsleep = Ask.forBoolean("Are you asleep?")
answerYourPhone = True

#Check the conditions and provide the correct responses
if isAsleep == True or (not(isMom) and isMorning):
    answerYourPhone = False
    print "Morning: " + str(isMorning) + "; Mom: " + str(isMom) + "; Asleep: " + str(isAsleep) + "; I don't answer..."
else:
    print "Morning: " + str(isMorning) + "; Mom: " + str(isMom) + "; Asleep: " + str(isAsleep) + "; Hello..."
