total = 0
orderInformation = ""
finalTotal = 0

#sandwich
sandwich = input("would you like a sandwich? y/n    ")
if sandwich == "y":
    sandwich = input("what sandwich would you like: (c)hicken $5.25, (b)eef $6.25, or (t)ofu $5.75?      ")
    if sandwich == "c":
        sandwich = "chicken"
        total += 5.25
    elif sandwich == "b":
        sandwich = "beef"
        total+= 6.25
    elif sandwich == "t":
        sandwich = "tofu"
        total += 5.75
else:
    sandwich = "none"
if sandwich != "none":
    orderInformation += f"sandwich:\t{sandwich}\n"

#fries
fries = input("would you like fries? y/n    ")
if fries == "y":
    fries = input("what size fries would you like: (s)mall, (m)edium, or (l)arge?      ")
    if fries == "s":
        fries = input("would you like to mega size those for $1 more? y/n     ")
        if fries == "y":
            fries = "large"
            total += 2.00
        else:
            total += 1.00
    elif fries == "m":
        sandwich = "medium"
        total+= 1.50
    elif sandwich == "l":
        sandwich = "large"
        total += 2.00
else: 
    fries = "none"
if fries != "none":
    orderInformation += f"fries:\t{fries}\n"

#drinks
drink = input("would you like a drink? y/n    ")
if drink == "y":
    drink = input("what size drink would you like: (s)mall $1.00, (m)edium $1.75, or (l)arge $2.25?      ")
    if drink == "s":
        drink = "small"
        total += 1.00
    elif drink == "m":
        drink = "medium"
        total+= 1.75
    elif drink == "l":
        drink = input("would you like to upgrade to a child size drink for $.38 more? y/n      ")
        if drink == "y":
            drink = "child-size"
            total += (2.25 + 0.38)
        else:
            drink = "large"
            total += 2.25
else:
    drink = "none"
if drink != "none":
    orderInformation += f"drink:\t{drink}\n"

#ketchup packets
ketchup = input("would you like ketchup with that? y/n    ")
if ketchup == "y":
    ketchup = int(input("how many packets of ketchup would you like? $.25 per packet     "))
    total += ketchup * 0.25
else:
    ketchup = "none"
if ketchup != "none":
    orderInformation += f"ketchup:\t{ketchup}\n"

#discount
discount = 0
if  sandwich and drink and fries != "none":
    total -= 1.00
    discount = 1.00

#checkout
total = round(total,2)
tax = round(total * 0.07,2)
finalTotal = round(tax + total,2)
print(orderInformation)
print(f"discount: -{discount}")
print(f"subtotal: {total}\n")
print(f"tax: {tax}\n")
print(f"Total: {finalTotal}\n")
