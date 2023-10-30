import turtle as t

from turtle import *

car = t.Turtle()

wn = t.Screen()

wn.bgcolor("black")

wn.setup(width=750, height=750)


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

def moveEmBois():
    


    for i in range(17):

        for tt in tortugas:

            tt.penup()
            tt.fd(30)

            
        
            if abs(tortugas[4].xcor() - tortugas[1].xcor() <20):
                if abs(tortugas[4].ycor()-tortugas[1].ycor()<20):

                    # tortugas[4].color("red")
                    # tortugas[1].color("red")


                    # tortugas[4].stamp()
                    # tortugas[1].stamp()

                    # tortugas[4].color("black")
                    # tortugas[1].color("black")

                    tortugas[4].hideturtle()
                    tortugas[1].hideturtle()

                    # tortugas[4].goto(10000,100000)
                    # tortugas[1].goto(10000,100000)


            
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
            
# end of functions

    


intersectionMaker()

spacing = 50

tortugas = []

turtleShapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horizColors = ["red", "blue", "green", "orange", "purple", "gold"]
vertColors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
coordinates = [[125,31,180],[31,-125,90],[-125,-31,0],[-31,125,270],[145,31,180],[-145,-31,0]]


for shape in turtleShapes:
    tt = Turtle(shape=shape)
    tortugas.append(tt)
    tt.penup()
    tt.fillcolor(horizColors.pop())
    z = turtleShapes.index(shape)
    x = coordinates[z][0]
    y = coordinates[z][1]
    tt.goto(x,y)
    tt.setheading(coordinates[z][2])

def teleport():

    for tt in tortugas:

        tt.hideturtle()
    
    for tt in tortugas:

        i = tortugas.index(tt)

        x = coordinates[i][0]
        y = coordinates[i][1]

        tt.goto(x,y)

        tt.showturtle()
    moveEmBois()



moveEmBois()
teleport()


# end of stuff

wn.mainloop()