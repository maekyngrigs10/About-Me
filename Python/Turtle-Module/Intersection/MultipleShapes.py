import turtle as t

mikey = t.Turtle()

wn = t.Screen()

#------^ Important Begin Stuff ^------#

# (0,0) is middle of screen

#------ Drawing Square Function ------#

def drawSquare(d):
    
    for i in range(4):
        
        mikey.forward(d)

        mikey.right(90)
        
# makes pen stop drawing --> moves the turtle --> then starts drawing again
        
# mikey.penup()
# mikey.goto(100,100)
# mikey.pendown()


# shape = input("what shape: (s)quare, (st)ar , (n)inja star , (d)onut , or (t)riangle    ")

color = input("what color: red , orange , yellow , green , blue , purple, or black    ")
size = int(input("what size (just need a length) :  "))

mikey.pencolor(color)

drawSquare(size)


#------^ Important End Stuff ^------#

wn.mainloop()