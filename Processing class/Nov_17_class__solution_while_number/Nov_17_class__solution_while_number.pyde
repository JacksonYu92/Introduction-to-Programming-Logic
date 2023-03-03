import Ask

numberOfQuestions = Ask.forInt("How many questions")
counter = 1
total = 0
chancesCounter = 0

while(counter <= numberOfQuestions):
    enteredNumber = Ask.forInt("Enter Number for question " + str(counter))
    while (enteredNumber < 0 and chancesCounter <3):
        enteredNumber = Ask.forInt("Re-Enter Number for question " + str(counter))
        chancesCounter += 1
    total = total + enteredNumber
    counter+=1

print("The total is: " + str(total))
print("The average is: " + str(total/numberOfQuestions))
