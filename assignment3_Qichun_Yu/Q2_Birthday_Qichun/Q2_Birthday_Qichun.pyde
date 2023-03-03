"""
Name: Qichun Yu
Student ID: 0361980
Assignment No.3
Date: November 17, 2021
Description: Count down from 100 to 0, if the number is equal to my birthday(Feb,4th), it will print Happy birthday with my name. If the number is equal it will print favorite. 
"""
# Create variables to store my birth month, birth day, and favorite number
birthMonth = 2
birthDay = 4
favoriteNumber = 8

for counter in range(100,-1,-1):
    if counter == birthMonth or counter == birthDay:
        if (counter % favoriteNumber) == 0:
            print "   Happy Birthday Qichun   Favorite" 
        else:
            print "   Happy Birthday Qichun"
    elif (counter % favoriteNumber) == 0:
        print "   Favorite"
    else:
        print counter

    
