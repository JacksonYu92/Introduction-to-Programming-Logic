#ielts - This program will tell an international whether they meet the english requirement for RRC

overallScore = 6.0
readingScore = 6.0
writingScore = 6.0
listeningScore = 6.5
speakingScore = 5.5

#To gain admission a student must score at least 6.0 on all tests and overall score must be 6.0

averageOfInvididualScores = round((readingScore + writingScore + listeningScore + speakingScore)/4, 1)
print "Average of individual scores: " + str(averageOfInvididualScores)
print "Overall Score: " + str(overallScore)

"""
if readingScore>= 6.0 and writingScore>=6.0 and listeningScore>=6.0 and speakingScore>=6.0 and overallScore>=6.0:
    print "Welcome to RRC"
else: 
    print "Sorry"
"""
#To gain admission a student must score at least 6.0 on all tests Or overall score must be 6.0

# averageScore = round((readingScore + writingScore + listeningScore + speakingScore)/4, 1)
"""
if overallScore>=6.0 or (readingScore>= 6.0 and writingScore>=6.0 and listeningScore>=6.0 and speakingScore>=6.0):
    print "Welcome to RRC"
else: 
    print "Sorry"
"""    
#To gain admission a student must score at least 6.0 on all individual tests Or the overall score must be 6.0
if averageOfInvididualScores>=6.0 or overallScore>=6.0:
    print"Welcom to RRC"
else:
    print "Sorry"







# if averageScore >= overallScore:
#     print "Congruation, your average score is " + str(averageScore) + ". You meet the English requirement for RRC"
# else:
#     print "Sorry, your average score is " + str(averageScore) + ". You fail to meet the English requirement for RRC"
