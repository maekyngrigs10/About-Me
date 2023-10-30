# imports

import turtle as t

from turtle import *

import random as r

# configuration and global variables

courtHeight = 600
courtWidth = 1000
ballSize = 15
paddleWidth = 50
fontSetup = ("Times New Roman",50,"normal")
leftScore = 0
rightScore = 0

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

# left/red player

leftPlayer = t.Turtle("square")
leftPlayer.color("red")
leftPlayer.penup()
leftPlayer.speed(0)
leftPlayer.setx(-courtWidth/2)
leftPlayer.turtlesize(4,1,1)

# lscore

lScore = t.Turtle(visible=False)
lScore.speed(0)
lScore.penup()
lScore.color("white")
lScore.setposition(-courtWidth/4,courtHeight/4)
lScore.write(leftScore,font=fontSetup)

# right/blue player

rightPlayer = t.Turtle("square")
rightPlayer.color("blue")
rightPlayer.penup()
rightPlayer.speed(0)
rightPlayer.setx(courtWidth/2)
rightPlayer.turtlesize(4,1,1)

# rscore

rScore = t.Turtle(visible=False)
rScore.speed(0)
rScore.penup()
rScore.color("white")
rScore.setposition(courtWidth/4,courtHeight/4)
rScore.write(rightScore,font=fontSetup)


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
    
def moveBall():
    
    global rightScore
    global leftScore
    
    ball.fd(20)
    
    x,y = ball.position()
    
    # bounce off the walls
    
    if y >( courtHeight/2-ballSize) or y<(-courtHeight/2-ballSize):
        ball.setheading(-ball.heading())
        
    # bounce off the left or right wall
    elif x >( courtWidth/2-ballSize) or x<(-courtWidth/2-ballSize):
        ball.setheading(ball.heading()+r.randint(150,210))
        if x > courtWidth/2:
            leftScore += 1
            lScore.clear()
            lScore.write(leftScore,font=fontSetup)
        elif x < -courtWidth/2:
            rightScore += 1
            rScore.clear()
            rScore.write(rightScore,font=fontSetup)
        resetBall()
    else:
        paddleCollision(leftPlayer,ball)
        paddleCollision(rightPlayer,ball)
    
    wn.ontimer(moveBall,20)

def upLeft():
    if leftPlayer.ycor()< (courtHeight/2-paddleWidth):
        leftPlayer.sety(leftPlayer.ycor()+20)

def downLeft():
    if leftPlayer.ycor() > (-courtHeight/2+paddleWidth):
        leftPlayer.sety(leftPlayer.ycor()-20)
      
def upRight():
    if rightPlayer.ycor() < (courtHeight/2-paddleWidth):
        rightPlayer.sety(rightPlayer.ycor()+20)

def downRight():
    if rightPlayer.ycor() > (-courtHeight/2+paddleWidth):
        rightPlayer.sety(rightPlayer.ycor()-20)
    
def paddleCollision(paddle,b):
    if paddle.distance(b)<paddleWidth:
        b.setheading(b.heading()+r.randint(150,210))
        if b.xcor()>0:
            b.setx(b.xcor()-5)
        else:
            b.setx(b.xcor()+5)
        b.fd(10)
# events

wn.onkeypress(resetBall,"r")
wn.onkeypress(upLeft,"w")
wn.onkeypress(downLeft,"s")
wn.onkeypress(upRight,"Up")
wn.onkeypress(downRight,"Down")


wn.listen()

makeCourt()

moveBall()

# end of loop

wn.mainloop()