# imports

import turtle as t

from turtle import *

import random as r

# configuration and global variables

courtHeight = 600
courtWidth = 1000
ballSize = 15

# object creation
wn = t.Screen()
wn.bgcolor("black")
wn.setup(width=1000,height=1000)

border = t.Turtle(visible=False) #same as hideTurtle
border.speed(0)
border.color("white")
border.penup()



ball = t.Turtle("circle")
ball.color("white")
ball.penup()
ball.speed(0)


# main functions

def makeCourt():
    
    border.penup()    
    border.goto(-500,300)
    border.pensize(5)
    border.pendown()
    
    for i in range(2):
        border.fd(1000)
        border.rt(90)
        border.fd(600)
        border.rt(90)
    
    border.penup()
    border.goto(0,300)
    border.setheading(270)
    border.pensize(2)
    border.pendown()
    
    for i in range(12):
        border.fd(30.5)
        border.penup()
        border.fd(21)
        border.pendown()
    
def resetBall():
    ball.setposition(0,0)
    
def move():
    ball.fd(20)
    
    x,y = ball.position()
    
    # bounce off the walls
    
    if y >( courtHeight/2-ballSize) or y<(-courtHeight/2-ballSize):
        ball.setheading(-ball.heading())
        
    # bounce off the left or right wall
    elif x >( courtWidth/2-ballSize) or x<(-courtWidth/2-ballSize):
        ball.setheading(ball.heading()+r.randint(150,210))
    wn.ontimer(move,20)

# events

wn.onkeypress(resetBall,"r")
wn.listen()

makeCourt()

move()

# end of loop

wn.mainloop()