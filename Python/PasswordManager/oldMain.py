# main file for password manager

from Account import Account

users = []





def newUser():
    file1 = open("AccountsDV.csv","w")

    firstName = input("first name: ")
    lastName = input("last name: ")
    username = input("username: ")
    password = input("password: ")

    w = f"{firstName},{lastName},{username},{password}"
    newAcct = w
    file1.write(newAcct)
    file1.close()

    file1 = open("AccountsDB.csv","r")

    file = file1.readlines()
    for line in file:
        firstName,lastName,username,password = line.rstrip().split(",")
        newAcct = Account(firstName, lastName,username,password)
        users.append(newAcct)
        print(line)
    file1.close()

ui= input("(s)ign-up or (l)ogin")

if ui == "s":
    newUser()

# login process kind of

username = input(' enter your username: ')
if username == 'urmom':
   print("checking username")
   print("username is right") 
   password = input(' type your password: ')
   if password == 'addi':
        print("password is correct") 
   else:
        print("not correct")
        exit()
else:
    print("username is not right") 

    exit()

