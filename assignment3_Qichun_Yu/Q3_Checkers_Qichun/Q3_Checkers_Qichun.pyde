"""
Name: Qichun Yu
Student ID: 0361980
Assignment No.3
Date: November 18, 2021
Description: Create a 8 x 8 checkerboard that alternate blue and green color. 
"""
#set up screen
size(640,640)
#Set up the width of Square
widthOfSquare = width/8

for counter in range(8):
    for counter1 in range(8):
        if ((counter + counter1) % 2 ==0):
            fill(0,0,255)
        else:
            fill(0,255,0)
        square(counter*widthOfSquare,counter1*widthOfSquare,widthOfSquare)
