x = True 
y = False
print (x)
def truthy(x,y):
    if type(x) != bool or type(y) != bool:
        print("Glitch!!!")
    else:
        if x == y:
            Print("False")
        elif x != y:
            Print("True")
truthy(x,y)
