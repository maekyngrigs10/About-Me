# import

import turtle as t

from turtle import *

import time

import random as r

import winsound as win

# game config and globals

delay = 0.1

bodyParts = []

colors = ["red","orange","yellow","green","blue","purple","pink","white","brown","cyan"]

timer = 0
interval = 1000

game = False

dis = 1

posX = 0
posY = 0

fontSetup = ("Comic Sans MS",15,"normal")

console = '''# ------- Directions  ------- #
# -- press 'w' to  move up -- #
# - press 's' to  move down - #
# - press 'a' to  move left - #
# - press 'd' to move right - #
# --------------------------- #
'''

# object creation

wn = t.Screen()
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.title("Snakey Dude")

head = t.Turtle(shape="square")
head.speed(0)
head.penup()
head.direction = "stop"
head.color("light grey")

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
    global colors
    
    # ---- ! uncomment this if you want to see the change color on move or else it lags like crazy ! ---- #
    
    # color = r.choice(colors)

    # for i in range(len(bodyParts)-1,0,-1):
    #     x = bodyParts[i-1].xcor()
    #     y = bodyParts[i-1].ycor() 
    #     bodyParts[i].goto(x,y)
    #     bodyParts[i].setheading(head.heading())
    #     bodyParts[i].color(color)
    
    # head.color(color)

    if head.direction == "up":
        head.sety(head.ycor()+20+dis)
        head.setheading(90)

    if head.direction == "down":
        head.sety(head.ycor()-20-dis)
        head.setheading(270)

    if head.direction == "right":
        head.setx(head.xcor()+20+dis)
        head.setheading(0)

    if head.direction == "left":
        head.setx(head.xcor()-20-dis)
        head.setheading(180)

        

def hideBodyParts():
    global dis
    
    global bodyParts
    
    head.goto(0,0)
    head.direction = "stop"
    for eachPart in bodyParts:
        eachPart.goto(1000,1000)

    dis = 1
        
    bodyParts = []

# here is where the time thing will go
def updateTimer():
    
    global timer
    global game    

    # while game == True:
    timer += 1
    if 25//timer == 0:
        x = r.randint(-290,290)
        y = r.randint(-290,290)
        food.goto(x,y)
        timer = 1

# events

wn.onkeypress(ups,"w")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.onkeypress(downs,"s")

wn.listen()

# mainloop
print(console)



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
        
        x = r.randint(-280,280)
        y = r.randint(-280,280)
        food.goto(x,y)

        dis += 1
        
        win.Beep(1000,50)
        
        color =  r.choice(colors)
        # grow a body parts
        part = t.Turtle(shape="square")
        part.speed(0)
        part.penup()
        part.color(color)
        bodyParts.append(part)

        
        head.color("light grey")
    # # # move the body parts
    for i in range(len(bodyParts)-1,0,-1):
        x = bodyParts[i-1].xcor()
        y = bodyParts[i-1].ycor()
        bodyParts[i].goto(x,y)
        bodyParts[i].setheading(head.heading())
        bodyParts[i].color(color)
        bodyParts[i].speed(0)

    move()
    
    # move the neck to the head
    
    if len(bodyParts)>0:
        x = head.xcor()
        y = head.ycor()
        bodyParts[0].goto(x,y)
        bodyParts[0].setheading(head.heading())
    
    # did we hit ourselves? or did we eat our body parts
    
    for i in range(len(bodyParts)-1,0,-1):
        if bodyParts[i].xcor() == head.xcor() and bodyParts[i].ycor() == head.ycor():
            hideBodyParts()
    
    
    time.sleep(delay)

    wn.ontimer(updateTimer,interval)

# end of all movement

wn.mainloop()