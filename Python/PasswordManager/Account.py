# method to create an account

class Account:
    
    def __init__(self,category,username,password,account):
        self.category = category
        self.username = username
        self.password = password
        self.account = account
        self.categories = []
        self.usernames = []
        self.password = []
        self.accounts = []
        
    def __str__(self):
        out = ""
        d = 0
        for c in self.categories:
            out += f"Category: {c}"
            j = 0
            print(out)
            for i in self.accounts:
                out += f"\n\taccount: {self.accounts[j][d]}\n\t\tusername: {self.usernames[j][d]}\n\t\tpassword: {self.password[j][d]}"
                j += 1
            d +=1
            print(out)
        return out

    def getCategory(self):
        return self.category

    def getAccount(self):
        return self.account

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getAccount(self,newAcct):
        self.accounts.append(newAcct)
    
    