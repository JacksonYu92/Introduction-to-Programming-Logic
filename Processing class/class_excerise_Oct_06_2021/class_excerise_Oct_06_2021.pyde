"""
Name: Qichun Yu
Date: October 6, 2021
Description: Working with the Ask.py file
"""
"""
def setup():
    size(1000,1000)
    myColor = color(150,53,204)
    fill(myColor) #Set the color to purple
    ellipse(100,100,50,50)
    rect(200,200,50,50)
    
    
def draw():
    #If the mouse is pressed then draw a line
    if (mousePressed):
        line(pmouseX, pmouseY, mouseX, mouseY)
"""        
import Ask

'''
yourName = Ask.forString("Please enter your first name")
print 'Your name is ' + yourName

yourAge = Ask.forInt('Please enter your age')
print 'You are ' + str(yourAge) + ' years old'

valueOfPi = Ask.forFloat('Please enter the value of Pi')
print 'You think Pi is ' + str(valueOfPi)


iLikeThisCourse = Ask.forBoolean('Do you like the course?')
print 'You said ' + str(iLikeThisCourse) + ' to liking the course'
'''

size(600,600)

nicePicture = loadImage('K-117.jpg')

image(nicePicture, random(10,500), random(10,500), 100,100)
