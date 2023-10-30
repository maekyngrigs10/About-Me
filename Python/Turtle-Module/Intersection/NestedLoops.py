# this class version works as well
# x = 0

# for i in range(10):
#     for j in range(x,x+10):
#         print(j,end=" ")
#     x +=10
#     print()
# end of class version


for row in range(10):
    for col in range(10):
        print(f"{row}{col}",end=" ")
    print()


# this way also works
# out = ""

# print()

# for i in range(100):
#     out += str(i)
    
# print(out)
    