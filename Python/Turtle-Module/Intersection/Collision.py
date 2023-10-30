from turtle import *

# create two empty lists of turtles, adding to them later
horizontalturtles = []
verticalturtles = []

# use interesting shapes and colors
turtleShapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horizColors = ["red", "blue", "green", "orange", "purple", "gold"]
vertColors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

wn = Screen()

spacing = 50

for shape in turtleShapes:
    ht = Turtle(shape=shape)
    horizontalturtles.append(ht)
    ht.penup()
    ht.fillcolor(horizColors.pop())
    ht.goto(-250,spacing)
    ht.setheading(0)
    
    vt = Turtle(shape=shape)
    verticalturtles.append(vt)
    vt.penup()
    vt.fillcolor(vertColors.pop())
    vt.goto(-spacing,180)
    vt.setheading(-90)
    
    spacing += 25
    
# moving the turtles

distanceToMove = 2

for step in range(100):
    for h in horizontalturtles:
        for v in verticalturtles:
            h.fd(distanceToMove)
            v.fd(distanceToMove)
            if (abs(h.xcor() - v.xcor()) < 20):
                if (abs(h.ycor()-v.ycor()) < 20):
                    h.fillcolor("grey")
                    v.fillcolor("grey")
                    horizontalturtles.remove(h)
                    verticalturtles.remove(v)

# end of everything

wn.mainloop()