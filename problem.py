x= bool(input("Do you have a soccer ball? Yes or No"))
y = bool(input("Do you play soccer? Yes or No"))
output1 = ("You play soccer")
output2 = ("You don't play soccer")
output3 = ("You have a soccer ball")
if x == True & y == True:
    print(output1)
if x == True & y == False:
    print(output3)