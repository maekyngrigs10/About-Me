# import

import turtle as t

from turtle import *

import time

import random as r

# game config and globals

delay = 0.1

bodyParts = []

# object creation

wn = t.Screen()
wn.bgcolor("grey")
wn.setup(width=600,height=600)

head = t.Turtle(shape="square")
head.speed(0)
head.penup()
head.direction = "stop"

food = t.Turtle()
food.shape("circle")
food.speed(0)
food.shapesize(.5,.5)
food.color("red")
food.penup()
food.goto(100,100)

# functions

def ups():
    # in mazerunner we used setheading
    
    if head.direction != "down":
        head.direction = "up"
        
def left():
    # in mazerunner we used setheading
    
    if head.direction != "right":
        head.direction = "left"

def right():
    # in mazerunner we used setheading
    
    if head.direction != "left":
        head.direction = "right"

def downs():
    # in mazerunner we used setheading
    
    if head.direction != "up":
        head.direction = "down"
    
def move():
    if head.direction == "up":
        head.sety(head.ycor()+20)
    if head.direction == "down":
        head.sety(head.ycor()-20)
    if head.direction == "right":
        head.setx(head.xcor()+20)
    if head.direction == "left":
        head.setx(head.xcor()-20)

def hideBodyParts():
    
    global bodyParts
    
    head.goto(0,0)
    head.direction = "stop"
    for eachPart in bodyParts:
        eachPart.goto(1000,1000)
    bodyParts = []

# events

wn.onkeypress(ups,"w")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.onkeypress(downs,"s")

wn.listen()

# mainloop

while True:
    
    wn.update()     # updates/refreshes the screen
    
    # border collision
    
    if head.xcor() == 300 or head.xcor() == -300 or head.ycor() == 300 or head.ycor() == -300:
        head.goto(0,0)
        head.direction = "stop"    
        hideBodyParts()
        
    # Collide with the food
    if head.distance(food) < 20:    # returns the distance between the objects
        # food moves
        
        x = r.randint(-290,290)
        y = r.randint(-290,290)
        
        food.goto(x,y)
        
        # grow a body parts
        part = t.Turtle(shape="turtle")
        part.speed(0)
        part.penup()
        bodyParts.append(part)
        
    
    # move the body parts
    for i in range(len(bodyParts)-1,0,-1):
        x = bodyParts[i-1].xcor()
        y = bodyParts[i-1].ycor() 
        bodyParts[i].goto(x,y)
    move()
    
    # move the neck to the head
    
    if len(bodyParts)>0:
        x = head.xcor()
        y = head.ycor()
        bodyParts[0].goto(x,y)
    
    # did we hit ourselves? or did we eat our body parts
    
    for i in range(len(bodyParts)-1,0,-1):
        if bodyParts[i].xcor() == head.xcor() and bodyParts[i].ycor() == head.ycor():
            hideBodyParts()
    
    
    time.sleep(delay)

# end of all movement

wn.mainloop()