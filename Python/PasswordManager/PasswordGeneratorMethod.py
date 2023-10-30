import random

allCharacters = (33,64,35,36,37,38,40,41,42,43,45,48,49,50,51,52,53,54,55,56,57,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122)

specialCharacters = (33,64,35,36,37,38,40,41,42,43,45)


def passwordMaker():

    allCharacters = (33,64,35,36,37,38,40,41,42,43,45,48,49,50,51,52,53,54,55,56,57,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122)

    specialCharacters = (33,64,35,36,37,38,40,41,42,43,45)

    password = ""

    sc = int(input("how many special characters?    ")) # special characters

    cl = int(input("how many capital letters?  ")) # capital letters

    ll = int(input("how many lowercase letters?  ")) # lowercase letters

    nums = int(input("how many numbers?  ")) # numbers

    passwordLength = sc + cl + ll + nums

    if (sc <= 0) or (cl <= 0) or (ll <= 0) or (nums <= 0) or passwordLength < 8:
        while passwordLength < 8 or (sc <= 0) or (cl <= 0) or (ll <= 0) or (nums <= 0) :
            print("one or more of the following requirements were not met: must be at least 8 characters long, must have 1 special character, 1 capital letter, 1 lowercase letter, and 1 number  . . . so let's try again . . .")
            sc = int(input("how many special characters?    ")) # special characters
            cl = int(input("how many capital letters?  ")) # capital letters
            ll = int(input("how many lowercase letters?  ")) # lowercase letters
            nums = int(input("how many numbers?  ")) # numbers
            passwordLength = sc + cl + ll + nums
        while passwordLength > 0:
            i = random.randint(48,122)
            if i in range(48,57):
                if nums != 0:
                    nums -= 1
                    password += chr(i)
                    passwordLength -= 1
            elif i in range(65,90):
                if cl != 0:
                    cl -= 1
                    password += chr(i)
                    passwordLength -= 1
            elif i in range(97,122):
                if ll != 0:
                    ll -= 1
                    password += chr(i)
                    passwordLength -= 1
            elif i in specialCharacters :
                if sc != 0:
                    sc -= 1
                    password += chr(i)
                    passwordLength -= 1
    else: 
        while passwordLength > 0:
            i = random.choice(allCharacters)
            if i in range(48,57):
                if nums != 0:
                    nums -= 1
                    password += chr(i)
                    passwordLength -= 1
            elif i in range(65,90):
                if cl != 0:
                    cl -= 1
                    password += chr(i)
                    passwordLength -= 1
            elif i in range(97,122):
                if ll != 0:
                    ll -= 1
                    password += chr(i)
                    passwordLength -= 1
            elif i in specialCharacters :
                if sc != 0:
                    sc -= 1
                    password += chr(i)
                    passwordLength -= 1

    print(password)
    runAgain()

def runAgain():
    print("enter 'quit' to stop program or enter 'new' to make a new password . . .")
    
    ui = input("user: ")

    if ui == "new":
        passwordMaker()
    elif ui == "quit":
        print("thanks for using my password generator! ")
    else:
        while(ui != "quit") or (ui != "new"):
            print("invalid input, enter 'quit' to stop program or enter 'new' to make a new password . . .")
    
            ui = input("user: ")
            if ui == "new":
                passwordMaker()
            elif ui == "quit":
                print("thanks for using my password generator! ")
                exit()

passwordMaker()



