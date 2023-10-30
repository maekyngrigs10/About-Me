import turtle as t

car = t.Turtle()

wn = t.Screen()

wn.bgcolor("black")

def whiteLines(x,y):
    car.penup()
    car.goto(x,y)
    car.pencolor("white")
    for i in range(9):
        car.pendown()
        car.fd(10)
        car.penup()
        car.fd(10)
    
def yellowLines(x,y):
    car.pencolor("yellow")
    car.penup()
    car.goto(x,y)
    car.pendown()
    car.fd(175)
    
wn.setup(width=750, height=650)

car.penup()

car.goto(-325,125)

car.color("lightgrey")


# out line of intersection
for i in range(4):
    car.pendown()
    car.fd(175)
    car.lt(90)
    car.fd(175)
    car.rt(90)
    car.fd(175)
    car.rt(90)
    
# end of outline

# white dashed lines
whiteLines(-325,80)

whiteLines(-325,-10)
    
car.penup()

# yellow lines

yellowLines(-325,40)

yellowLines(25,40)

whiteLines(25,80)

whiteLines(25,-10)

car.lt(90)


yellowLines(-60,125)

whiteLines(-10,125)

whiteLines(-100,125)

car.rt(180)

yellowLines(-60,-50)

whiteLines(-10,-50)

whiteLines(-100,-50)


# end of stuff

wn.mainloop()