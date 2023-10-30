# imports

import turtle as t

from turtle import *

import random as r

# end of imports

# game configuration/ global variables

wn = t.Screen()

wn.bgcolor("black")

wn.setup(width=750, height=750)

car = t.Turtle()

horizontalTurtles = []

verticalTurtles = []

shapes = ["arrow", "circle","classic", "square", "triangle","turtle" ]

colors = ["red", "blue", "green", "orange", "purple", "gold"]

vertColors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

coords = [[125,31,180],[31,-125,90],[-125,-31,0],[-31,125,270],[145,93,180],[-165,-93,0]]


# end of game configuration and variables

# turtles/objects intialization

for s in shapes:
    
    i = shapes.index(s)
    
    ht = Turtle(shape=s)
    
    horizontalTurtles.append(ht)
    ht.penup()
    ht.color(colors.pop())
    ht.hideturtle()
    ht.goto(coords[i][0],coords[i][1])
    ht.setheading(coords[i][2])
    ht.showturtle()
    
    if i != 5:
        i += 1
    
    vt = Turtle(shape=s)
    
    
    verticalTurtles.append(vt)
    vt.penup()
    vt.color(vertColors.pop())
    vt.hideturtle()
    vt.goto(coords[i][0],coords[i][1])
    vt.setheading(coords[i][2])
    vt.showturtle()


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
    
    
    for step in range(50):

        d = r.randint(5,15)
    
        for h in horizontalTurtles:
            
            for v in verticalTurtles:
                
                h.fd(d)
                v.fd(d)
                
                if (abs(h.xcor()-v.xcor()) < 2):
                    if (abs(h.ycor()-v.ycor()) < 2):
                        
                        h.fillcolor("grey")
                        v.fillcolor("grey")
                        
                        h.stamp()
                        v.stamp()
                        
                        horizontalTurtles.remove(h)
                        verticalTurtles.remove(v)
        
    for h in horizontalTurtles:
        for v in verticalTurtles:

            i = horizontalTurtles.index(h)

            x = coords[i][0]
            y = coords[i][1]


            h.goto(x,y)

            if i != 5:
                i+=1
            
            x1 = coords[i][0]
            y1 = coords[i][1]

            v.goto(x1,y1)
                
    

# end of functions

# main game loop
    
intersectionMaker()

moveCars()


# end of main loop

wn.mainloop()