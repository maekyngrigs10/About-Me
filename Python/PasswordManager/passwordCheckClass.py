class passwordCheck:

    @staticmethod

    def getPassword(sc,cl,ll,nums,question):
        length = sc+cl+ll+nums
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
        return userInput