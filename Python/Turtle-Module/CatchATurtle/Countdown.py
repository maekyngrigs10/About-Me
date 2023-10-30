# import

import turtle as t

# configuration (global variables)

wn = t.Screen()

# font setup

fontSetup = ("Times New Roman",30,"normal")

# intialize turtles

timekeeper = t.Turtle()

timekeeper.penup()

timekeeper.goto(-100,200)

timekeeper.pendown()

timer = 10

# functions

def updateTimer():
    
    global timer
    
    timekeeper.clear()
    
    if timer <= 0:
        timekeeper.write("Time's up!",font=fontSetup)
    
    else:
        timer -= 1
        
        timekeeper.write(f"Timer: {timer}",font=fontSetup)
        
        timekeeper.getscreen().ontimer(updateTimer,interval)
    
    # it needs to recursively run this function

# end of all movement

interval = 1000

wn.ontimer(updateTimer,interval)

wn.mainloop()