"""
Name: Qichun Yu
Student ID: 0361980
Assignment No.2
Date: November 03, 2021
Description: Create a sketch to display a grid of 9 equal-sized squares. The background color change to green when the mouse reaches the middle top, the left middle, or the right bottom squares.
"""

def setup():
    # Set up size of the window
    size(300,300)

def draw():
    # Using black lines create a grid of 9 equal-sized squares, create a condition when the mouse reach one of the 3 chosen squares the background color change to green
    if (mouseX>=100 and mouseX<=200 and mouseY>=0 and mouseY<=100) or (mouseX>=0 and mouseX<=100 and mouseY>=100 and mouseY<=200) or (mouseX>=200 and mouseX<=300 and mouseY>=200 and mouseY<=300) :
        background(35,205,30)
        line(width/3,0,width/3,height)
        line(width/3*2,0,width/3*2,height)
        line(0,height/3,width,height/3)
        line(0,height/3*2,width,height/3*2)
    else:
        background(205)
        line(width/3,0,width/3,height)
        line(width/3*2,0,width/3*2,height)
        line(0,height/3,width,height/3)
        line(0,height/3*2,width,height/3*2)
