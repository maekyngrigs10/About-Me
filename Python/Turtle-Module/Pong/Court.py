# imports

import turtle as t

from turtle import *

# configuration and global variables



# object creation
wn = t.Screen()
wn.bgcolor("black")
wn.setup(width=1000,height=1000)

pete = t.Turtle()
pete.speed(0)
pete.color("white")
pete.penup()


# main functions

def makeCourt():
    
    pete.penup()    
    pete.goto(-500,300)
    pete.pensize(5)
    pete.pendown()
    
    for i in range(2):
        pete.fd(1000)
        pete.rt(90)
        pete.fd(600)
        pete.rt(90)
    
    pete.penup()
    pete.goto(0,300)
    pete.setheading(270)
    pete.pensize(2)
    pete.pendown()
    
    for i in range(12):
        pete.fd(30.5)
        pete.penup()
        pete.fd(21)
        pete.pendown()
    

# main game loop

makeCourt()

# end of loop

wn.mainloop()