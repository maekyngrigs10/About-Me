# all imports

import turtle as t

from turtle import *

import random as r

from random import randint

# end of imports

# configuration and global variables

wn = t.Screen()

# end of config and variables

# intialize turtles/objects

mazeDrawer = t.Turtle()

mazeDrawer.pensize(5)

mazeDrawer.color("blue")

mazeDrawer.speed(0)

mazeDrawer.penup()

mazeDrawer.goto(125,-100)

mazeDrawer.pendown()

mazeRunner = t.Turtle()
mazeRunner.color("red")
mazeRunner.penup()
mazeRunner.goto(50,-50)
mazeRunner.pendown()


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
  
    
    for i in range(25):
        
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
    
    mazeRunner.fd(5)
    
    canvas = wn.getcanvas()
    
    x,y = mazeRunner.pos()
    
    margin = 5
    
    items = canvas.find_overlapping(x+margin,-y+margin,x-margin,-y-margin)
    
    # if the item has overlap
    
    if( len(items)>0):      # stack of what is overlapping
        canvasColor = canvas.itemcget(items[0],"fill")
        
        if canvasColor == "blue":       # check for collision
            
            print("you hit")
            
            mazeRunner.color("grey")
            wn.onkeypress(None,"space") # disabling the movement
            return
        
        # wn.ontimer(move,10)

# end of functions

# events

wn.onkeypress(goUp,"w")
wn.onkeypress(goLeft,"a")
wn.onkeypress(goDown,"s")
wn.onkeypress(goRight,"d")
wn.onkeypress(move,"space")


# end of events

# main/game loop or running code

mazeMaker()

# end of main loop

wn.listen()

wn.mainloop()



