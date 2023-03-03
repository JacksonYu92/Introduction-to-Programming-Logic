"""
Name: Qichun Yu
Student ID: 0361980
Assignment No.4
Date: November 30, 2021
Description: Build a program to determine which of two entered numbers is closest to 27 without going over.
"""
import Ask

def setup():
    #create variable to ask user to enter two numbers
    firstNumber = Ask.forInt("Please enter the first number: ")
    secondNumber = Ask.forInt("Please enter the second number: ")
    value = returnedValue(firstNumber, secondNumber)
    print("The value returned is " + str(value))
    
def returnedValue(num1, num2):
    #All of not acceptive conditions return 0
    if (num1 > 27 and num2 > 27) or num1 <= 0 or num2 <= 0:
        return 0
    else:
        #If the number is bigger than 27, return the other number
        if num1 > 27:
            return num2
        elif num2 > 27:
            return num1
        else:
            #return the one closest to 27
            if (27-num1) <= (27-num2):
                return num1
            else:
                return num2
        
    
