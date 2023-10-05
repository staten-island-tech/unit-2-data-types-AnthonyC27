x= bool(input("Do you have a soccer ball? Yes or No, Do not type anything for No"))
y = bool(input("Do you play soccer? Yes or No, Do not type anything for No"))
output1 = ("You play soccer")
output2 = ("You don't play soccer")
output3 = ("You have a soccer ball")
output4 = ("You are broke")
if (x,y)==(True,False):
    print(output1)
elif (x,y) == (False,False):
    print(output2)
elif (x,y)==(True,False):
    print(output3)
elif (x,y)==(False,True):
    print(output4)