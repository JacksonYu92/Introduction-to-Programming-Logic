import Ask

financiallyStable = Ask.forBoolean("are you fincnaially stable? (Yes/No)")
print financiallyStable

if not(financiallyStable):
    print "You need to work on your finances"
else: 
    print "Excellent work!"
