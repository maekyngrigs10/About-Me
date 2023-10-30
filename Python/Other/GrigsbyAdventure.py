import random

#--------- Variables n' Stuff ---------#

#   ------ Misc     Variables ------   #  

answers = ["y","Y","n","N"]

returns = ""

secretNum = 0

#   ------ Story    Variables ------   #  

next = 0

spell = ""

place = "beginning"

status = "begin"

area = ""

spells = []

practice = 0

level = 0

actions      = ''' 
                    #---------------------------------------#
                    #-------------- Actions ----------------#
                    #---------------------------------------#
                    # ----- enter the following codes  -----#
                    #---------------------------------------#
                    # ---- p: level up w/spell practice ----#
                    #---------------------------------------#
                    #------ sb: show your spell book -------#
                    #---------------------------------------#
                    #----------- l: leave the room ---------#
                    #---------------------------------------#
                    #---------- e: learning center ---------#
                    #---------------------------------------#
                    #--------- s: learn spells -------------#
                    #---------------------------------------#
                    #--------- t: test spell level ---------#
                    #---------------------------------------#
                '''
masterSpellBook =       ''' #--------------------------------#
                            # ------ Master Spell Book ------#
                            #--------------------------------#
                            #   ---- Earthling  Spells ----  #
                            #--------------------------------#
                            # beginner (level 0-1):          #
                            #flowery towery: use to create a #
                            #   flowing landscape of flowers #
                            #        call: FP                #
                            #thorny: used to create vines as #
                            #   sharp as a needle            #
                            #        call: TH                #
                            #--------------------------------#
                            # Intermediate:                  #
                            # petal picker: turn anything in #
                            #   a blink of the eye to petals #
                            #       call: PP                 #
                            # growth spurto: make something  #
                            #    bigger or smaller           #
                            #       call: GS                 #
                            #--------------------------------#
                            # Master:                        #
                            #animalia: the ability to morph  #
                            #    into any animal you please  #
                            #        call: AN                #
                            #--------------------------------#
                            #  ----- Fiesty  Spells -----    #
                            #--------------------------------#
                            # beginner:                      #
                            #resisteance(FR): used to shield #
                            #    you from fire               #
                            #        call: RE                #
                            # fire bolt: creates a fine bolt #
                            #    of fire                     #
                            #        call: FB                #
                            #--------------------------------#
                            # Intermediate:                  #
                            # burn baby: creates a fire ring #
                            #    around an object/person     #
                            #        call: BB                #
                            # fire turnado: make a tornado   #
                            #    but of fire                 #
                            #        call: FT                #
                            #--------------------------------#
                            # Master:                        #
                            # here comes the boom: can blow  #
                            #    up something w/o dynamite   #
                            #        call: HB                #
                            #--------------------------------#
                            #   ----- Airea   Spells -----   #
                            #--------------------------------#
                            # beginner:                      #
                            # feather falling: allows them to#
                            #   land soft on their feet      #
                            #        call: FF                #
                            # windy loo hoo: creates a nice  #
                            #   gust of wind                 #
                            #        call: WH                #
                            #--------------------------------#
                            # Intermediate:                  #
                            # gusty dusty: combines wind with#
                            #   dust to help blind an enemy  #
                            #        call: GD                #
                            #cloudy w/ a chance of meatballs:#
                            #    weather phenomnon           #
                            #        call: CM                #
                            #--------------------------------#
                            # Master:                        #
                            # you can't see me: allows one   #
                            #   to make themself John Cena   #
                            #        call: JC                #
                            #--------------------------------#
                            #   ----- Aqua    Spells ------  #
                            #--------------------------------#
                            # beginner:                      #
                            # speedy quick: allows them to   #
                            # swim fast underwater           #
                            #        call: SQ                #
                            # wave bye bye: creates a nice   #
                            # wave of water                  #
                            #        call: WB                #
                            #--------------------------------#
                            # Intermediate:                  #
                            # the jesus: allows one to be    #  
                            # able to walk on water          #
                            #        call: TJ                #
                            # too icy: bling bling, but w    #
                            #    water freezing into ice     #
                            #        call: TI                #
                            #--------------------------------#
                            # Master:                        #
                            # lil mermaid: to be able to see #
                            #   and breath underwater        #
                            #       call: LM                 #
                            #--------------------------------#
                        '''

#   ------ Earthling Variables ------   #  

