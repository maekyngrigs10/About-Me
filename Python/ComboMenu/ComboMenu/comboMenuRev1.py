#variables
answers = ["y","Y","n","N"]
count = 1

#for sandwich
numOfSandwiches = 0
sandwichType = ["c","C","b","B","t","T"]

#for fries
numOfFries = 0

#for drinks
numOfDrinks = 0

#for drinks and fries
sizeOptions = ["s","S","m","M","l","L"]

#for ketchup
ketchup = 0

#for checkout
subtotal = 0
tax = 0
total = 0
orderInformation = ""
order =[]

#sandwich ordering station
answer = input("would you like a sandwich? y/n      ")
while answer not in answers:
    answer = input("not valid answer, try again . . .    ")
if answer in answers:
    if answer == "y" or answer == "Y":
        numOfSandwiches = int(input("how many sandwiches will you be ordering?   "))
        if numOfSandwiches < 0:
            sandwich = "none"
            order.append({sandwich})
            orderInformation += f"sandwich {count}:\t{sandwich}\n"
        while numOfSandwiches != 0:
            sandwich = input("what sandwich would you like: (c)hicken $5.25, (b)eef $6.25, or (t)ofu $5.75?      ")
            while sandwich not in sandwichType:
                sandwich = input("not a valid option, try again . . . would you like: (c)hicken $5.25, (b)eef $6.25, or (t)ofu $5.75?      ")
            if sandwich == "c" or sandwich == "C":
                sandwich = "chicken"
                subtotal += 5.25
                numOfSandwiches -= 1
                order.append(sandwich)
                orderInformation += f"sandwich {count}:\t{sandwich}\n"
                count +=1
            elif sandwich == "b" or sandwich == "B":
                sandwich = "beef"
                subtotal += 6.25
                numOfSandwiches -= 1
                order.append(sandwich)
                orderInformation += f"sandwich {count}:\t{sandwich}\n"
                count +=1
            elif sandwich == "t" or sandwich == "T":
                sandwich = "tofu"
                subtotal += 5.75
                numOfSandwiches -= 1
                order.append(sandwich)
                orderInformation += f"sandwich {count}:\t{sandwich}\n"
                count +=1                
    else:
        sandwich = "none"
        order.append({sandwich})
        orderInformation += f"sandwich {count}:\t{sandwich}\n"
                
#fries
count = 1
answer = input("would you like fries? y/n      ")
while answer not in answers:
    answer = input("not valid answer, try again . . .    ")
if answer in answers:
    if answer == "y" or answer == "Y":
        numOfFries = int(input("how many orders of fries would you like?   "))
        if numOfFries < 0:
            fries = "none"
            order.append({fries})
            orderInformation += f"fries {count}:\t{fries}\n"
        while numOfFries != 0:
                fries = input("what size fries would you like: (s)mall, (m)edium, or (l)arge?      ")
                if fries not in sizeOptions:
                    fries = input("not a valid option, try again . . . what size fries would you like: (s)mall, (m)edium, or (l)arge?      ")
                if fries == "s" or fries == "S":
                    answer = input("would you like to super-size those for $1 more? y/n      ")
                    while answer not in answers:
                        answer = input("not valid answer, try again . . .    ")
                    if answer == "y" or answer == "Y":
                        fries = "large"
                        numOfFries -=1
                        subtotal += 2.00
                        order.append(fries)
                        orderInformation += f"fries {count}:\t{fries}\n"
                        count +=1
                    else:
                        fries = "small"
                        numOfFries -=1
                        subtotal += 1.00
                        order.append(fries)
                        orderInformation += f"fries {count}:\t{fries}\n"
                        count +=1
                elif fries == "m" or fries == "M":
                    fries = "medium"
                    numOfFries -=1
                    subtotal += 1.75
                    order.append(fries)
                    orderInformation += f"fries {count}:\t{fries}\n"
                    count +=1
                elif fries == "l" or fries == "L":
                    fries = "large"
                    numOfFries -= 1
                    subtotal += 2.00
                    order.append(fries)
                    orderInformation += f"fries {count}:\t{fries}\n"
                    count +=1                
    else:
        fries = "none"
        order.append({fries})
        orderInformation += f"fries {count}:\t{fries}\n"

#drinks
count = 1
answer = input("would you like a drink? y/n      ")
while answer not in answers:
    answer = input("not valid answer, try again . . .    ")
if answer in answers:
    if answer == "y" or answer == "Y":
        numOfDrinks = int(input("how many orders of drinks will you be ordering?   "))
        if numOfDrinks < 0:
            drink = "none"
            order.append({drink})
            orderInformation += f"drink {count}:\t{drink}\n"
        while numOfDrinks != 0:
                drink = input("what size drink would you like: (s)mall, (m)edium, or (l)arge?      ")
                if drink not in sizeOptions:
                    drink = input("not a valid option, try again . . . what size drink would you like: (s)mall, (m)edium, or (l)arge?      ")
                if drink == "s" or drink == "S":
                    drink = "small"
                    numOfDrinks -=1
                    subtotal += 1.00
                    order.append(drink)
                    orderInformation += f"drink {count}:\t{drink}\n"
                    count +=1
                elif drink == "m" or drink == "M":
                    drink = "medium"
                    numOfDrinks -=1
                    subtotal += 1.75
                    order.append(drink)
                    orderInformation += f"drink {count}:\t{drink}\n"
                    count +=1
                elif drink == "l" or drink == "L":
                    answer = input("would you like to child-size that for $.38 more? y/n     ")
                    while answer not in answers:
                        answer = input("not valid answer, try again . . .    ")
                    if answer == "y" or answer == "Y":
                        drink = "child-size"
                        numOfDrinks -=1
                        subtotal += (2.25 +0.38)
                        order.append(drink)
                        orderInformation += f"drink {count}:\t{drink}\n"
                        count +=1
                    else:
                        drink = "large"
                        numOfDrinks -= 1
                        subtotal += 2.00
                        order.append(drink)
                        orderInformation += f"drink {count}:\t{drink}\n"
                        count +=1                
    else:
        drink = "none"
        order.append({drink})
        orderInformation += f"drink {count}:\t{drink}\n"

#ketchup
answer = input("would you like ketchup with that? y/n    ")
while answer not in answers:
    answer = input("not valid answer, try again . . .    ")
if answer == "y" or answer == "Y":
    ketchup = int(input("how many packets of ketchup would you like? $.25 per packet     "))
    while ketchup < 0:
        ketchup = int(input("please choose a positive number . . .   "))
    if ketchup > 0:
        subtotal += (ketchup * .25)
else:
    ketchup = "none"
if ketchup != "none":
    orderInformation += f"ketchup:\t{ketchup}\n"
order.append(f"ketchup:\t{ketchup}\n")

#checkout
#discount


print(orderInformation)

subtotal = round(subtotal,2)
print(subtotal)

tax = round((subtotal * 0.07),2)
print(tax)

total = round((subtotal + tax),2)
print(total)