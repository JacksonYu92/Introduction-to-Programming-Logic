"""
Name: Qichun Yu
Student ID: 0361980
Assignment No.2
Date: November 02, 2021
Description: Using the Ask.py file to ask the ages of three friends and check if their ages are equally apart. 
"""
import Ask
# Create variables to store ages of my friends
ageOfLuke = Ask.forInt("Friend Luke's age: ")
ageOfLumen = Ask.forInt("Friend Lumen's age: ")
ageOfCee = Ask.forInt("Friend Cee's age: ")
ageEquallyApart = True
ageDifference = 0

#Find the youngest, middle and oldest first, then compare the age difference to check if ages are equally apart
if ageOfLuke < ageOfLumen and ageOfLuke < ageOfCee:
    if ageOfLumen < ageOfCee:
        if (ageOfLumen - ageOfLuke) != (ageOfCee - ageOfLumen):
            ageEquallyApart = False
        else: 
            ageDifference = ageOfLumen - ageOfLuke
    else:
        if (ageOfCee - ageOfLuke) != (ageOfLumen - ageOfCee):
            ageEquallyApart = False
        else:
            ageDifference = ageOfCee - ageOfLuke
elif ageOfLumen < ageOfCee:
    if ageOfLuke < ageOfCee:
        if (ageOfLuke - ageOfLumen) != (ageOfCee - ageOfLuke):
            ageEquallyApart = False
        else:
            ageDifference = ageOfLuke - ageOfLumen
    else:
        if (ageOfCee - ageOfLumen) != (ageOfLuke - ageOfCee):
            ageEquallyApart = False
        else:
            ageDifference = ageOfCee - ageOfLumen
else:
    if ageOfLuke < ageOfLumen:
        if (ageOfLuke - ageOfCee) != (ageOfLumen - ageOfLuke):
            ageEquallyApart = False
        else:
            ageDifference = ageOfLuke - ageOfCee
    else:
        if (ageOfLumen - ageOfCee) != (ageOfLuke - ageOfLumen):
            ageEquallyApart = False
        else:
            ageDifference = ageOfLumen - ageOfCee

# Display the appropriate message based on whether they are equal or not            
if ageEquallyApart:
    print "The ages of my friends are " + str(ageDifference) + " years apart."
else:
    print "My friends ages are not the same."
