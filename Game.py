import random
import time

a = 1

def WhatChest():
    Chests = ["green", "orange", "purple", "golden"]
    WhatChest = random.choices(Chests, [75, 20, 4, 1], k = 100)
    print("You found the", WhatChest[0], "chest, congratulations!")
    print()
    if WhatChest[0] == "green":
        print("You open it and... 1000 gold!")
    elif WhatChest[0] == "orange":
        print("You open it and... 4000 gold!")
    elif WhatChest[0] == "purple":
        print("You open it and... 9000 gold!")
    else:
        print("You open legendary chest and... 12000 gold!")
    

def IsChest():
    Random = ['is', "is no"]
    IsThere = random.choices(Random, [40, 60], k = 100)
    print()
    if IsThere[0][-1] == 's':
        print("There ", IsThere[0],"a chest!")
        print()
        WhatChest()
        print()
    else:
        print()
        print("Empty room!")


print('Welcome to the game!')
print()
print('I think we should start')
print()

while a <= 5:
    print(a, "room...")
    IsChest()
    a += 1
    time.sleep(3.5)
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()





