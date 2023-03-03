"""
Name: Qichun Yu
Student ID: 0361980
Assignment No.4
Date: November 30, 2021
Description: Create a program to tell the user whether they passed a course or not.
"""
import Ask



#Create a function to check whether score is higher than 60
def checkPassed(mark):
    if mark >= 60:
        return True
    else: 
        return False 

#Create Function to check the amout difference
def calculateDifference(mark):
    difference = abs(mark - 60)
    return difference

#Create Function to show happy face when passed
def showHappyFace(amount):
    happyFace =loadImage('happy_face.PNG')
    for counter in range(amount):
        image(happyFace, random(10,500),random(10,550),50,50)

#Create Function to show unhappy face when failed
def showUnhappyFace(amount):
    unhappyFace =loadImage('unhappy_face.PNG')
    for counter in range(amount):
        image(unhappyFace, random(10,500),random(10,550),50,50)

def setup():
    size(600,600)
    studentGrade = Ask.forInt("Please enter the student grade: ")
    # If the user enter a mark outside the valid range(1-100), re-prompted to enter the mark again
    while (studentGrade < 0 or studentGrade > 100):
        studentGrade = Ask.forInt("Please enter the student grade: ")
    studentPassed = checkPassed(studentGrade)    
    scoreDifference = calculateDifference(studentGrade)
    if studentPassed:
        #One happy face will display when student score is 60
        if scoreDifference == 0:
            showHappyFace(1)
        else:
            showHappyFace(scoreDifference)
    else:
        showUnhappyFace(scoreDifference)
