# s = 5
# usernames = []
# passwords = []
# encrypts = []
# result = ""
# char = ""

# # files = "testingPM.csv"

# # userFile = "usersEncrypt.csv"

# def encrypter(files):
#     global result 

#     file1 = open(f"{files}","r")
#     file = file1.readlines()

#     for line in file:
#         acct,username,password = line.rstrip().split(",")

#         for u in username:
#             if (u.isupper()):
#                 result += chr((ord(u) + s))
#                 # Encrypt lowercase characters in plain text
#             else:
#                 result += chr((ord(u) + s ))
#         result += ","
#         for p in password:
#             if (p.isupper()):
#                 result += chr((ord(p) + s))
#                 # Encrypt lowercase characters in plain text
#             else:
#                 result += chr((ord(p) + s ))
#         result += f"\n"
        
#     file2 = open(f"{userFile}","w")
#     file2.write(f"{result}")
#     file2.close()
        

# def decrypter(files):
#     global result 

#     file1 = open(f"{files}","r")
#     file = file1.readlines()

#     for line in file:
#         username,password = line.rstrip().split(",")

#         for u in username:
#             if (u.isupper()):
#                 result += chr((ord(u) + s))
#                 # Encrypt lowercase characters in plain text
#             else:
#                 result += chr((ord(u) - s ))
#         result += ","
#         for p in password:
#             if (p.isupper()):
#                 result += chr((ord(p) - s))
#                 # Encrypt lowercase characters in plain text
#             else:
#                 result += chr((ord(p) - s ))
#         result += f"\n"
#         print(result)




# encrypter(files)

# filen = "usersEncrypt.csv"

# decrypter(filen)


# # for i in range(len(passwords)):
# #     char = passwords[i]
# #     for p in char:
            
# #         # Encrypt uppercase characters in plain text

# #         if (char.isupper()):
# #             result += chr((ord(char) + s))#-65) % 26 + 65)
# #             # Encrypt lowercase characters in plain text
# #         else:
# #             result += chr((ord(char) + s ))
# #         print(result)






# # github,meggrigs,puppywuppy
# # BBC,baddest,beach
# # sugar Daddies,sugar_baby_1,sugacube
# # gmail,maekyn.grigsby@evsck12.com,8024006
# # echo,maekyn.grigsby,uq5WJK+)#*