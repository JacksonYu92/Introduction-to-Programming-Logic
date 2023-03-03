import Ask

yourAge = Ask.forInt("How old are you")
bossAge = Ask.forInt("How old is your boss")
areYouOlder = yourAge > bossAge

# display appropriate message based on who is older
if areYouOlder:
    #will only execute if you are older than your boss
    print "You are older than your boss!"
    print "You are: " + str(yourAge),
    print "Your boss is: " + str(bossAge)
    if yourAge>60:
        print "Wow " + str(yourAge) + " years old and still not retired! Come on give the youngsters a chance!"
    else:
        print "You still have some way to go before retirement"
else:
    #will only execute if you are younger than your boss
    print "You are younger than you boss!"
    print "You are: " + str(yourAge),
    print "Your boss is: " + str(bossAge)

print "Thank you for using our program"
