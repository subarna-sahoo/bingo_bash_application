import time
import random
from random import randint
from prettytable import PrettyTable


CardData=[]
bingo = 4
count={} #Not to repeat any bingo evaluation #Also for check score.

def decBingo(player):
    global bingo
    bingo -= 1
    print('''\n|>Player  {}  Got A BINGO \n|>Bingo left {}'''.format(player,bingo))
    if bingo == 0:
        return True
    while True:
        break
class Card:
    def __init__(self):
        self.CardData = {}
    def GetCards(self,PlayerData):
        for player in PlayerData:
            print("\n|>",player,"Chosed [",PlayerData[player],"] Cards:\n")
            self.CardData[player] = [] #assigning keys as PlayerName with empty list
            NoOfCard = PlayerData[player]
            for Card in range(NoOfCard):
                PL=[] #just a demo list
                while len(PL) != 5:
                    element=randint(1,15)
                    if not element in PL:
                            PL.append(element)
                while len(PL) != 10:
                    element=randint(16,30)
                    if not element in PL:
                            PL.append(element)
                while len(PL) != 15:
                    element=randint(31,45)
                    if not element in PL:
                            PL.append(element)
                while len(PL) != 20:
                    element=randint(46,60)
                    if not element in PL:
                            PL.append(element)
                while len(PL) != 25:
                    element=randint(61,75)
                    if not element in PL:
                            PL.append(element)
                            
                self.CardData[player].append(PL)#adding all P.name with Cards as a list
                # This loop Prints the Card As Output
                for i in PL:
                    print(i, end=" ")
                    if (((PL.index(i))+1)%5==0):
                        print()
                print()
        return self.CardData
    def ShowCard(self,d,player,card):
        Title = ("""Name: {}, Card NO ( {} )""".format(player,card))
        x = PrettyTable()
        x.title = Title
        x.field_names = ["B", "I", "N", "G", "O"]
        x.add_row([d[player][card][0],d[player][card][1],d[player][card][2],d[player][card][3],d[player][card][4]])
        x.add_row([d[player][card][5],d[player][card][6],d[player][card][7],d[player][card][8],d[player][card][9]])
        x.add_row([d[player][card][10],d[player][card][11],d[player][card][12],d[player][card][13],d[player][card][14]])
        x.add_row([d[player][card][15],d[player][card][16],d[player][card][17],d[player][card][18],d[player][card][19]])
        x.add_row([d[player][card][20],d[player][card][21],d[player][card][22],d[player][card][23],d[player][card][24]])
        print(x,'\n\n')
          
    def EvaluateCard(self,element):
        print('____________________________\n\n')
        print('|>>>>                        GAME CALL: (',element,')\n')#Finall Printing that Element here @Game<<
        time.sleep(0)
        for d in CardData:  #In 'd' we have the actual DATA 
            for player in d:
                for card in range(len(d[player])):  #will Check all cards of every player for selection as (0)
                    try:
                        if element in d[player][card]:
                            ind = d[player][card].index(element)
                            d[player][card][ind]=0
                            Card().ShowCard(d,player,card)
                            #==========                                                     
                            H1=[d[player][card][0],d[player][card][1],d[player][card][2],d[player][card][3],d[player][card][4]]
                            H2=[d[player][card][5],d[player][card][6],d[player][card][7],d[player][card][8],d[player][card][9]]
                            H3=[d[player][card][10],d[player][card][11],d[player][card][12],d[player][card][13],d[player][card][14]]
                            H4=[d[player][card][15],d[player][card][16],d[player][card][17],d[player][card][18],d[player][card][19]]
                            H5=[d[player][card][20],d[player][card][21],d[player][card][22],d[player][card][23],d[player][card][24]]
                            #==========
                            V1=[d[player][card][0],d[player][card][5],d[player][card][10],d[player][card][15],d[player][card][20]]
                            V2=[d[player][card][1],d[player][card][6],d[player][card][11],d[player][card][16],d[player][card][21]]
                            V3=[d[player][card][2],d[player][card][7],d[player][card][12],d[player][card][17],d[player][card][22]]
                            V4=[d[player][card][3],d[player][card][8],d[player][card][13],d[player][card][18],d[player][card][23]]
                            V5=[d[player][card][4],d[player][card][9],d[player][card][14],d[player][card][19],d[player][card][24]]
                            #==========
                            D1=[d[player][card][0],d[player][card][6],d[player][card][12],d[player][card][18],d[player][card][24]]
                            D2=[d[player][card][4],d[player][card][8],d[player][card][12],d[player][card][16],d[player][card][20]]
                            #==========
                            #Horizontal ::
                            if (H1==[0,0,0,0,0] and count[player][card][0]==0 and bingo>0 ):
                                count[player][card][0] = 1  #H1
                                count[player][card][12] +=1  # +Score
                               
                                decBingo(player)
                            elif (H2==[0,0,0,0,0] and count[player][card][1]==0 and bingo>0 ):
                                count[player][card][1] = 1 #H2
                                count[player][card][12] +=1  # +Score
                              
                                decBingo(player)
                            elif (H3==[0,0,0,0,0] and count[player][card][2]==0 and bingo>0 ):
                                count[player][card][2] = 1 #H3
                                count[player][card][12] +=1  # +Score
                           
                                decBingo(player)
                            elif (H1==[0,0,0,0,0] and count[player][card][3]==0 and bingo>0 ):
                                count[player][card][3] = 1 #H4
                                count[player][card][12] +=1  # +Score
                                
                                decBingo(player)
                            elif (H1==[0,0,0,0,0] and count[player][card][4]==0 and bingo>0 ):
                                count[player][card][4] = 1 #H5
                                count[player][card][12] +=1  # +Score
                                
                                decBingo(player)
                            #Vertical ::
                            elif (H1==[0,0,0,0,0] and count[player][card][5]==0 and bingo>0 ):
                                count[player][card][5] = 1 #V1
                                count[player][card][12] +=1  # +Score
                                
                                decBingo(player)
                            elif (H1==[0,0,0,0,0] and count[player][card][6]==0 and bingo>0 ):
                                count[player][card][6] = 1 #V2
                                count[player][card][12] +=1  # +Score
                                
                                decBingo(player)
                            elif (H1==[0,0,0,0,0] and count[player][card][7]==0 and bingo>0 ):
                                count[player][card][7] = 1 #V3
                                count[player][card][12] +=1  # +Score
                                
                                decBingo(player)
                            elif (H1==[0,0,0,0,0] and count[player][card][8]==0 and bingo>0 ):
                                count[player][card][8] = 1 #V4
                                count[player][card][12] +=1  # +Score
                             
                            elif (H1==[0,0,0,0,0] and count[player][card][9]==0 and bingo>0 ):
                                count[player][card][9] = 1 #V5
                                count[player][card][12] +=1  # +Score
                              
                                decBingo(player)
                            #Diagonal ::
                            elif  (H1==[0,0,0,0,0] and count[player][card][10]==0 and bingo>0 ):
                                count[player][card][10] = 1 #D1
                                count[player][card][12] +=1  # +Score
                               
                                decBingo(player)
                            elif  (H1==[0,0,0,0,0] and count[player][card][11]==0 and bingo>0 ):
                                count[player][card][11] = 1 #D2
                                count[player][card][12] +=1  # +Score
                                
                                decBingo(player)
                            else:
                                Card().ShowCard(d,player,card)
                                pass
                    except ValueError:
                        pass
                    
