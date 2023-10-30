import turtle as t

from turtle import *

car = t.Turtle

wn = t.Screen()

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


intersectionMaker()
#Turtles
horizontalTurts = []
verticalTurts = []
# use interesting shapes and colors
turtleShapes = ["arrow", "turtle", "circle"]
horizColors = ["red", "blue", "green"]
vertColors = ["darkred", "darkblue", "lime"]
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
horizontalTurts[0].goto(-200,25)
horizontalTurts[1].goto(-200,-25)
horizontalTurts[2].setheading(180)
horizontalTurts[2].goto(350,-75)
verticalTurts[0].goto(25,250)
verticalTurts[1].goto(75,250)
verticalTurts[2].goto(125,-300)
verticalTurts[2].setheading(90)
#moving the turtles
distanceToMove=2
collisionDistance=20
# for step in range(100):
#     for h in horizontalTurts:
#         for v in verticalTurts:
#             print(h,v)
#             h.fd(distanceToMove)
#             v.fd(distanceToMove)
#             #check for collision
#             if (abs(h.xcor() - v.xcor()) < collisionDistance):
#                 if (abs(h.ycor()-v.ycor()) < collisionDistance):
#                     print("COLLISION",h,v)
#                     h.fillcolor("gray")
#                     v.fillcolor("gray")
#                     horizontalTurts.remove(h)       #remove from the list stop stop them moving, cant move something not in the list
#                     verticalTurts.remove(v) 
wn.mainloop()