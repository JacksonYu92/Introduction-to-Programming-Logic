import Ask

numberOfQuestions = Ask.forInt("How many questions")
total = 0
number = 0
for question in range(numberOfQuestions):
    number = Ask.forInt("Enter Number for question " + str(question + 1))
    while number < 0:
        number = Ask.forInt("Re-enter Number for question " + str(question + 1))
    total += number

print "The total is: " + str(total)
average = total / numberOfQuestions
print "The average is: " + str(average)
    
