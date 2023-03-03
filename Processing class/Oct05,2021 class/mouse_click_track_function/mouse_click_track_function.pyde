
def setup():
    size(450, 450)

def draw():
    background(150, 150, 150)
    stroke(255,0,0)
    textSize(12)
    text("X:" + str(mouseX), width-40, 20)
    text("Y:" + str(mouseY), width-40, 40)
    
    #Create your shape here
    rect(250, 190, 50, 75)#example
    
