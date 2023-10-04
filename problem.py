x= bool(input("Do you have a soccer ball? True or False"))
y = bool(input("Do you play soccer? True or False"))
output1 = ("You play soccer")
output2 = ("You don't play soccer")
output3 = ("You have a soccer ball")
output4 = ("You are broke")
if x == True and y == True:
    print(output1)
elif  x == False and y == False:
    print(output2)
elif x == True and y == False:
    print(output3)