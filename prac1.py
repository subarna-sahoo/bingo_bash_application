import time
import random
from random import randint

CardData = {}
class Card:
    def __init__(self,PlayerNmae,NoOfCard):
        CardData[PlayerNmae]=[]
        for Card in range(NoOfCard):
            B = []
            I = []
            N = []
            G = []
            O = []
            #Random elements without repetition
            while len(B) != 5:
                element=randint(1,15)
                if not element in B:
                            B.append(element)
            while len(I) != 5:
                element=randint(16,30)
                if not element in I:
                            I.append(element)
            while len(N) != 5:
                element=randint(31,45)
                if not element in N:
                            N.append(element)
            while len(G) != 5:
                element=randint(46,60)
                if not element in G:
                            G.append(element)
            while len(O) != 5:
                element=randint(61,75)
                if not element in O:
                            O.append(element)
            CardData[PlayerNmae].append([B,I,N,G,O])

        #Printing Cards:-
        print('\n>',PlayerNmae,'Chosed',NoOfCard,'Card >\n')
        time.sleep(0.5)
        for showcard in range(len(CardData[PlayerNmae])): 
            for i in range(len(CardData[PlayerNmae][showcard])) :
                for j in range(len(CardData[PlayerNmae][showcard][i])) :  
                    print(CardData[PlayerNmae][showcard][i][j], end=" ")
                print()
            print()   #SAME AS (end='\n')
            time.sleep(0.1)
        time.sleep(0.5)


class Game:
    def __init__(self):
        pass
        
class Player:
    PlayerData = {}
    PlayerNo=int(input('how many player: '))
    print('\nEnter Names of',PlayerNo,'Player: ')
    for player in range(PlayerNo):
        while len(PlayerData) != PlayerNo :
            Name = input('\n Player Name: ')
            if not Name in PlayerData:
               PlayerData[Name] = random.randint(1,4)#selecting cards for 
            else:
                print('\n A player with same name already exist. !! \n')
    print('')
    for PlayerNmae in PlayerData:
        NoOfCard = PlayerData [ PlayerNmae ]
        callCard = Card(PlayerNmae,NoOfCard)
    input('Press ENTER to Continue >>')
    

        
