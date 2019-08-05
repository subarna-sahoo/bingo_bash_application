import random 
from random import randint
#--------------------------------------------


Bingo=5     #you can take in random according to no. of players.
Glis=[0,0,0,0,0]    #for selection of rows/column comparison.

print('You got',Bingo,'Bingos')

for i in range(Bingo):
    def Rand(start=1, end=30, num=5):
        #according to players take the end value. (1/2, player-30)
        lis = ['B','I','N','G','O']
        lis1 = []
        lis2 = []
        lis3 = []
        lis4 = []
        lis5 = []
        for j in range(num):
            #Rows in list: 
            lis1.append(random.randint(start, end))
            lis2.append(random.randint(start, end))
            lis3.append(random.randint(start, end))
            lis4.append(random.randint(start, end))
            lis5.append(random.randint(start, end))    
        print('Your Card: \n')
        print(lis,'\n',lis1,'\n',lis2,'\n',lis3,'\n',lis4,'\n',lis5)
        #Columns in LIST:
        Bli = [lis1[0],lis2[0],lis3[0],lis4[0],lis5[0]]
        Ili = [lis1[1],lis2[1],lis3[1],lis4[1],lis5[1]]
        Nli = [lis1[2],lis2[2],lis3[2],lis4[2],lis5[2]]
        Gli = [lis1[3],lis2[3],lis3[3],lis4[3],lis5[3]]
        Oli = [lis1[4],lis2[4],lis3[4],lis4[4],lis5[4]]
        if Bingo>0:
                #selecting COLUMNS:
                if Glis == Bli:
                    B=Bingo-1
                    print('\n\n',B,'Bingos left.')
                elif Glis == Ili:
                    B=Bingo-1
                    print('\n\n',B,'Bingos left.')
                elif Glis == Nli:
                    B=Bingo-1
                    print('\n\n',B,'Bingos left.')
                elif Glis == Gli:
                    B=Bingo-1
                    print('\n\n',B,'Bingos left.')
                elif Glis == Oli:
                    B=Bingo-1
                    print('\n\n',B,'Bingos left.')
                #selecting ROWS--
                if Glis == lis1:
                    B=Bingo-1
                    print('\n\n',B,'Bingos left.')
                elif Glis == lis2:
                    B=Bingo-1
                    print('\n\n',B,'Bingos left.')
                elif Glis == lis3:
                    B=Bingo-1
                    print('\n\n',B,'Bingos left.')
                elif Glis == lis4:
                    B=Bingo-1
                    print('\n\n',B,'Bingos left.')
                elif Glis == lis5:
                    B=Bingo-1
                    print('\n\n',B,'Bingos left.')
                else:
                    B=Bingo
                    print('\n\n',B,'Bingos left.')
                #selecting DIGONALS--
                    '''
                elif Glis == digonal1:
                    B=Bingo-1
                    print('\n\n',B,'Bingos left.')
                elif Glis == digonal2:
                    B=Bingo-1
                    print('\n\n',B,'Bingos left.')
                    '''
                Bingo = Bingo-1
        else:
                print('END GAME')
    Rand()
