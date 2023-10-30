#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

robot = trtl.Turtle()

#------ robot commands
def moveUp():
  robot.dot(10)
  robot.fd(50)
    
def moveDown():
  robot.dot(10)
  robot.fd(50)

def moveLeft():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

def moveRight():
  robot.speed(0)
  robot.rt(90)
  robot.speed(2)
  
# actions = {"w": moveUp(),
#            "a": moveLeft(),
#            "s": moveRight(),
#            "d": moveDown()
# }

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze1.png") # other file names should be maze2.png, maze3.png


#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample for loop:
'''
for step in range(3): # forward 3
  move()
'''

color = "purple"

# moveUp(4,color)
# moveLeft()
# moveUp(4,color)

# # --- end of maze #1 --- #

# robot.goto(startx,starty)
# moveLeft()

# # --- Maze #2 --- #

# wn.bgpic("maze2.png")

# # --- maze #2 movement --- #

# color = "blue"

# moveUp(3,color)
# moveLeft()
# moveUp(2,color)

# # --- end robot movement --- #

# # --- end of maze #2 --- #

# robot.goto(startx,starty)

# # --- maze #3 --- #

# wn.bgpic("maze3.png")

# --- maze #3 movement --- #

# color = "red"

# for i in range(4):
#   moveUp(1,color)
#   moveLeft(1)
#   moveUp(1,color)
#   moveLeft(3)

# --- end of maze #3 --- #

game = True

while game == True:
  ui = input("w,a,s,d")
  if ui == "w":
    moveUp()
  elif ui == "a":
    moveLeft()
  elif ui == "d":
    moveRight()
  elif ui == "s":
    moveDown()
  
  x =robot.xcor()
  y = robot.ycor()
  print(x)
  print(y)
  if (x == 100) and (y == 100):
    game = False
    

# --- end of all movement --- #

wn.mainloop()