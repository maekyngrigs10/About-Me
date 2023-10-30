import turtle as t

car = t.Turtle()

wn = t.Screen()

wn.bgcolor("black")

def whiteLines(x,y):
    car.penup()
    car.goto(x,y)
    car.pendown()
    car.pencolor("white")
    for i in range(13):
        car.pendown()
        car.fd(10)
        car.penup()
        car.fd(10)
    
def yellowLines(x,y):
    car.pencolor("yellow")
    car.penup()
    car.goto(x,y)
    car.pendown()
    car.fd(250)
    
wn.setup(width=750, height=750)

car.penup()

car.goto(-375,125)

car.color("lightgrey")


# out line of intersection
for i in range(4):
    car.pendown()
    car.fd(250)
    car.lt(90)
    car.fd(250)
    car.rt(90)
    car.fd(250)
    car.rt(90)
    
# end of outline

# white dashed lines
whiteLines(-375,60)

whiteLines(-375,-60)
    
car.penup()

# yellow lines

yellowLines(-375,0)

yellowLines(125,0)

whiteLines(125,60)

whiteLines(125,-60)

car.lt(90)

yellowLines(0,125)

whiteLines(60,125)

whiteLines(-60,125)

car.rt(180)

yellowLines(0,-125)

whiteLines(-60,-125)

whiteLines(60,-125)


# end of stuff

wn.mainloop()