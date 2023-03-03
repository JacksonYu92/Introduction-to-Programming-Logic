"""
Name: Qichun Yu
Student ID: 0361980
Assignment No.1
Date: October 12, 2021
Description: Using the Ask.py file to collect user's name, age, height, weight, home country, favorite sport, and favorite food. Display the comparison of my information in the end.  
"""
import Ask
# Create a variable to store my full name
myFullName = "Qichun Yu"
# Create a variable to store my age
myAge = 29
# Create a variable to store my height
myHeight = 1.75
# Create a variable to store my weight
myWeight = 148.5
# Create a variable to store my home country
myHomeCountry = "China"
# Create a variable to store my favorite sport
myFavoriteSport = "basketball"
# Create a variable to store my favorite food
myFavoriteFood = "sushi"

# Using Ask.py to get user's full name and store it into a variable
yourFullName = Ask.forString("Please enter your full name: ")
# Using Ask.py to get user's age and store it into a variable
yourAge = Ask.forInt("What is your age?")
# Using Ask.py to get user's height and store it into a variable
yourHeight = Ask.forFloat("What is your height in meters?")
# Using Ask.py to get user's weight and store it into a variable
yourWeight = Ask.forFloat("What is your weight in pounds?")
# Using Ask.py to get user's home country and store it into a variable
yourHomeCountry = Ask.forString("Where are you from?")
# Using Ask.py to get user's favorite sport and store it into a variable
yourFavoriteSport = Ask.forString("What is your favorite sport?")
# Using Ask.py to get user's favorite food and store it into a variable
yourFavoriteFood = Ask.forString("What is your favorite food?")

# Print out my corresponding attribute and user's attribute to the console
print "My name is " + myFullName + ". Nice to meet you, " + yourFullName + "."
print "I am " + str(myAge) + " years old, your are " + str(yourAge) + " years old."
print "My height is " + str(myHeight) + " meters, you are " + str(yourHeight) + " meters tall."
print "My weight is " + str(myWeight) + " pounds, you are " + str(yourWeight) + " pounds."
print "I come from " + myHomeCountry + ", you are from " + yourHomeCountry + "."
print "My favorite sport is " + myFavoriteSport + ", your favorite sport is " + yourFavoriteSport + "."
print "My favorite food is " + myFavoriteFood + ", your favorite food is " + yourFavoriteFood + "."
