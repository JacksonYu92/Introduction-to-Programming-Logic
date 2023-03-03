def setup():
    size(400,400)
    widthInSetup = 120
    heightInSetup = 20
    howManyCircles = 20
    result = drawCircles(widthInSetup,heightInSetup,howManyCircles)
    print result

def drawCircles(width, height,numberOfCircles):
    # numberOfCircles = int(random(2,10))
    for circle in range(0, numberOfCircles):
        ellipse(random(10,390),random(10, 390),width,height)
        
    return str(numberOfCircles) + ' Circles drawn'
