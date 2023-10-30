import turtle as t

from turtle import *

car = t.Turtle()

wn = t.Screen()

wn.bgcolor("black")

wn.setup(width=750, height=750)


def whiteLines(x,y):
    car.penup()
    car.goto(x,y)
    car.pendown()
    car.pencolor("white")
    for i in range(13):
        car.pendown()
        car.fd(10)
        car.penup()
        car.fd(10)
    
def yellowLines(x,y):
    car.pencolor("yellow")
    car.penup()
    car.goto(x,y)
    car.pendown()
    car.fd(250)

def moveEmBois():
    
    distanceToMove = 30
    
    for step in range(17):
        for h in tortugasHori:
            for v in tortugasVert:
                h.fd(distanceToMove)
                v.fd(distanceToMove)
    
    for h in tortugasHori:
        for v in tortugasVert:
            h.hideturtle()
            v.hideturtle()

    
    for h in tortugasHori:
        i = tortugasHori.index(h)
        if i >= 1 and i <= 3:
            if i == 1:
                ind1 = 2
            elif i == 2:
                ind1 = 4
            elif i == 3:
                ind1 = 5
            
            
        for v in tortugasVert:
            
            x1 = teleportation[ind1][0]
            y1 = teleportation[ind1][1]
            
            j = tortugasVert.index(v)
            
            if j == 0:
                ind = 1
            elif j == 1:
                ind = 3
                
            h.penup()
            v.penup()
        
            x = teleportation[ind][0]
            y = teleportation[ind][1]

            
            h.goto(x1,y1)
            v.goto(x,y)

            h.setheading(teleportation[ind1][2])
            v.setheading(teleportation[ind][2])
    
    for h in tortugasHori:
        for v in tortugasVert:
            h.showturtle()
            v.showturtle()

def intersectionMaker():
    car.penup()

    car.goto(-375,125)

    car.color("lightgrey")

    car.speed(0)


    # out line of intersection
    for i in range(4):
        car.pendown()
        car.fd(250)
        car.lt(90)
        car.fd(250)
        car.rt(90)
        car.fd(250)
        car.rt(90)
        
    # end of outline

    # white dashed lines
    whiteLines(-375,60)

    whiteLines(-375,-60)
        
    car.penup()

    # yellow lines

    yellowLines(-375,0)

    yellowLines(125,0)

    whiteLines(125,60)

    whiteLines(125,-60)

    car.lt(90)

    yellowLines(0,125)

    whiteLines(60,125)

    whiteLines(-60,125)

    car.rt(180)

    yellowLines(0,-125)

    whiteLines(-60,-125)

    whiteLines(60,-125)

    # end of intersection maker

intersectionMaker()

spacing = 50

tortugasVert = []

tortugasHori = []

turtleShapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
colors = ["red", "blue", "green", "orange", "purple", "gold"]
# vertColors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
coordinates = [[125,31,180],[31,-125,90],[-125,-31,0],[-31,125,270],[145,31,180],[-145,-31,0]]
teleportation = [[345,31,180],[31,-345,90],[-345,-31,0],[-31,345,270],[375,31,180],[-375,-31,0]]


for shape in turtleShapes:
    z = turtleShapes.index(shape)
    tt = Turtle(shape=shape)
    if z == 0 or z == 2 or z == 4 or z == 5:
        tortugasHori.append(tt)
    else:
        tortugasVert.append(tt)
    
    tt.penup()
    tt.fillcolor(colors.pop())
    x = coordinates[z][0]
    y = coordinates[z][1]
    tt.goto(x,y)
    tt.setheading(coordinates[z][2])




moveEmBois()
moveEmBois()


# end of stuff

wn.mainloop()