# password manager

# start of modules, classes, and other imports

import random

from CheckInput import CheckInput

# end of modules, classes, and other imports

# start of initializing variables

dbFile = "AccountsDB.csv"

usernames = []

passwords = []

DBusernames = []

DBpasswords = []

accts = []

# userFile = ""

navMenu = '''

#-------- Navigation --------#

# "v" : view all accounts

# "n" : make a new password

# "e" : edit password manager

# "x" : exit password manager

# "m" : view nav menu

# "a" : add an account

#----------------------------#

'''


# end of variables

# login function for returning users

def login():

    global userFile
    global usernamePM

    file1 = open("AccountsDB.csv","r")
    file = file1.readlines()

    for line in file:
        DBusername,DBpassword = line.rstrip().split(",")

        DBusernames.append(DBusername)

        DBpasswords.append(DBpassword)

    usernamePM = input("username: ")
    if usernamePM in DBusernames:
        print("valid username -- enter password")

        i = DBusernames.index(usernamePM)

        password = input("password: ")
        
        if DBpasswords[i] == password:
            print(f"welcome {usernamePM} . . . please enter your desired password manager filename (must be .csv only) . . .")
            userFile = input("file: ")
            if userFile != "":
                decrypter(userFile)
                loadUserFile(userFile)
        
        else:
            t = 0
            while (password != passwords[i]) and t != 3:
                print("try again")
                t += 1
                password = input("password: ")
            if t == 3:
                print("re-login")
                login()
    
    else:
        print("not a valid username -- (t)ry again or (s)ign-up")
        user = input("user: ")
        CheckInput.getCorrectInput(user,["t","s"],"not a valid username -- (t)ry again or (s)ign-up")
        if user == "t":
            login()
        else:
            signup()

# end of login function

# function allows a returning user enter their data from the PM to pick up where they left off

def loadUserFile(files):

    file2 = open(files,"r")
    file = file2.readlines()

    for line in file:
        
        acct,username,password = line.rstrip().split(",")

        accts.append(acct)

        usernames.append(username)

        passwords.append(password)
    
    print("would you like to see your accounts? y/n ")
    user = input("user: ")
    CheckInput.getCorrectInput(user,["y","n"],"would you like to see your accounts? y/n ")
    if user == "y":
        printAccts()
    else:
        print("back to main command screen")

# end of load user file

# update user file function

def updateFile():
    global accts
    global usernames
    global passwords
    global userFile
    print(userFile)
    file = open(f"{userFile}","w")
    for a in range(len(accts)):
        file.write(f"{accts[a]},{usernames[a]},{passwords[a]}\r")
    file.close()

# print accounts function

def printAccts():

    print(f"\n now viewing accounts\n")

    viewer = ""

    for a in accts:
        viewer = (f"account: {a}\n")
        i = accts.index(a)
        viewer += (f"\tusername: {usernames[i]}\n\tpassword: {passwords[i]}\n\n")
        print(viewer)
    

# end of print accounts function       

# sign-up function

def signup():

    global NewUsername

    global usernamePM

    global passwordPM

    global userFile

    global DBusernames

    global DBpasswords

    file1 = open("AccountsDB.csv","r")
    file = file1.readlines()

    for line in file:
        username,password = line.rstrip().split(",")
        DBusernames.append(username)
        DBpasswords.append(password)

    NewUsername = input("username: ")
    while NewUsername in DBusernames:
        print("username is taken . . . try again . . . ")
        NewUsername = input("username: ")
    NewPassword = input("password: ")
    checkPasswords(NewPassword)
    DBusernames.append(NewUsername)
    DBpasswords.append(NewPassword)

    print(DBusernames)
    print(DBpasswords)

    print(f"welcome {NewUsername} . . . let's add your first account . . .")
    usernamePM = NewUsername
    passwordPM = NewPassword

    userFile = f"{NewUsername}.csv"
    file1 = open(f"{userFile}","w")
    file1.write(f"{NewUsername},{NewPassword}")
    file1.close()
    addNewUser()
    addAccount()

# end of sign up function

# adds a new user to the database

def addNewUser():
    global userFile

    global DBusernames

    global DBpasswords

    global passwordPM

    global usernamePM

    j = len(usernames)-2
    file1 = open("AccountsDB.csv","r")
    file = file1.readlines()

    lines = ""
    for line in file:
        username,password = line.rstrip().split(",")
        lines += f"{username},{password}\n"
    lines += f"{usernamePM},{passwordPM}\n"

    # te.encrypter(userFile)
    file2 = open("AccountsDB.csv","w")
    file2.write(lines)
    file2.close()

