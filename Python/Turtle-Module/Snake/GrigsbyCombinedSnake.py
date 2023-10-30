# import

import turtle as t

from turtle import *

import time

import random as r

import winsound as win

# game config and globals

delay = 0.1

bodyParts = []
bodyParts2 = []

colors = ["red","orange","yellow","green","blue","purple","pink","white","brown","cyan"]

timer = 0
interval = 1000

game = False

dis = 1

posX = 0
posY = 0

mode = "Home"

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

# snake #2

snake2 = t.Turtle(shape="square")
snake2.speed(0)
snake2.penup()
snake2.color("yellow")
snake2.goto(100,-100)
snake2.direction="stop"
snake2.hideturtle()

# functions
def hardMode():
    global mode
    mode = "Hard"

def regMode():
    global mode
    mode = "Reg"

def PVPMode():
    global mode

    mode = "PVP"
    snake2.showturtle()

    wn.onkeypress(snake2Up,"Up")
    wn.onkeypress(snake2Left,"Left")
    wn.onkeypress(snake2Right,"Right")
    wn.onkeypress(snake2Down,"Down")

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

def hideBodyParts():
    global dis
    
    global bodyParts
    
    head.goto(0,0)
    head.direction = "stop"
    for eachPart in bodyParts:
        eachPart.goto(1000,1000)

    dis = 1
        
    bodyParts = []

# snake #2 hide body parts
def hideBodyParts2():
    global bodyParts2
    snake2.goto(50,50)
    snake2.direction = "stop"

    for eachPart in bodyParts2:
        eachPart.goto(1000,1000)
    bodyParts2 = []

# here is where the time thing will go
def updateTimer():
    
    global timer
    global game  
    global mode  

    # while game == True:
    timer += 1
    if 25//timer == 0 and mode == "Hard":
        x = r.randint(-290,290)
        y = r.randint(-290,290)
        food.goto(x,y)
        timer = 1

# events

wn.onkeypress(ups,"w")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.onkeypress(downs,"s")
wn.onkeypress(hardMode,"h")
wn.onkeypress(regMode,"r")
wn.onkeypress(PVPMode,"p")
wn.onkeypress(snake2Up,"Up")
wn.onkeypress(snake2Left,"Left")
wn.onkeypress(snake2Right,"Right")
wn.onkeypress(snake2Down,"Down")




# mainloop
print(console)

if mode == "Home":
    print("Home")
elif mode == "Hard":
    print("Hard")
elif mode == "Reg":
    print("Reg")
elif mode == "PVP":
    print("PVP")



while True:

    
    wn.update()     # updates/refreshes the screen
    
        # border collision
    if mode == "Reg" or mode == "Hard":
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
    elif mode == "PVP":
        # if either player hits the other

        for i in range(len(bodyParts2)):
            if int(head.distance(bodyParts2[i]) < 20):
                hideBodyParts()

        if head.distance(snake2) < 20:
            hideBodyParts()

        for i in range(len(bodyParts)):
            if int(snake2.distance(bodyParts[i]) < 20):
                hideBodyParts2()

        if snake2.distance(head) < 20:
            hideBodyParts2()
    
        # wall collision

        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()>290 or head.ycor()<-290:
            hideBodyParts()

        if snake2.xcor()>290 or snake2.xcor()<-290 or snake2.ycor()>290 or snake2.ycor()>290 or snake2.ycor()<-290:
            hideBodyParts2()

        # food collision

        if head.distance(food) < 20:
            # script.clear()
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
            x = head.xcor()
            y = head.ycor()
            bodyParts[0].goto(x,y)
        if len(bodyParts2)>0:
            x = snake2.xcor()
            y = snake2.ycor()
            bodyParts2[0].goto(x,y)
        move()
        snake2Move()

        for part in bodyParts:
            if part.distance(head)<10:
                hideBodyParts()

        for part in bodyParts2:
            if part.distance(snake2)<10:
                hideBodyParts2()
           

        ~time.sleep(delay)

    wn.ontimer(updateTimer,interval)

# end of all movement

wn.listen()

wn.mainloop()