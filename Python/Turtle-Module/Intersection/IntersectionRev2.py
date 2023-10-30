# imports

import turtle as t

from turtle import *

# end of imports

# game configuration/ global variables

wn = t.Screen()

wn.bgcolor("black")

wn.setup(width=750, height=750)

car = t.Turtle()

horizontalTurts = []

verticalTurts = []




# end of game configuration and variables

# turtles/objects intialization

turtleShapes = ["arrow", "turtle", "circle", "square"]
horizColors = ["red", "blue", "green", "orange"]
vertColors = ["darkred", "darkblue", "lime", "salmon"]
spacing=100
for shape in turtleShapes:
    ht = Turtle(shape=shape)
    horizontalTurts.append(ht)
    ht.penup()
    ht.fillcolor(horizColors.pop())
    ht.setheading(0)
    vt = Turtle(shape=shape)
    verticalTurts.append(vt)
    vt.penup()
    vt.fillcolor(vertColors.pop())
    vt.setheading(270)
    spacing+=25

# end of turtle/object intialization

car.speed(0)

# functions

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
    
def intersectionMaker():
    car.penup()

    car.goto(-375,125)

    car.color("lightgrey")


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

def moveCars():

    coords = [[125,31,180],[31,-125,90],[-125,-31,0],[-31,125,270],[145,93,180],[-165,-93,0]]

    
    d = 15
    
    for step in range(25):
    
        for h in horizontalTurts:

            i = horizontalTurts.index(h)

            x = coords[i][0]
            y = coords[i][1]
        
            h.goto(x,y)

            h.setheading(coords[i][2])
            
            for v in verticalTurts:

                j = horizontalTurts.index(v)

                x1 = coords[j][0]
                y1 = coords[j][1]

                v.goto(x1,y1)

                v.setheading(coords[j][2])
                
                h.fd(d)
                v.fd(d)
                
                # if (abs(h.xcor()-v.xcor()) < 2):
                #     if (abs(h.ycor()-v.ycor()) < 2):
                        
                #         h.fillcolor("grey")
                #         v.fillcolor("grey")
                        
                #         h.stamp()
                #         v.stamp()
                        
                #         horizontalTurts.remove(h)
                #         verticalTurts.remove(v)
                
    

# end of functions

# main game loop
    
intersectionMaker()

moveCars()


# end of main loop

wn.mainloop()