# end of add new user function

# add a new account and it's information

def addAccount():

    print(f"\n now adding account\n")

    print("enter account name . . .")
    acct = input("account: ")
    if acct in accts:
        print("this acct already exists . . . would you like to continue adding? y/n ")
        user = input("user: ")
        CheckInput.getCorrectInput(user,["y","n"],"this acct already exists . . . would you like to continue adding? y/n ")
        if user == "n":
            print("back to main command screen")
        else:
            username = input("username: ")
            
            print("would you like to use a randomly generated password? y/n ")
            user = input("user: ")
            CheckInput.getCorrectInput(user,["y","n"],"would you like to use a randomly generated password? y/n ")
            if user == "y":
                password = passwordMaker()
            else:
                password = input("password: ")
                password = checkPasswords(password)

            usernames.append(username)
            passwords.append(password)
            accts.append(acct)

            updateFile()
    else:
        username = input("username: ")
        print("would you like to use a randomly generated password? y/n ")
        user = input("user: ")
        CheckInput.getCorrectInput(user,["y","n"],"would you like to use a randomly generated password? y/n ")
        if user == "y":
            password = passwordMaker()
        else:
            password = input("password: ")
            checkPasswords(password)

        accts.append(acct)
        usernames.append(username)
        passwords.append(password)

        updateFile()
    
    print("account added . . .")
    print(f"account: {acct}\n\tusername: {username}\n\tpassword: {password}")

    print("add another account? y/n")
    user = input("user: ")
    CheckInput.getCorrectInput(user,["y","n"],"add another account? y/n")
    if user == "y":
        addAccount()
    else:
        print("back to main command screen")

# end of add account function

# password maker function

def passwordMaker():

    print(f"\n now making a password\n")

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

    print(f"password: {password}\n")

    return password


# end of password maker function

# check password method

def checkPasswords(password):

    global allCharacters

    allCharacters = (33,64,35,36,37,38,40,41,42,43,45,48,49,50,51,52,53,54,55,56,57,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122)

    specialCharacters = (33,64,35,36,37,38,40,41,42,43,45)

    sc = 0
    cl = 0
    ll = 0
    nums = 0

    for c in password:
        char = ord(c)
        if char in range(65,90):
            cl += 1
        elif char in range(97,122):
            ll += 1
        elif char in specialCharacters:
            sc += 1
        else:
            nums += 1
    total = nums + sc+ ll + cl
    if total < 8 or cl <= 0 or ll <= 0 or sc <= 0 or nums <= 0:
        print("one or more of password requirements were not met: 8 characters, at least 1 uppercase,lowercase,number,and special character")
        print("try again . . .")
        password = input("password: ")
        checkPasswords(password)
    else:
        return password
    
# end of check password method

# edit passwords and accounts function

def editPM():
    print("do you want to (m)odify or (d)elete an account? ")
    user = input("user: ")
    CheckInput.getCorrectInput(user,["m","d"],"do you want to (m)odify or (d)elete an account? ")
    if user == "m":
        print("what account do you want to modify? ")
        print(printAccts())
        user = input("user: ")
        while user not in accts:
            print("that account does not exist . . .try again")
            user = input("user: ")
        k = accts.index(user)
        print("what would you like to modify: (a)ccount name, (u)sername, (p)assword, or (e)verything")
        user = input("user: ")
        CheckInput.getCorrectInput(user,["a","p","u","e"],"what would you like to modify: (a)ccount name, (u)sername, (p)assword, or (e)verything")
        if user == "a":
            print(accts[k])
            print("what is the new account name? ")
            user = input("user: ")
            accts[k] = user
        elif user == "u":
            print(usernames[k])
            print("what is the new username? ")
            user = input("user: ")
            usernames[k] = user
            print(f"account: {accts[k]}\n\tusername: {usernames[k]}\n\tpassword: {passwords[k]}")
        elif user == "p":
            print(passwords[k])
            print("what is the new password? ")
            user = input("user: ")
            passwords[k] = user
            print(f"account: {accts[k]}\n\tusername: {usernames[k]}\n\tpassword: {passwords[k]}")
        elif user == "e":
            print(accts[k])
            print("what is the new account name? ")
            user = input("user: ")
            accts[k] = user
            print(usernames[k])
            print("what is the new username? ")
            user = input("user: ")
            usernames[k] = user
            print(passwords[k])
            print("what is the new password? ")
            user = input("user: ")
            passwords[k] = user
            print(f"account: {accts[k]}\n\tusername: {usernames[k]}\n\tpassword: {passwords[k]}")
        print("back to main command screen")
    elif user == "d":
        print("what account do you want to delete? ")
        print(printAccts())
        user = input("user: ")
        while user not in accts:
            print("that account does not exist . . .try again")
            user = input("user: ")
        k = accts.index(user)
        del accts[k], usernames[k], passwords[k]
        print("account deleted")
        print("back to main command screen")

