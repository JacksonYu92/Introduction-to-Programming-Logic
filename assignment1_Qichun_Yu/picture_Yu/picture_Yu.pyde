"""
Name: Qichun Yu
Student ID: 0361980
Assignment No.1
Date: October 13,2021
Description: Create a sketch that draws Esplanade Riel Pedestrian Bridge.
"""
# Create a variable for the height of the bridge tower
heightOfTower = 300
# Create a variable for the height of the highest building
heightOfHighestBuilding = 200
# Create a variable for the height of the highest tree
heightOfHighestTree = 250
# Create a variable for the color of the bridge deck and foundation
colorOfDeckAndFoundation = 209
# Create a variable for the color of the building behind the bridge
colorOfBuilding = 50
#Create a variable for the color of the trees
colorOfTrees = 80

def setup():
    # Set up size of the window
    size(600, 500)

def draw():
    # Set up mouse location
    background(150, 150, 150)
    stroke(255,255,255)
    textSize(12)
    text("X:" + str(mouseX), width-40, 20)
    text("Y:" + str(mouseY), width-40, 40)
    
    # Creating buildings behind the bridge
    fill(colorOfBuilding)
    stroke(colorOfBuilding)
    rect(0,150,200,60)
    rect(30,210-heightOfHighestBuilding,60,heightOfHighestBuilding)
    rect(50,110,70,100)
    rect(120,70,50,140)
    line(145,60,145,70)
    rect(200,50,60,160)
    line(226,25,226,51)
    rect(430,160,200,50)
    
    # Using triangle() function to draw bridge Suspender Cables 
    fill(162)
    stroke(255,255,255)
    triangle(80,280,304,130,600,330)
    triangle(110,283,304,130,560,326)
    triangle(140,285,304,130,510,321)
    triangle(170,288,304,130,460,317)
    triangle(200,291,304,130,410,312)
    triangle(230,294,304,130,360,307)
    
    # Using ellipse() function to draw bridge tower
    fill(255)
    stroke(255)
    rotate(0.05)
    ellipse(310,160,6,heightOfTower)
    rotate(-0.05)

    # Using rect() function to draw bridge Deck
    fill(colorOfDeckAndFoundation)
    stroke(colorOfDeckAndFoundation)
    rotate(0.095)
    rect(102,273,530,6)
    
    # Creating the foundation of the bridge
    rect(102,275,30,30)
    rect(282,279,75,30)
    rect(520,276,30,30)
    
    #Creating the top of bridge plaza

    fill(87)
    stroke(87)
    triangle(306,228,320,213,335,229)
    stroke(255)
    fill(255)
    ellipse(319,211,5,5)
    #Creating the base of bridge plaza
    fill(70)
    stroke(70)
    ellipse(320,272,90,30)
    #Creating the middle of bridge plaza
    fill(255)
    stroke(209)
    rect(305,230,30,40)
    triangle(275,268,305,231,305,270)
    triangle(336,270,335,230,364,269)
    
    #Creating the trees
    fill(colorOfTrees)
    stroke(colorOfTrees)
    rotate(-0.095)
    ellipse(52,282,40,100)
    ellipse(30,290,60,97)
    ellipse(20,320,90,55)
    ellipse(150,460,60,90)
    ellipse(320,500,480,60)
    ellipse(280,460,55,110)
    ellipse(350,470,360,80)
    ellipse(550,480,120,heightOfHighestTree)
 
    


    

    
