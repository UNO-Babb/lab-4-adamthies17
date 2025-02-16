#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(larry, sides):
    for s in range(sides):
        larry.forward(50)
        larry.right(360/sides)
        
def fillCorner(gary, corner):
    drawSquare(gary, 150)
    if corner == 1:
        gary.begin_fill()
        drawSquare(gary, 75)
        gary.end_fill()
    elif corner == 2:
        gary.forward(75)
        gary.begin_fill()
        drawSquare(gary, 75)
        gary.end_fill()
    elif corner == 4:
        gary.right(90)
        gary.forward(75)
        gary.left(90)
        gary.begin_fill()
        drawSquare(gary, 75)
        gary.end_fill()
    elif corner == 3:
        gary.right(90)
        gary.forward(150)
        gary.left(90)
        gary.forward(75)
        gary.left(90)
        gary.begin_fill()
        drawSquare(gary, 75)
        gary.end_fill()
        
def squaresInSquares(gus, squares):
    theSize = 20
    for j in range(squares):
        drawSquare(gus, theSize)
        gus.penup()
        gus.left(135)
        gus.forward(20)
        gus.right(135)
        gus.pendown()
        theSize= theSize + 29
        
        
        
        
        
        
def main():
    myTurtle = turtle.Turtle()
    
    
   
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 4) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