# end of edit function

# save and close PM function

def saveAndExit():

    global usernamePM
    global userFile

    print(f"see you next time {usernamePM}")
    


# end of save and close PM function

s = 5

# encrypter function

def DBencrypter(files):
    global result 
    global s
    global dbFile

    file1 = open("AccountsDB.csv","r")
    file = file1.readlines()

    result = ""

    for line in file:
        username,password = line.rstrip().split(",")

        for u in username:
            if (u.isupper()):
                result += chr((ord(u) + s))
                # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(u) + s ))
        result += ","
        for p in password:
            if (p.isupper()):
                result += chr((ord(p) + s))
                # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(p) + s ))
        result += f"\n"
        
    file2 = open(f"{files}","w")
    file2.write(f"{result}")
    file2.close()
        
# end on encrypter

# DB decrypter function
def DBdecrypter(files):
    global result 
    global s

    result = ""

    file1 = open(f"{files}","r")
    file = file1.readlines()

    for line in file:
        username,password = line.rstrip().split(",")

        for u in username:
            if (u.isupper()):
                result += chr((ord(u) - s))
                # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(u) - s ))
        result += ","
        for p in password:
            if (p.isupper()):
                result += chr((ord(p) - s))
                # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(p) - s ))
        result += f"\n"

        file2 = open("AccountsDB.csv","w")
        file2.write(result)
        file2.close()

# end of DB decrypter function

# decrypter of user's file function

def decrypter(files):
    global result 
    global s

    result = ""

    file1 = open(f"{files}","r")
    file = file1.readlines()

    for line in file:
        acct,username,password = line.rstrip().split(",")
        for a in acct:
            if (a.isupper()):
                result += chr((ord(a) - s))
                # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(a) - s ))
        result += ","
        for u in username:
            if (u.isupper()):
                result += chr((ord(u) - s))
                # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(u) - s ))
        result += ","
        for p in password:
            if (p.isupper()):
                result += chr((ord(p) - s))
                # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(p) - s ))
        result += f"\n"

        file2 = open(f"{files}","w")
        file2.write(result)
        file2.close()
# end of user file decrypter function

# user file encrypter function

def encrypter(files):
    global result 
    global s
    global dbFile

    file1 = open(f"{files}","r")
    file = file1.readlines()

    result = ""

    for line in file:
        acct,username,password = line.rstrip().split(",")
        for a in acct:
            if (a.isupper()):
                result += chr((ord(a) + s))
                # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(a) + s ))
        result += ","
        for u in username:
            if (u.isupper()):
                result += chr((ord(u) + s))
                # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(u) + s ))
        result += ","
        for p in password:
            if (p.isupper()):
                result += chr((ord(p) + s))
                # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(p) + s ))
        result += f"\n"
        
    file2 = open(f"{files}","w")
    file2.write(f"{result}")
    file2.close()

# end of user file encrypter

# end of all functions

# login or signup

print("(l)ogin or (s)ign-up")

user = input("user: ")
CheckInput.getCorrectInput(user,["l","s"],"(l)ogin or (s)ign-up")
if user == ("l"):
    DBdecrypter(dbFile)
    login()
else:
    decrypter(dbFile)
    signup()

# end of login/sign-up

print(navMenu)

# start of mainloop

while user != "x":

    print("what would you like to do? ")
    user = input("user: ")
    CheckInput.getCorrectInput(user,["v","n","x","m","a","e"],"what would you like to do? ")

    if user == "v":
        printAccts()

    elif user == "n":
        passwordMaker()

    elif user == "e":
        editPM()

    elif user == "m":
        print(navMenu)

    elif user == "a":
        addAccount()

if user == "x":
    saveAndExit()
    print(f"thanks for using Password Manager, here take your acct info, so you can login and have everything waiting for you! your file name is {userFile}")
    DBencrypter(dbFile)
    encrypter(userFile)
    printAccts()

    

