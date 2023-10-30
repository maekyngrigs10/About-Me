# all imports

import turtle as t

from turtle import *

import random as r

from random import randint

# end of imports

# configuration and global variables

fontSetup = ("Georgia",30,"normal")

timer = 0
interval = 1000
game = True
secs = 0
mins = 0

# end of config and variables

# intialize turtles/objects

# window/screen setup

wn = t.Screen()
wn.setup(width=1000,height=1000)

# maze drawer

mazeDrawer = t.Turtle()
mazeDrawer.pensize(5)
mazeDrawer.color("black")
mazeDrawer.speed(0)
mazeDrawer.penup()
mazeDrawer.goto(125,-100)
mazeDrawer.pendown()

# maze Runner

mazeRunner = t.Turtle()
mazeRunner.color("blue")
mazeRunner.penup()
mazeRunner.goto(50,-50)
mazeRunner.pendown()

# time keeper

timekeeper = t.Turtle()
timekeeper.hideturtle()
timekeeper.penup()
timekeeper.goto(-400,300)
timekeeper.pendown()

# enemy turtle

enemy = t.Turtle()
enemy.penup()
enemy.shape("turtle")
enemy.speed(6)
enemy.goto(100,-100)
enemy.hideturtle()
enemy.color("red")


# end of turtle/object intialization

p = 25

# functions

def drawDoor(pos):
    
    mazeDrawer.fd(pos)
    
    mazeDrawer.penup()
    
    mazeDrawer.fd(p*2)
    
    mazeDrawer.pendown()
    
def drawBarrier(pos):
    
    mazeDrawer.fd(pos)
    
    mazeDrawer.lt(90)
    
    mazeDrawer.fd(p*2)
    
    mazeDrawer.bk(p*2)
    
    mazeDrawer.rt(90)

# normal spiral with paths and boundaries

def mazeMaker():
    
    w = 20
    
    p = 25
  
    
    for i in range(18):
        
        w += p
        
        if i > 4:
            
            mazeDrawer.lt(90)
            
            # where do we draw the doors and barriers inside of a wall length
            
            doorSpot = r.randint(p*2,(w-2*p))
            barrierSpot = r.randint(p*2,(w-2*p))
            
            # # check to make sure a foor and barrier do not render on top of each other
            
            while abs(doorSpot-barrierSpot) < p:
                
                doorSpot = r.randint(p*2,(w-2*p))
                
            if (doorSpot < barrierSpot):
                
                drawDoor(doorSpot)
                
                drawBarrier(barrierSpot-doorSpot-p*2)
                
                mazeDrawer.fd(w-barrierSpot)
            
            else:
                
                drawBarrier(barrierSpot)
                
                drawDoor(doorSpot-barrierSpot)
                
                mazeDrawer.fd(w-doorSpot-p*2)
        
        # to make only one exit

    x = r.randint(1,2)
    
    for j in range(4):

        mazeDrawer.fd(10)
        mazeDrawer.lt(90)

        if x != j:
            
            for k in range(50):
                mazeDrawer.fd(10)
            # mazeDrawer.lt(90)
        else:
            y = r.randint(15,35)
            # mazeDrawer.fd(10)
            # mazeDrawer.lt(90)
            for l in range(46):
                if l != y:
                    mazeDrawer.fd(10)
                else:
                    mazeDrawer.rt(90)
                    mazeDrawer.fd(50)
                    mazeDrawer.penup()
                    mazeDrawer.lt(90)
                    mazeDrawer.fd(50)
                    mazeDrawer.pendown()
                    mazeDrawer.lt(90)
                    mazeDrawer.fd(50)
                    mazeDrawer.rt(90)
                    
                    # mazeDrawer.penup()
                    # mazeDrawer.fd(50)
                    # mazeDrawer.pendown()
    # mazeDrawer.fd(5)
    mazeDrawer.lt(90)
    # mazeDrawer.fd(35)

def moveEnemy():

    if enemy.xcor()> 250 or enemy.ycor()> 250 or enemy.xcor()< -250 or enemy.ycor()< -250:
        enemy.goto(100,-100)
        enemy.setheading(-enemy.heading())
        enemy.fd(100)
    else:
        enemy.setheading(mazeRunner.heading())
        enemy.fd(35)

