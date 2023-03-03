"""
Name: Qichun Yu
Student ID: 0361980
Assignment No.2
Date: November 03, 2021
Description: Create a sketch to make a red line move across the screen.
"""
#Set a global variable x for the start position of the line
x = 0
lineMovement = 1

def setup():
    # Set up size of the window
    size(310,310)

def draw():
    global x, lineMovement
    # Set the line 3 pixels wide, color in red, background is a light gray
    background(211)
    strokeWeight(3)
    stroke(255,0,0)
    line(x,0,x,height)
    x += 1
    if x > width:
        x = 0

    
