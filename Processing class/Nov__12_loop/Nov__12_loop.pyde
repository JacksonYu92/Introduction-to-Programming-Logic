"""
counter = 200
stopValue = 0
print 'Loop starting'
while counter > stopValue:
    print "    " + str(counter)
    counter -= 1
print 'Loop ending'
"""
"""
for counter in range(100, 5,-3):
    print counter
"""
"""
iterationCount = 0
for counter1 in range(0,25):
    for counter2 in range(0,20):
        print counter2 , 
        iterationCount += 1
    print
print "The loops iterated " + str(iterationCount) + " times."
"""
"""
star = "*"
for counter in range(1,6):
    print star * counter,
    print
"""

for counter in range (0,5):
    for counter2 in range (0,counter):
        print "*",
    print " "
for counter in range (5,0,-1):
    for counter2 in range (0,counter):
        print "*",
    print " "



    
    