def updateTimer():
    
    global timer
    
    global secs
    global mins


    if game != False:
        timekeeper.clear()

        timer += 1

        if int(secs) >= 2:
            enemy.showturtle()
            wn.ontimer(moveEnemy,10)
        if timer < 60:
            secs = timer
            if int(secs) < 10:
                secs = f"0{str(secs)}"
            else:
                secs = timer
        elif timer%60 == 0:
            secs = 0
            mins = int(mins)+1
            if int(mins) < 10:
                mins = f"0{str(mins)}"
        elif timer > 60:
            secs = timer%60
            if int(secs) < 10:
                secs = f"0{str(secs)}"
    elif game == False:
        timer += 0
    # timekeeper.write(f"Timer: {timer}",font=fontSetup)
    timekeeper.pendown()
    timekeeper.write(f"Timer: {mins}:{secs}",font=fontSetup)
    timekeeper.penup()
    
    timekeeper.getscreen().ontimer(updateTimer,interval)
    

def checkExit():

    global game

    if mazeRunner.xcor()>= 280 or mazeRunner.ycor()>= 280 or mazeRunner.xcor()<= -280 or mazeRunner.ycor()<= -290:
        print("Congrats")
        mazeRunner.shapesize(7,7,2)
        enemy.clear()
        enemy.penup()
        enemy.hideturtle()

        game = False
        wn.onkeypress(None,"space")
        
        
        
        
    mazeDrawer.hideturtle()



def goUp():
    mazeRunner.setheading(90)
    
def goLeft():
    mazeRunner.setheading(180)
    
def goDown():
    mazeRunner.setheading(270)
    
def goRight():
    mazeRunner.setheading(0)
    
def move():
    global timer
    global mins
    global secs
    
    mazeRunner.fd(5)
    
    canvas = wn.getcanvas()
    
    x,y = mazeRunner.pos()
    
    margin = 5
    
    items = canvas.find_overlapping(x+margin,-y+margin,x-margin,-y-margin)
    checkExit()

    # if the mazerunner collides with the enemy turtle

    if (abs(mazeRunner.xcor()-enemy.xcor())<2) or (abs(mazeRunner.ycor()-enemy.ycor())<2):

        print("the enemy got you, start again")

        mazeRunner.color("grey")
        wn.onkeypress(None,"space") # disabling the movement
        
        mazeRunner.clear()
        mazeRunner.penup()
        mazeRunner.goto(50,-50)
        mazeRunner.pendown()
        mazeRunner.color("blue")
        
        # if u want the timer to restart after the enemy gets them uncomment this
        
        # mins = int(mins)
        # secs = int(secs)
        
        # timer,mins,secs = 0
        
        wn.onkeypress(move,"space") # disabling the movement
        return
    
    # if the item has overlap
    
    if( len(items)>0):      # stack of what is overlapping
        canvasColor = canvas.itemcget(items[0],"fill")
        
        if canvasColor == "black":       # check for collision
            
            print("you hit")
            
            mazeRunner.color("grey")
            wn.onkeypress(None,"space") # disabling the movement

    
            
            mazeRunner.clear()
            mazeRunner.penup()
            mazeRunner.goto(50,-50)
            mazeRunner.pendown()
            mazeRunner.color("blue")
            
            # if u want the timer to restart after the turtle hits the side then uncomment this
        
            # mins = int(mins)
            # secs = int(secs)
            
            # timer,mins,secs = 0
            
            wn.onkeypress(move,"space") # disabling the movement
            return

        # wn.ontimer(move,10)

def pauseButton():

    global game
    global timer

    game = False
    
    wn.onkeypress(None,"space")


def unpause():

    global game
    global interval

    game = True
    wn.onkeypress(move,"space")
    # wn.ontimer(updateTimer,interval)
    


# end of functions

# events

wn.onkeypress(goUp,"w")
wn.onkeypress(goLeft,"a")
wn.onkeypress(goDown,"s")
wn.onkeypress(goRight,"d")
wn.onkeypress(move,"space")
wn.onkeypress(pauseButton,"p") # pauses the game
wn.onkeypress(unpause,"u") # unpauses the game

# wn.ontimer(moveEnemy,10)


# end of events

# main/game loop or running code

mazeMaker()

# while game == True:
#     updateTimer()

wn.ontimer(updateTimer,interval) 

# end of main loop

wn.listen()

wn.mainloop()



