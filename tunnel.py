traffic = (input("Are the cars driving west or east"))
EastTraffic = True or False
WestTraffic = True or False
if traffic == "east":
    EastTraffic = True and print("There is traffic from the east and no traffic from the west")
elif traffic == "west":
    WestTraffic = True and print("There is traffic from the west and no traffic from the east")
