"""
Name: Jackson Yu
Date: October 5, 2021
Description: In class examples using Python
"""

'''
This is Multipleline comment
'''


#set the size of the canvas
size(400,600)

strokeWeight(20)
point(200,300)
strokeWeight(3)
line(100,100,300,300)
stroke(105,168,50)
fill(168,50,52)
rect(30,20,155,55,27)
line(50,50,100,100)

#Print message to the screen
print "Hello World!"

counter = 0
print type(counter)
counter = 3.3
print type(counter)

firstName = "Jackson"
lastName = "Yu"
myFullName = firstName + ' ' + lastName
print myFullName
print "myFullName"
print(myFullName)

print type(myFullName)


number1 = 3
number2 = 4.1
number3 = 0
number3 = str(number1*number2)
print(number3)
print type(number3)
number3 = number3*2
print number3
print type(number3)

pi=3.14
print 'This is pi:' + str(pi)
print '\"Frodo\n Baggins\"'
