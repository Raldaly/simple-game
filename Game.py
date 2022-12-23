import random
import time

equipment = {}
quit = 0
HowMuchGold = 0
InWalletTotal = []
Rounds = 1

def WhichChest():
    Chests = ["green", "orange", "purple", "golden"]
    WhichChest = random.choices(Chests, [75, 20, 4, 1], k = 100)
    print("You found the", WhichChest[0], "chest, congratulations!")
    print()

    if WhichChest[0] == "green":
        HowMuchGold = random.randint(801,1201)
        print("You open it and...", HowMuchGold, "gold!")
        InWalletTotal.append(HowMuchGold)

    elif WhichChest[0] == "orange":
        HowMuchGold = random.randint(3601,4401)
        print("You open it and...", HowMuchGold, "gold!")
        InWalletTotal.append(HowMuchGold)

    elif WhichChest[0] == "purple":
        HowMuchGold = random.randint(8201,9801)
        print("You open it and...", HowMuchGold, "gold!")
        InWalletTotal.append(HowMuchGold)

    else:
        HowMuchGold = random.randint(10901,14101)
        print("You open legendary chest and...", HowMuchGold, "gold!")
        InWalletTotal.append(HowMuchGold)

def IsChest():
    Random = ['is', "is no"]
    IsThere = random.choices(Random, [40, 60], k = 100)
    print()
    if IsThere[0][-1] == 's':
        print("There ", IsThere[0],"a chest!")
        print()
        WhichChest()
        print()
    else:
        print()
        print("Empty room!")


print('Welcome to the game!')
print()
print()

while quit == 0:
    print("Would you like to go to the shop?")
    decision = input("Type yes or no: ")
    
    """ sklep """

    if decision.capitalize() == "Yes":
        print()

        """ Ekwipunek """

        print("Would you like to see your equipment?")
        Eq = input("Type 1 if you do: ")

        if Eq == "1":
            print("Your equipmnet: ")
            print()
            for values in equipment.values():
                print(values)
            print()
            continue

    """" Kupowanie """

        else:
            print("Welcome traveler! What you need?")
            print("1 - Health potion (2000 gold)")
            secondDecision = input()
            if secondDecision == "1":

                if sum(InWalletTotal) >= 1500:
                    InWalletTotal.append(-1500)
                    print("Don't forget to drink it!")
                    print()
                    print("You have ", sum(InWalletTotal),"gold in your wallet.")
                    equipment.update({"1" : "Health Potion"})
                    print()
                    continue

            elif sum(InWalletTotal) <= 1500:
                    print()
                    print("But you don't have enough gold!")
                    continue

            else:
                print()
                print("I don't understand, could you repeat?")
                print()
                continue

    if decision.capitalize() == "No":
        Rounds = 0
        while Rounds <= 5:
            print()
            print(Rounds, "room...")
            IsChest()
            print()
            print("You have ", sum(InWalletTotal), "gold in your wallet.")
            Rounds += 1
            time.sleep(2.65)
            print()
            print()
            print()
            print()
            print()
            print()
    elif decision.capitalize() != "No" or decision.capitalize() != "Yes":
        print()
        print("Goodbye then!")
        quit += 1
            



