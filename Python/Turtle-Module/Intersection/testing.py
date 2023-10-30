import turtle as t
Turtle=t.Turtle
wn = t.Screen()
def drawing():
    t.speed(0)
    t.penup()
    t.goto(-200,50)
    t.pendown()
    t.begin_fill()
    t.fillcolor("grey")
    for i in range(4):
        t.forward(200)
        t.left(90)
        t.forward(200)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()
    #yellow line horizontal
    t.penup()
    t.goto(-200,-42)
    t.pendown()
    t.pensize(5)
    t.color("yellow")
    t.forward(200)
    t.penup()
    t.forward(200)
    t.pendown()
    t.forward(200)
    t.penup()
    t.goto(-200,-50)
    t.pendown()
    t.pensize(5)
    t.color("yellow")
    t.forward(200)
    t.penup()
    t.forward(200)
    t.pendown()
    t.forward(200)
    #white lines horizontal
    t.penup()
    t.goto(-250,0)
    t.color("white")
    for i in range(8):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
    t.penup()
    t.forward(200)
    for i in range(8):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
    t.penup()
    t.goto(-250,-100)
    for i in range(8):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
    t.penup()
    t.forward(200)
    for i in range(8):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
    #yellow lines vertical
    t.right(90)
    t.penup()
    t.color("yellow")
    t.goto(100,250)
    t.pendown()
    t.pensize(5)
    t.color("yellow")
    t.forward(200)
    t.penup()
    t.forward(200)
    t.pendown()
    t.forward(200)
    t.penup()
    t.goto(108,250)
    t.pendown()
    t.pensize(5)
    t.color("yellow")
    t.forward(200)
    t.penup()
    t.forward(200)
    t.pendown()
    t.forward(200)
    #white dashed lines vertical
    t.penup()
    t.goto(50,300)
    t.color("white")
    for i in range(8):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
    t.penup()
    t.forward(200)
    for i in range(8):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
    t.penup()
    t.goto(150,300)
    for i in range(8):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
    t.penup()
    t.forward(200)
    for i in range(8):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
drawing()
#Turtles
horizontalTurts = []
verticalTurts = []
# use interesting shapes and colors
turtleShapes = ["arrow", "turtle", "circle", "square"]
horizColors = ["red", "blue", "green", "orange"]
vertColors = ["darkred", "darkblue", "lime", "salmon"]
spacing=100
for shape in turtleShapes:
    ht = Turtle(shape=shape)
    horizontalTurts.append(ht)
    ht.penup()
    ht.fillcolor(horizColors.pop())
    ht.setheading(0)
    vt = Turtle(shape=shape)
    verticalTurts.append(vt)
    vt.penup()
    vt.fillcolor(vertColors.pop())
    vt.setheading(270)
    spacing+=25
horizontalTurts[0].goto(-200,25)
horizontalTurts[1].goto(-200,-25)
horizontalTurts[2].setheading(180)
horizontalTurts[2].goto(350,-75)
horizontalTurts[3].goto(350,-125)
horizontalTurts[3].setheading(180)
verticalTurts[0].goto(25,250)
verticalTurts[1].goto(75,250)
verticalTurts[2].goto(125,-300)
verticalTurts[2].setheading(90)
verticalTurts[3].goto(175,-300)
verticalTurts[3].setheading(90)
#moving the turtles
distanceToMove=2
collisionDistance=20
for step in range(200):
    for h in horizontalTurts:
        for v in verticalTurts:
            if horizontalTurts[0].xcor()>400 and horizontalTurts[0].xcor()<450:
                horizontalTurts[0].goto(-200,25)
            if horizontalTurts[1].xcor()>400 and horizontalTurts[1].xcor()<450:
                horizontalTurts[1].goto(-200,-25)
            if horizontalTurts[2].xcor()<-200 and horizontalTurts[2].xcor()>-250:
                horizontalTurts[2].goto(350,-75)
            if horizontalTurts[3].xcor()<-200 and horizontalTurts[3].xcor()>-250:
                horizontalTurts[3].goto(350,-125)
            if verticalTurts[0].ycor()<-200 and verticalTurts[0].ycor()>-250:
                verticalTurts[0].goto(25,250)
            if verticalTurts[1].ycor()<-200 and verticalTurts[1].ycor()>-250:
                verticalTurts[1].goto(75,250)
            if verticalTurts[2].ycor()>250 and verticalTurts[2].ycor()<300:
                verticalTurts[2].goto(125,-300)
            if verticalTurts[3].ycor()>250 and verticalTurts[3].ycor()<300:
                verticalTurts[3].goto(175,-300)
            #this is the code for whenever they reach the end, they will teleport back to the beginning.
            h.fd(distanceToMove)
            v.fd(distanceToMove)
            #check for collision
            if (abs(h.xcor() - v.xcor()) < collisionDistance):
                if (abs(h.ycor()-v.ycor()) < collisionDistance):
                    h.fillcolor("gray")
                    v.fillcolor("gray")
                    h.goto(-1000,1000)     
                    v.goto(-1000,1000) 
wn.mainloop()







