# import

import turtle as t

# configuration (global variables)

wn = t.Screen()

# font setup

fontSetup = ("Times New Roman",30,"normal")

# intialize turtles

scorekeeper = t.Turtle()

scorekeeper.fillcolor("red")

scorekeeper.shape("circle")

scorekeeper.hideturtle()

scorekeeper.penup()

scorekeeper.goto(100,200)

scorekeeper.pendown()

score = 0


# functions

def updateScore(x,y):
    
    scorekeeper.clear()
    
    global score
    
    score += 1
    
    # object.write("message",options) --------- ("font type",size,"style")
    scorekeeper.write(f"Score: {score}",font=fontSetup)
    


# end of all movement

wn.onscreenclick(updateScore)

wn.mainloop()