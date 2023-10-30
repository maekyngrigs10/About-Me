def DBencrypter():
    s = 5

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
        
    file2 = open(f"AccountsDB.csv","w")
    file2.write(f"{result}")
    file2.close()

DBencrypter()