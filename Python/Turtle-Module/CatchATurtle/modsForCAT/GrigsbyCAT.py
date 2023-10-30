# import turtle

import turtle as t

import random as r

import leaderboard as lb

import winsound as w

# game configuration (global variables)


wn = t.Screen()

wn.setup(width=700,height=700)

fontSetup = ("Times New Roman",30,"normal")

FILENAME = "Database.txt"

# intialize turtles

doug = t.Turtle()

doug.shape("turtle")

doug.shapesize(4,4,2)

doug.fillcolor("blue")

doug.speed(0)

doug.penup()

doug.hideturtle()

# scorekeeper

scorekeeper = t.Turtle()

scorekeeper.hideturtle()

scorekeeper.penup()

scorekeeper.goto(200,250)

scorekeeper.pendown()

score = 0

# time keeper

timekeeper = t.Turtle()

timekeeper.hideturtle()

timekeeper.penup()

timekeeper.goto(-100,250)

timekeeper.pendown()

timer = 10

# click counter

counter = t.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-300,250)
counter.pendown()


clicks = 0

game = False

interval = 1000

# game functions

def startGame(x,y):
    
    global interval
    
    global game
    
    game = True
    scorekeeper.hideturtle()
    scorekeeper.shape("turtle")
    scorekeeper.hideturtle()
    scorekeeper.goto(100,250)
    
    doug.showturtle()

    wn.ontimer(updateTimer,interval)

def dougClicked(x,y):
    
    # global score
    
    # score += 1

    w.Beep(10000,250)

    wn.bgcolor("red")

    doug.color("red")
    
    doug.fillcolor("white")
    
    doug.stamp()
    
    wn.bgcolor("white")
    
    doug.fillcolor("blue")
    doug.color("blue")
    
    
    
    # print("doug was clicked")
    
    updateScore(x,y)
    
    # print(x,y)
    
    moveDoug()
    
def moveDoug():
    
    global score
    
    # print(clicks)
    
    newX = r.randint(-225,225)
    
    newY = r.randint(-225,225)
    
    doug.goto(newX,newY)
    
    if score%2 == 0:
        i = doug.shapesize()
        j = i[0]
        doug.shapesize(j/2,j/2)
    else:
        i = doug.shapesize()
        j = i[0]
        doug.shapesize(j/2,j/2)
    
    if score%3 == 0:
        doug.shapesize(4,4,2)
    
def updateTimer():
    
    global timer
    
    global interval
    
    global score
    
    global clicks
    
    timekeeper.clear()
    
    if timer <= 0:
        
        timekeeper.write("Time's up!",font=fontSetup)
        
        accuracy = round(score/clicks,2)*100
        
        counter.clear()
        
        counter.penup()
        
        counter.goto(-150,-275)

        counter.pendown()
        
        counter.write(f"accuracy: {accuracy}%",font=fontSetup)
        
        doug.hideturtle()
        
        manageLeaderboard()
    
    else:
        
        timer -= 1
        
        timekeeper.write(f"Timer: {timer}",font=fontSetup)
        
        timekeeper.getscreen().ontimer(updateTimer,interval)

def clickerCounter(x,y):
    
    global clicks
    
    global timer
    
    clicks += 1
    
    counter.clear()
    
    if timer <= 0:
        # counter.clear()
        pass
    else:
        counter.write(f"Clicks: {clicks}",font=fontSetup)
    
    

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

doug.hideturtle()

while game == False:
    scorekeeper.penup()
    scorekeeper.goto(0,0)
    scorekeeper.shape("square")
    scorekeeper.shapesize(2,5,1)
    scorekeeper.showturtle()
    scorekeeper.onclick(startGame)

scorekeeper.hideturtle()

doug.onclick(dougClicked)

wn.onclick(clickerCounter)

# main loop (the running code)


wn.mainloop()

'''
    1.) click the turtle
    2.) move the turtle
    3.) update score
    4.) countdown

'''


