
# beginning of main functions

def getNames(FILENAME):
        
    names = []
    
    # open the file
    
    file1 = open(FILENAME,"r")
    
    # loop through each line of the file
    
    for line in file1:
        
        index = 0
        
        leaderName = ""
        
    # get the information up to the ","
    
        while(line[index]!= ","):
        
            leaderName += line[index]
            
            index += 1
        names.append(leaderName)

    
    # return that information
    
    return names

def getScores(FILENAME):
    
    scores = []
    
    # open the file
    
    file1 = open(FILENAME,"r")
    
    # get info up to the ","
    
    for line in file1:
        
        index = 0
        
        leaderScore = ""
        
        # get the info up to the ","
        
        while (line[index] != ","):
            
            index += 1
            
        index += 1
         
        while (line[index] != "\n"):
            
            leaderScore += line[index]
            
            index += 1
        
        scores.append(leaderScore)
        
    # return information
    
    return scores
    

def updateLeaderboard(FILENAME,leaderName,leaderScores,playerName,playerScore):
    
    # loop through all the scores in the current leaderboard
    
    index = 0
    
    while (index<len(leaderScores)):
    
        # check if the score can be inserted into this position
        
        if (playerScore >= int(leaderScores[index])):
            
            break
        
        else:
        
            index += 1
            
    # insert player info
        
    leaderName.insert(index,playerName)
    
    leaderScores.insert(index,playerScore)
    
    # ensure only 5 players are on the leaderboard
    
    if (len(leaderName)>5):
        
        leaderName.pop()
        
        leaderScores.pop()
        
    # save the data back to the database
    
    file1 = open(FILENAME,"w")
    
    # loop through the lists and save each list to the file
    
    for i in range(len(leaderName)):
        
        file1.write(f"{leaderName[i]},{leaderScores[i]}\n")
        
    file1.close()

# not best habits to do this bc it is a visual in a mainly function file

# draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
    #high_scorer is a boolean to tell if the current user is a high_scorer
    
    # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.goto(-160,100)
    turtle_object.hideturtle()
    turtle_object.down()
    
    index = 0
    # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
    while (index < len(leader_scores)):
        turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
        turtle_object.penup()
        turtle_object.goto(-160,int(turtle_object.ycor())-50)
        turtle_object.down()
        index = index + 1
    
    # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.pendown()
    
    # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.pendown()
    
    # display a gold/silver/bronze message if player earned a medal
    
    gold = int(leader_scores[0])
    silver = int(leader_scores[1])
    bronze = int(leader_scores[2])
  
    if player_score >= gold:
        turtle_object.write("you earned a gold medal!", font=("Times New Roman",10,"bold"))
    elif player_score >= silver:
        turtle_object.write("you earned a silver medal!", font=("Times New Roman",10,"bold"))
    elif player_score >= bronze:
        turtle_object.write("you earned a bronze medal!", font=("Times New Roman",10,"bold"))
        



# end of main functions 

# testing functions area


print(getNames("Database.txt"))

print(getScores("Database.txt"))
