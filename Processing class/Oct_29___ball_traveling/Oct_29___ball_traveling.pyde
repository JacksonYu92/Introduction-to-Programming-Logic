x = 25;
circleMovement = 1


def setup():
    size(350,350)
    ellipse(x, 50, 25, 25)
    print width
    
def draw():
    global x, circleMovement
    background(192)
    """
    x += 1
    if x > width:
        x=0
    """
    x += circleMovement

    if x > width:
        #turn around and go back
        circleMovement = -1
    elif x < 0:
        circleMovement = 1
    
    #ellipse(x, height/2, 25, 25)
    ellipse(x, mouseY, 25, 25)
    
