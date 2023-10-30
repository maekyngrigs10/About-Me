# --- Imports --- #
import turtle as t

from turtle import *

import time

import random as r

import winsound as win

# --- Global Configuration and Variables --- #

bodyParts = []
bodyParts2 = []

delay = 0.1

# --- Object Intialization --- #

# window set up

wn = t.Screen()
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.title("Snakey Dude: PVP")

# snake #1

snake1 = t.Turtle(shape="square")
snake1.speed(0)
snake1.penup()
snake1.color("blue")
snake1.goto(-100,-100)
snake1.direction="stop"

# snake #2

snake2 = t.Turtle(shape="square")
snake2.speed(0)
snake2.penup()
snake2.color("yellow")
snake2.goto(100,-100)
snake2.direction="stop"

# food turtle

food = t.Turtle(shape="circle")
food.speed(0)
food.shapesize(.5,.5)
food.color("red")
food.penup()
food.goto(0,0)

# script
script = t.Turtle()
script.color("lime green")
script.penup()
script.goto(-150,150)


# --- Main functions --- #

# Snake #1 movements
def up():
    if snake1.direction != "down":
        snake1.direction = "up"

def left():
    if snake1.direction != "right":
        snake1.direction = "left"

def right():
    if snake1.direction != "left":
        snake1.direction = "right"
def down():
    if snake1.direction != "up":
        snake1.direction = "down"

# Snake #2 movements
def snake2Up():
    if snake2.direction != "down":
        snake2.direction = "up"

def snake2Left():
    if snake2.direction != "right":
        snake2.direction = "left"

def snake2Right():
    if snake2.direction != "left":
        snake2.direction = "right"

def snake2Down():
    if snake2.direction != "up":
        snake2.direction = "down"

# -- main move functions -- #

# snake #1 move
def move():
    if snake1.direction == "up":
        snake1.sety(snake1.ycor()+20)

    elif snake1.direction == "down":
        snake1.sety(snake1.ycor()-20)

    elif snake1.direction == "right":
        snake1.setx(snake1.xcor()+20)

    elif snake1.direction == "left":
        snake1.setx(snake1.xcor()-20)

# snake #2 move
def snake2Move():
    if snake2.direction == "up":
        snake2.sety(snake2.ycor()+20)

    elif snake2.direction == "down":
        snake2.sety(snake2.ycor()-20)

    elif snake2.direction == "right":
        snake2.setx(snake2.xcor()+20)

    elif snake2.direction == "left":
        snake2.setx(snake2.xcor()-20)

# -- hide body parts functions -- #

# snake #1 hide body parts
def hideBodyParts():
    global bodyParts
    snake1.goto(-50,-50)
    snake1.direction = "stop"

    for eachPart in bodyParts:
        eachPart.goto(1000,1000)
    bodyParts = []

# snake #2 hide body parts
def hideBodyParts2():
    global bodyParts2
    snake2.goto(50,50)
    snake2.direction = "stop"

    for eachPart in bodyParts2:
        eachPart.goto(1000,1000)
    bodyParts2 = []

# --- Main Game Loop --- #

wn.onkeypress(up,"w")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.onkeypress(down,"s")
wn.onkeypress(snake2Up,"Up")
wn.onkeypress(snake2Left,"Left")
wn.onkeypress(snake2Right,"Right")
wn.onkeypress(snake2Down,"Down")

wn.listen()

# script writes the main screen

script.write("Snake 2.0: PVP",font=("Comic Sans MS",35,"bold"))
script.hideturtle()

while True:
    wn.update()

    # if either player hits the other

    for i in range(len(bodyParts2)):
        if int(snake1.distance(bodyParts2[i]) < 20):
            hideBodyParts()

    if snake1.distance(snake2) < 20:
        hideBodyParts()

    for i in range(len(bodyParts)):
        if int(snake2.distance(bodyParts[i]) < 20):
            hideBodyParts2()

    if snake2.distance(snake1) < 20:
        hideBodyParts2()
   
    # wall collision

    if snake1.xcor()>290 or snake1.xcor()<-290 or snake1.ycor()>290 or snake1.ycor()>290 or snake1.ycor()<-290:
        hideBodyParts()

    if snake2.xcor()>290 or snake2.xcor()<-290 or snake2.ycor()>290 or snake2.ycor()>290 or snake2.ycor()<-290:
        hideBodyParts2()

    # food collision

    if snake1.distance(food) < 20:
        script.clear()
        food.goto(r.randint(-290,290),r.randint(-290,290))

        win.Beep(1000,50)

        # add a body part
        part = t.Turtle(shape="square")
        part.speed(0)
        part.penup()
        part.color("blue")
        bodyParts.append(part)

    if snake2.distance(food) < 20:
        food.goto(r.randint(-290,290),r.randint(-290,290))
        win.Beep(1000,50)
        # add a body part
        part = t.Turtle(shape="square")
        part.color("yellow")
        part.speed(0)
        part.penup()
        bodyParts2.append(part)
    for i in range(len(bodyParts)-1,0,-1):
        x = bodyParts[i-1].xcor()
        y = bodyParts[i-1].ycor()
        bodyParts[i].goto(x,y)
    for i in range(len(bodyParts2)-1,0,-1):
        x = bodyParts2[i-1].xcor()
        y = bodyParts2[i-1].ycor()
        bodyParts2[i].goto(x,y)
    if len(bodyParts)>0:
        x = snake1.xcor()
        y = snake1.ycor()
        bodyParts[0].goto(x,y)
    if len(bodyParts2)>0:
        x = snake2.xcor()
        y = snake2.ycor()
        bodyParts2[0].goto(x,y)
    move()
    snake2Move()

    for part in bodyParts:
        if part.distance(snake1)<10:
            hideBodyParts()

    for part in bodyParts2:
        if part.distance(snake2)<10:
            hideBodyParts2()
           

    time.sleep(delay)

# --- End of All Movement --- #

wn.mainloop()