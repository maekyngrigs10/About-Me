import random

name = input("what is your name?\t")
compName = input("what is your computer's name?\t")
print("\n")

board=[[" "," "," "],[" "," "," "],[" "," "," "]]

b='''
          |    |
     -----------------
          |    |
     -----------------
          |    |
     '''
"""
     sampleBoard=[[1,2,3],[4,5,6],[7,8,9]]
     print(sampleBoard)
     for row in range(len(sampleBoard)):    #range(len(sampleBoard))->[0,1,2]
          for columns in range(len(sampleBoard[row])):
               print(sampleBoard[row][columns])
"""
def printBoard(board):
     for r in range(3):
          print(board[r][0]+"|"+board[r][1]+"|"+board[r][2])
          if r<2:
               print("-"*5)

#returns a true or false value on whether we can choose that spot
def chooseSpot(r,c,symbol,board):
     #if the spot is open
     if board[r][c] == " ":
          #add the symbol and return true
          board[r][c]=symbol
          return True    
     return False

#---------------------- CHECKING THE BOARD ----------------------#
def catGame(board):
     #check every spot to see if there is something
     for row in range(len(board)):    #range(len(sampleBoard))->[0,1,2]
          for columns in range(len(board[row])):
               if (board[row][columns]) == " ":
                    return False
     print("CAT GAME!")
     return True         #return stop the function and give a value back

def checkForWinners(board):
#check horizontally
     for r in range(len(board)):
     #r is the rows and the columns are the same for each row
          if (board[r][0] == board[r][1] and board[r][1] == board[r][2]) and board[r][0]!=" ":
               print("Winner winner Turkey dinner!")
               return True
     #check vertically
     for c in range(len(board)):
          #r is the rows and the columns are the same for each row
          if (board[0][c] == board[1][c] and board[1][c] == board[2][c]) and board[0][c]!=" ":
               print("Winner winner salmon dinner!")
               return True
#check diagonally
     #left to right
     if ((board[0][0] == board[1][1] == board[2][2]) and (board[0][0]) == "X" or (board[0][0] == board[1][1] == board[2][2]) and (board[0][0]) == "O"):
          print("winner winner beef dinner")
          return True  
     #right to left 
     if ((board[0][2] == board[1][1] == board[2][0]) and (board[0][2]) == "X" or (board[0][2] == board[1][1] == board[2][0]) and (board[0][2]) == "O"):
         print("winner winner mutton dinner")
         return True

#---------------------- END OF CHECKING THE BOARD ----------------------#


          
#hard code 
"""
the following code was commented out to test my theory 
of the taken spots list, so if that doesn't end up 
working out just uncomment all this stuff -- thanks, maekyn
"""
# symbol="X"
# while symbol!="Q":
#      printBoard(board)

#      #if the symbol is x
#      # then run the code already built
#      #else
#      # run the computer's code

#      #loop until a good spot is chosen
#      goodSpot=False
#      while not goodSpot:
#           r = int(input("row: "))-1
#           c = int(input("col: "))-1
#           #if we can NOT choose the spot
#           if((0<=r<=2) and (0<=c<=2)):
#                if (not chooseSpot(r,c,symbol,board)):
#                     print("Spot Taken")
#                else:
#                     goodSpot = True
     
#      #check for a winner or CAT
#      if catGame(board) or checkForWinners(board):
#           symbol="Q"
#      #switching our symbols
#      if symbol=="X":
#           symbol="O"
#      elif symbol=="O":
#           symbol="X"
"""
this is the end of the code that
I commented out, just in case you
get confused where the end was :)
"""

#computer vs player
#computer --> r = randomint(1,3) c = randomint(1,3) while r,c in board == "" the spot can be filled

#strategy
#if row or column -1 or +1 == "" computer guesses one of those spots 

#there are 9 combos (r,c) --> (1,1)(1,2)(1,3) / (2,1)(2,2)(2,3) / (3,1)(3,2)(3,3)
#r = [1,2,3]
#c = [1,2,3]
#combos = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]
# combos technically turn into --> combos = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
#when player puts in r,c --> turn it into (r,c) and take it out of the combos list
#i.e. ) 
# row: 2
# col: 1
# combo -= (r,c)

printBoard(board)
symbol = "X"
while symbol != "Q":
     if catGame(board) or checkForWinners(board) != True:
          while symbol == "X":
               print(f"\nit's {name}'s turn\n")
               symbol = "X"
               goodSpot = False
               while not goodSpot:
                    r = int(input("row: "))-1
                    c = int(input("col: "))-1
                    if ((0<=r<=2) and (0<=c<=2)):
                         if (not chooseSpot (r,c,symbol,board)):
                              print("spot taken")
                         else:
                              goodSpot = True
               printBoard(board)
               if catGame(board) or checkForWinners(board) == True:
                    symbol = "Q"
               else:
                    symbol = "O"
          while symbol == "O":
               print(f"\nit's {compName}'s turn\n")
               goodSpot = False
               firstTurn = True
               while not goodSpot:
                    while firstTurn == True:
                         r = random.randint(0,2)
                         c = random.randint(0,2)
                         firstTurn = False
                    # r = random.randint(0,2)         #testing the +1 -1 column and row theory
                    # c = random.randint(0,2)

                    print(f"row: {(r+1)}\n")
                    print(f"col: {(c+1)}\n")
                    if ((0<=r<=2) and (0<=c<=2)):
                         if (not chooseSpot(r,c,symbol,board)):
                              print("spot taken")
                         else: 
                              goodSpot = True
               printBoard(board)
               symbol = "X"
     else:
          symbol = "Q"




#computer vs player
#computer --> r = randomint(1,3) c = randomint(1,3) while r,c in board == "" the spot can be filled

#strategy
#if row or column -1 or +1 == "" computer guesses one of those spots 