earthSpells =   '''
                            #--------------------------------#
                            #   ---- Earthling  Spells ----  #
                            #--------------------------------#
                            # beginner (level 0-1):          #
                            #flowery towery: use to create a #
                            #   flowing landscape of flowers #
                            #        call: FP                #
                            #thorny: used to create vines as #
                            #   sharp as a needle            #
                            #        call: TH                #
                            #--------------------------------#
                            # Intermediate:                  #
                            # petal picker: turn anything in #
                            #   a blink of the eye to petals #
                            #       call: PP                 #
                            # growth spurto: make something  #
                            #    bigger or smaller           #
                            #       call: GS                 #
                            #--------------------------------#
                            # Master:                        #
                            #animalia: the ability to morph  #
                            #    into any animal you please  #
                            #        call: AN                #
                            #--------------------------------#
                '''

#   ------ Fiesty    Variables ------   #  

fireSpells =    '''
                            #--------------------------------#
                            #  ----- Fiesty  Spells -----    #
                            #--------------------------------#
                            # beginner:                      #
                            #resisteance(FR): used to shield #
                            #    you from fire               #
                            #        call: RE                #
                            # fire bolt: creates a fine bolt #
                            #    of fire                     #
                            #        call: FB                #
                            #--------------------------------#
                            # Intermediate:                  #
                            # burn baby: creates a fire ring #
                            #    around an object/person     #
                            #        call: BB                #
                            # fire turnado: make a tornado   #
                            #    but of fire                 #
                            #        call: FT                #
                            #--------------------------------#
                            # Master:                        #
                            # here comes the boom: can blow  #
                            #    up something w/o dynamite   #
                            #        call: HB                #
                            #--------------------------------#
                '''

#   ------ Airea    Variables ------   #  

airSpells = '''
                            #--------------------------------#
                            #   ----- Airea   Spells -----   #
                            #--------------------------------#
                            # beginner:                      #
                            # feather falling: allows them to#
                            #   land soft on their feet      #
                            #        call: FF                #
                            # windy loo hoo: creates a nice  #
                            #   gust of wind                 #
                            #        call: WH                #
                            #--------------------------------#
                            # Intermediate:                  #
                            # gusty dusty: combines wind with#
                            #   dust to help blind an enemy  #
                            #        call: GD                #
                            #cloudy w/ a chance of meatballs:#
                            #    weather phenomnon           #
                            #        call: CM                #
                            #--------------------------------#
                            # Master:                        #
                            # you can't see me: allows one   #
                            #   to make themself John Cena   #
                            #        call: JC                #
                            #--------------------------------#
            '''

#   ------ Aquatics  Variables ------   #  

waterSpells =   '''
                            #--------------------------------#
                            #   ----- Aqua    Spells ------  #
                            #--------------------------------#
                            # beginner:                      #
                            # speedy quick: allows them to   #
                            # swim fast underwater           #
                            #        call: SQ                #
                            # wave bye bye: creates a nice   #
                            # wave of water                  #
                            #        call: WB                #
                            #--------------------------------#
                            # Intermediate:                  #
                            # the jesus: allows one to be    #  
                            # able to walk on water          #
                            #        call: TJ                #
                            # too icy: bling bling, but w    #
                            #    water freezing into ice     #
                            #        call: TI                #
                            #--------------------------------#
                            # Master:                        #
                            # lil mermaid: to be able to see #
                            #   and breath underwater        #
                            #       call: LM                 #
                            #--------------------------------#
                '''

#------------ Character Build ------------#
begin = input("are you ready to start your adventure? y/n   ")
if begin == "y" or "Y":
    print("great! I'm your adventure guide, Giddeon, I'll help you out on where to go and what to do, but I think it is time we start the story . . .")
else:
    print("really, you're gonna be like that . . .")
name = input("so what should we call you?   ")
print(f"wow nice to meet you{name}")
element = input("and what element: (e)arth, (f)ire, (w)ater, or (a)ir?  ")
if element == "e" or element == "E":
    element = "earth"
    print("FLOWER POWER!! I love it! You will go into the Grotto, in the middle of the Meadow just over the hill! I'll meet you over there!")
    choice = input("would you like to head to the Earthling Grotto? y/n ")
    if choice == "y" or choice == "Y":
        place = "grotto"
elif element == "f" or element == "F":
    element = "fire"
    print("Ooooo Fiesty, I like it! You will go into the Firepit, in the middle of the volcano mountain range just over the hill! I'll meet you over there!")
elif element == "a" or element == "A":
    element = "air"
    print("Very Breezy Baby, I'm here for it! You will go into the Cloud Kingdom, in the middle of the sky just go up the stairway to heave! I'll meet you over there!")
    place = "airea"