class Game:
    def __init__(self):
        called_element = []
        while bingo>0:
            element=(random.randint(1,75))
            if not element in called_element:
                called_element.append(element)
                okay = Player()
                okay.PassElement(element)#passing the element to Player 
            elif len(called_element)==75:
                print('\n|  E n d - G A M E  |')
                break
        print('\n|> B I N G O - L E F T : ',bingo,' ')
        print('\n|  E n d - G A M E  |')

        
class Player(Card):
    def PlayerData(self):
        PlayerData = {}
        PlayerNo=int(input('how many player: '))
        print('\nEnter Names of',PlayerNo,'Player: ')
        for player in range(PlayerNo):
            while len(PlayerData) != PlayerNo :
                Name = input('\n Player Name: ')
                if not Name in PlayerData:
                   PlayerData[Name] = random.randint(1,4)#Random Cards.
                else:
                    print('\n A player with same name already exist. !! \n')
        print('')#Finished User Input.
        for Pname in PlayerData:
            count[Pname]=[]
            for cards in range(PlayerData[Pname]):
                count[Pname].append([0,0,0,0,0, 0,0,0,0,0, 0,0,0])
                # [ H1,H2,H3,H4,H5, V1,V2,V3,V4,V5, D1,D2, @SCORE ]
        input('\nPress ENTER to Continue >>\n')
        #instansiating Card 
        callCard = Card()
        CardData.append(callCard.GetCards(PlayerData)) #Cards of all Player's
        input('\nPress ENTER to START The  G.A.M.E  >>\n')
        #instansiating Game 
        callGame = Game()
    def PassElement(self,element):
        Card().EvaluateCard(element)#passing the element to Card
start= Player()
start.PlayerData()
