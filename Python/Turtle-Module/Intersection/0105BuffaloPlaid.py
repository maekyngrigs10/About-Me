import turtle as t
from turtle import *

# start of turtle setup

doug = t.Turtle()

wn = t.Screen()

wn.setup(500,500)

doug.shape("square")

doug.pensize(25)

doug.penup()

# end of turtle setup

# plaid maker function
    
def plaidMaker(y,c1,c2):
    
    doug.goto(-235,y)
    
    for i in range(12):
        doug.color(c1)
        doug.stamp()
        doug.penup()
        doug.fd(20)
        doug.color(c2)
        doug.stamp()
        doug.fd(20)
        
# end of plaid maker function

# extra variable definings
        
c1 = "black"

c2 = "blue"

y = 235

# end of extra variable definings

# main for loop

for i in range(12):
    
    plaidMaker(y,c1,c2)
    y -= 20
    plaidMaker(y,c2,c1)
    y -= 20
    
# end of main loop
    

# end of all movement

wn.mainloop()