elif element == "w" or element == "F":
    element = "water"
    print("Ooooo Fiesty, I like it! You will go into the Firepit, in the middle of the volcano mountain range just over the hill! I'll meet you over there!")
    place = "aqua"
if place == "grotto":
    answer = input("Welcome to Earthling Grotto! At the Grotto they are all about helping the environment through learning various earthling spells. The more spells you learn and master, the more powerful you will become. Ready to see the dorms? y/n   ")
    while answer not in answers:
        answer = input("Sorry I don't think I understand, would you like to know about all the places to explore at The Grotto? y/n   ")
    if answer == "y" or answer == "Y":
        print("Well let's go check it out")
        area = "edorm"
elif place == "firepit":
    answer = input("Welcome to Fiesty Fireput! At the Firepit they are all about mastering the chaotic fire power through learning various fiesty spells. The more spells you learn and master, the more powerful you will become. Ready to see the dorms? y/n   ")
elif place == "airea":
    answer = input("Welcome to the Kingdom of Clouds! At Cloud they are all about mastering wind and breezes through learning various airea spells. The more spells you learn and master, the more powerful you will become. Ready to see the dorms? y/n   ")
elif place == "aqua":
    answer = input("Welcome to the Aquarium! At the Aquarium they are all about mastering very wavy currents through learning various aqua spells. The more spells you learn and master, the more powerful you will become. Ready to see the dorms? y/n   ")
#------------- Dorming Part of Game ----------------#

#--------- Earthling dorm Room --------#
while status == "begin":
    if area == "edorm":
        print("here you can practice the spells you learn at the learning center, which I will show you after this")
        print(f"to see what all you can do in a certain place enter: actions, only when there is {name}: , let's try it out!")
        user = input(f"{name}: ")
        while user != "actions":
            print("practice first please . . .")
            user = input(f"{name}: ")
        if user == "actions":
            print(actions)
        print(f"when you see: {name}:, you can also enter 'l' , try it out")
        user = input(f"{name}: ")
        if user == "l":
            area = "mid"
            next = 1
    status = "mid"


#---- Navigating between places Grotto Edition ----#

