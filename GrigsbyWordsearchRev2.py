# --- imports --- #

from termcolor import colored

import random as r

# --- variables --- #

wordsearch = []
words = []
printWS = []

wordsearchFile = ""
wordsFile = ""

allPOS = []
place = []

numOfWords = 0

colors = ["yellow","green","blue","magenta","cyan","red","light_red","light_green","light_yellow","light_blue","light_magenta","light_cyan"]

# --- Functions --- #

def configureFile(wordsearchFile,wordsFile):

    global wordsearch
    global words
    global printWS

    # read the wordsearch file and append it all to the wordsearch variable

    file1 = open(wordsearchFile,"r")
    file = file1.readlines()

    row = ""
    numOfRows = 0
    numOfCols = 0

    i = 0

    for lines in file:
        i += 1
        for l in range(len(lines)):
            char = lines[l]
            if char == "\n" or char == "\t" or  char == "-" or char == " " or char == ",":
                lines.replace(char,",")
            else:
                row += char
                numOfCols += 1
        if i == 1:
            length = len(row)
        numOfRows += 1
        wordsearch.append(row)
        
        if len(row) != length:
            
            print(f"this file is no bueno\n\tin row #{numOfRows} only has {len(row)} columns instead of {length}\nplease try again")
            wordsearchFile = input("file: ")
            wordsearch = []
            configureFile(wordsearchFile,wordsFile)
            row = ""
            
        # print(row)

        row = ""

    # read the words file and get the words

    file1 = open(wordsFile,"r")
    file = file1.readlines()

    wordle = ""

    for line in file:

        # words.append(line)

        for l in range(len(line)):
            if line[l] == " " or line[l] =="\n" or line[l] =="\t" or line[l] == "," or line[l] == "-":
                words.append(wordle)
                wordle = ""
            else:
                wordle+= line[l]

    printWordsearch()
	
	
	

def printWordsearch():
    global wordsearch

    line = ""
    j = 1

    print(f"\n# --------------------------------- #\n")
    print(f"\n        HERE'S THE WORDSEARCH     \n")

    # print the wordsearch board
    for r in range(len(wordsearch)):
        for c in range(len(wordsearch[r])):
            if j == 1:
                print(f"    {wordsearch[r][c]}",end=" ")
                j -= 1
            else:
                print(wordsearch[r][c],end=" ")
        print()
        j += 1

    # print the words
    for w in range(len(words)):
        if w%2 == 0:
            line += (f"\n     {words[w]}\t")
        else:
            line += (f"  {words[w]}")
    print(f"{line}")
    
    print()


	
def findLetter(wordsearch, word):
	# goes through and tries to find the word
	# appends first character positions in list

	location = []
	first = word[0]

	for i in range(0, len(wordsearch)):
		for j in range(0, len(wordsearch[i])):
			if (wordsearch[i][j] == first):
				location.append([i,j])

	# check all starting pos for word
	for p in location:
		if checkFirst(wordsearch, word, p):
			# if word found
			return
	# if word not found
	print(f"  '{word}'   CAN NOT BE FOUND\n")


def checkFirst (wordsearch, word, location):
	# sees if the word starts at the location pos and returns true if it is found

	directions = [[-1,1], [0,1], [1,1], [-1,0], [1,0], [-1,-1], [0,-1], [1,-1]]

	# Iterate through all directions and check each for the word
	for d in directions:
		if (checkAround(wordsearch, word, location, d)):
			return True


def checkAround (wordsearch, word, location, dir):
    global printWS
    global allPOS
    global colors
    global place
    global numOfWords

    printWS = []

    i =1

	# if the word is in the direction compared to the location pos then it will return true and tell the user

    matches = [word[0]] # first character already found and characters found in that direction
    start = location # position we are looking at
    pos = [location] # positions we have looked at

    while (checkMatch(matches, word)):
        if (len(matches) == len(word)):

            color = r.choice(colors)
            # if all characters have been found, then it tells the user

            print(colored(f"# --------------------------------- #",color))
            numOfWords += 1

            colour = colored(word,color)

            print(f"\n\tHERE'S   '{colour}'  \n")
            
            # show the words position --> prints it to the terminal
            for row in range(len(wordsearch)):
                line = ""
                for col in range(len(wordsearch[row])):
                    spot = False
                    for z in pos:
                        if (z[0] == row) and (z[1] == col):
                            spot = True
                            place = [row,col]
                            allPOS.append(place)
                    if (spot):
                        line = line + " " + colored(wordsearch[row][col],color)
                    else:
                        # line = line + " -"
                        line = line + " " + wordsearch[row][col]
                printWS.append(line)
                print(f"   {line}")
            if i == 1:
                print(f"\n\n     {colour}'S START LOCATION \n\t     row : {place[0]+1}\n\t     col : {place[1]+1} \n")
                i -= 1
            print()
            return True

		# Have not found enough letters so look at the next one
        start = [start[0] + dir[0], start[1] + dir[1]]
        pos.append(start)
        if (checkIndex(wordsearch, start[0], start[1])):
            matches.append(wordsearch[start[0]][start[1]])
        else:
            # Reached edge of wordsearch and not found word
            return

def checkMatch (found, word):
	# goes through and sees if the letters found are a match to the word

	index = 0

	for i in found:
		if (i != word[index]):
			return False
		index += 1
	return True

def checkIndex (wordsearch, row, col):
	# checks if the row and col are correct
    # if outta reach it returns that that spot es no bueno

	if ((row >= 0) and (row < len(wordsearch))):
		if ((col >= 0) and (col < len(wordsearch[row]))):
			return True
	return False

def showAll():

    global allPOS
    global wordsearch
    global colors
    global numOfWords

    final = ""

    color=r.choice(colors)

    print(colored(f"# --------------------------------- #",color))

    print(f"\n     Here's all of them together\n")

    for row in range(len(wordsearch)):
        for col in range(len(wordsearch[row])):
            color=r.choice(colors)
            if [row,col] in allPOS:
                # color=r.choice(colors)
                final += colored(wordsearch[row][col],color) + " "
            else:
                final += wordsearch[row][col] + " "
        print(f"    {final}")
        final = ""
        
    # print(numOfWords)

    print(colored(f"\n\n# --------------------------------- #",color))


# --- main loop --- #

wordsearchFile = input("file: ")
# get the words for the wordsearch

print("please type the file name for the words")
wordsFile = input("word file: ")

configureFile(wordsearchFile,wordsFile)


for w in words:
	findLetter(wordsearch,w)

showAll()