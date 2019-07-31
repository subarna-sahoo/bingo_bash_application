import random


Size = 5
minNum = 1
maxNum = 50
cards = int(input('Chose Cards [1/2/3/n]: '))

for h in range(cards):
    card = []
    randRange = range(minNum, maxNum)
    card = random.sample(randRange, Size * Size)
    print ("    B  i  n  g  o")
    for i in range(Size):
        string = "    "
        for j in range(Size):
            string +=  str(card[i + j * Size]) + " "
        print (string)
    print("\n")