while (status != "begin") and (place == "grotto"):
    print(f"you are at {area} and level {level} so what will you do . . .")
    user = input(f"{name}   ")
    if (user == "s"):
        area = "class"
        print(f"welcome to the classroom! Here you will teach yourself all of your spells! To learn a spell you first must pass the test, when you pass the test it will be added to your spell book!")
        print(f"let's find out what level you are so we can see which spells you can do . . . it looks like you are level {level}! Let's call on the spell book to see what spells you can learn!   ")
        user = input(f"{name}:  ")
    if (user == "sb") and area != "class":
        print(earthSpells)
    if (user == "sb") and (area == "class"):
        print(earthSpells)
        if level == 0:
            print("let's start with the beginner spell, to start learning/practicing enter the call for the spell. If you don't remember the call look back at the spellbook to see. And when you feel ready, take the test to master the spells and level up. Good luck! ")
    if user == "s" and area == "class":
        print("practice time! enter the call for the spell to gain practice points, the more practice points the better you will get. ")
    if user == "p":
        while user != "t":
            user = input(f"{name}:  ")
            practice += 1
        if user == "t":
            area = "test"
    if user == "actions":
        print(actions)
    if user == "l" and area == "edorm":
        area = "mid"
    if user == "l" and area == "lc":
        area = "mid"
    if user == "e" and area == "mid":
        area = "lc"
    if user == "FP" and (level >= 0):
        print(f"{name}: oooooo, pretty flowers, wait way too many flowers")
    if user == "TH" and (level >= 1):
        print(f"{name}: wow so sharp, ow ow ow omg make it stop")
    if user == "PP" and (level >= 2):
        print(f"{name}: now that's petals, ooo and they're a petal, oh man not my bed . . ., but i guess it is pretty cute")
    if user == "GS" and (level >= 3):
        print(f"{name}: i mean my coffee could be a little bit bigger . . . oh no there goes my ceiling, again")
    if user == "AN" and (level >= 4):
        print(f"{name}: soooo you said you like cats *morphs into a cat*, how are you feeling about me right about now . . .*meows*")
    if user == "l":
        area = "mid"
    if area == "lc":
        print("welcome to the learning center!  ")
    if area == "test":
        #---- Spell Test Check ----#
        print(level)
        print(f"welcome to the testing area, it seems you have {practice} points. Well done! Let's see what spell you can test for . . .")
        if level == 0: 
            print("you are able to test for FP, flowery towery. Are you ready for the test? y/n ")
            user = input(f"{name}:  ")
        elif level == 1:
            print("you are able to test for TH, thorny. Are you ready for the test? y/n ")
            user = input(f"{name}:  ")
        elif level == 2:
            print("you are able to test for PP, petal picker. Are you ready for the test? y/n ")
            user = input(f"{name}:  ")
        elif level == 3:
            print("you are able to test for GS, growth spurto. Are you ready for the test? y/n ")
            user = input(f"{name}:  ")
        elif level == 4:
            print("you are able to test for AN, animalia. Are you ready for the test? y/n ")
            user = input(f"{name}:  ")
        #------ Guess a Number -------#
        if level == 0 and user == "y":
            spell = "Flowery Towery"
            print("try to tune in your powers to guess the right number 1-50 . . .")
            secretNum = random.randint(0,50)
            user = int(input(f"whats your guess {name} . . . "))
            while user != secretNum:
                if user < secretNum:
                    print("too low . . .")
                elif user > secretNum:
                    print("too high . . .")
                elif user > 50:
                    print("out of range . . .")
                elif user < 0:
                    print("out of range . . .")
                user = int(input(f"wrong, whats your guess {name} . . . "))
            if user == secretNum:
                    print("congrats! You passed!! Now that spell will be added to your spell book!! ")
                    spells += f"Level {level}:\t{spell}\n"
                    level += 1
        elif level == 1 and user == "y":
            spell = "Thorny"
            print("try to tune in your powers to guess the right number 1-75 . . .")
            secretNum = random.randint(0,75)
            user = int(input(f"whats your guess {name} . . . "))
            while user != secretNum:
                if user < secretNum:
                    print("too low . . .")
                elif user > secretNum:
                    print("too high . . .")
                elif user > 75:
                    print("out of range . . .")
                elif user < 0:
                    print("out of range . . .")
                user = int(input(f"wrong, whats your guess {name} . . . "))
            if user == secretNum:
                    print("congrats! You passed!! Now that spell will be added to your spell book!! ")
                    spells += f"Level {level}:\t{spell}\n"
                    level += 1
        elif level == 2 and user == "y":
            spell = "Petal Picker"
            print("try to tune in your powers to guess the right number 1-125 . . .")
            secretNum = random.randint(0,125)
            user = int(input(f"whats your guess {name} . . . "))
            while user != secretNum:
                if user < secretNum:
                    print("too low . . .")
                elif user > secretNum:
                    print("too high . . .")
                elif user > 125:
                    print("out of range . . .")
                elif user < 0:
                    print("out of range . . .")
                user = int(input(f"wrong, whats your guess {name} . . . "))
            if user == secretNum:
                    print("congrats! You passed!! Now that spell will be added to your spell book!! ")
                    spells += f"Level {level}:\t{spell}\n"
                    level += 1
        elif level == 3 and user == "y":
            spell = "Growth Spurto"
            print("try to tune in your powers to guess the right number 1-250 . . .")
            secretNum = random.randint(0,250)
            user = int(input(f"whats your guess {name} . . . "))
            while user != secretNum:
                if user < secretNum:
                    print("too low . . .")
                elif user > secretNum:
                    print("too high . . .")
                elif user > 250:
                    print("out of range . . .")
                elif user < 0:
                    print("out of range . . .")
                user = int(input(f"wrong, whats your guess {name} . . . "))
            if user == secretNum:
                    print("congrats! You passed!! Now that spell will be added to your spell book!! ")
                    spells += f"Level {level}:\t{spell}\n"
                    level += 1
        elif level == 4 and user == "y":
            spell = "Animalia"
            print("try to tune in your powers to guess the right number 1-1000 . . .")
            secretNum = random.randint(0,1000)
            user = int(input(f"whats your guess {name} . . . "))
            while user != secretNum:
                if user < secretNum:
                    print("too low . . .")
                elif user > secretNum:
                    print("too high . . .")
                elif user > 1000:
                    print("out of range . . .")
                elif user < 0:
                    print("out of range . . .")
                user = int(input(f"wrong, whats your guess {name} . . . "))
            if user == secretNum:
                    print("congrats! You passed!! Now that spell will be added to your spell book!! ")
                    spells += f"Level {level}:\t{spell}\n"
                    level += 1
    if level == 5:
        print("you are now an all powerful earthling! bye bye")
        status = "end"