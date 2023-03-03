"""
90 or over - A
80-89      - B
70-79      - C
below 70   - F
"""

studentMark = 90
letterGrade = "Unknown"

if (studentMark>= 90):
    letterGrade = "A"
elif (studentMark>=80):
    letterGrade = "B"
elif (studentMark>=70):
    letterGrade = "C"
else:
    letterGrade = "F"
    
print "Your grade was " + str(studentMark) + " which is a letter grade of " + letterGrade
