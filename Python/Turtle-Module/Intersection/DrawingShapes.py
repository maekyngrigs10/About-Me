# turtle stuff
# import Turtle module as aliasName t

import turtle as t

# if did not use alias --> would have to write Turtle.Turtle()
#                                                         Class.Constructor()

mikey = t.Turtle()

wn = t.Screen()         # screen for the turtle

mikey.shape("turtle")   # changes shape to a turtle

mikey.color("#ffc179")

# mikey is speedy quick

mikey.speed(6)



# mikey draws his first square on repeat --- awwwwwww

# while True:
    
#     for i in range(4):
    
#         mikey.forward(100)

#         mikey.right(90)

# mikey draws his first star on repeat --- awwwwwww

while True:
    mikey.right(252)
    mikey.forward(100)
    mikey.right(36)
    mikey.forward(100)
        
# 8 point star
# while True:
#     for i in range(5):
#         mikey.forward(100)
        
#         mikey.right(225)
        
#         mikey.forward(100)
        
#         mikey.right(45)
        
#         mikey.right(300)        

# creates a ninja star
# while True:
#     for i in range(4):
#         mikey.forward(100)
        
#         mikey.right(225)
        
#         mikey.forward(100)
        
#         mikey.right(45)
        
#         mikey.forward(100)
        
#         mikey.right(315)
       
# makes a donut 
# while True:
#     for i in range(4):
#         mikey.forward(100)
        
#         mikey.right(100)
        
#         mikey.forward(50)
        
#         mikey.right(90)
        
    

# ^^^ stuff that must always (kind of) go at very very top





# stuff that must always (kind of) go at very very bottom

wn.mainloop()

