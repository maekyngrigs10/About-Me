# import turtle

import turtle as t

import random as r

import leaderboard as lb

# game configuration (global variables)

wn = t.Screen()

fontSetup = ("Times New Roman",30,"normal")

FILENAME = "Database.txt"

# intialize turtles

doug = t.Turtle()

doug.shape("turtle")

doug.shapesize(2)

doug.fillcolor("blue")

doug.speed(0)

doug.penup()

# scorekeeper

scorekeeper = t.Turtle()

scorekeeper.hideturtle()

scorekeeper.penup()

scorekeeper.goto(100,200)

scorekeeper.pendown()

score = 0

# time keeper

timekeeper = t.Turtle()

timekeeper.hideturtle()

timekeeper.penup()

timekeeper.goto(-100,200)

timekeeper.pendown()

timer = 10


# game functions

def dougClicked(x,y):
    
    # print("doug was clicked")
    
    updateScore(x,y)
    
    # print(x,y)
    
    moveDoug()
    
def moveDoug():
    
    newX = r.randint(-300,300)
    
    newY = r.randint(-300,300)
    
    doug.goto(newX,newY)

def updateTimer():
    
    global timer
    
    timekeeper.clear()
    
    if timer <= 0:
        
        timekeeper.write("Time's up!",font=fontSetup)
        
        doug.hideturtle()
        
        manageLeaderboard()
    
    else:
        
        timer -= 1
        
        timekeeper.write(f"Timer: {timer}",font=fontSetup)
        
        timekeeper.getscreen().ontimer(updateTimer,interval)

def updateScore(x,y):
    
    scorekeeper.clear()
    
    global score
    
    score += 1
    
    # object.write("message",options) --------- ("font type",size,"style")
    scorekeeper.write(f"Score: {score}",font=fontSetup)
    
def manageLeaderboard():
    
    # get the data from the txt file
    
    namesList = lb.getNames(FILENAME)  
    
    scoresList = lb.getScores(FILENAME)  
    
    # check to see if you made the leader board
    
    playerName = ""
    
    if (len(scoresList)<5 or score>=int(scoresList[-1])):
    
        playerName = t.textinput("What's your name?", "username: ")
        
        lb.updateLeaderboard(FILENAME,namesList,scoresList,playerName,score)
    
    else:
        
        print("did not make leaderboard")
        
        lb.draw_leaderboard(False,namesList,scoresList,scorekeeper,10)
    
    # update the leader board
    
    
    # display the leader board
    
    lb.draw_leaderboard(False,namesList,scoresList,scorekeeper,10)

# events

doug.onclick(dougClicked)

# main loop (the running code)

interval = 1000

wn.ontimer(updateTimer,interval)

wn.mainloop()

'''
    1.) click the turtle
    2.) move the turtle
    3.) update score
    4.) countdown

'''


