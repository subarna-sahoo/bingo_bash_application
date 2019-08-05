
from random import randint
import random
import time                 #for use of time.sleep


ltr = ['lis1', 'lis2', 'lis3', 'lis4', 'lis5']
for draw in range(1000):    
    drawn_numbers=list()
    bingo_draw=randint(1,90)
    
    if not bingo_draw in drawn_numbers:
        #print((random.choice(ltr)),'-',(bingo_draw))
        #print(bingo_draw)
        #print('\n')
        
        drawn_numbers.append(bingo_draw)
        time.sleep(0.5)     #import time

        
Bingo=8
Glis=[0,0,0,0,0]                                     #for selection comparison
def Rand(start=1, end=70, num=5):
    lis = ['B','I','N','G','O']
    lis1 = []
    lis2 = []
    lis3 = []
    lis4 = []
    lis5 = []
  
    for j in range(num): 
        lis1.append(random.randint(start, end))
        lis2.append(random.randint(start, end))
        lis3.append(random.randint(start, end))
        lis4.append(random.randint(start, end))
        lis5.append(random.randint(start, end))
        
    print('Your Card: \n')
    print(lis,'\n',lis1,'\n',lis2,'\n',lis3,'\n',lis4,'\n',lis5)
    
    Bli = [lis1[0],lis2[0],lis3[0],lis4[0],lis5[0]]
    Ili = [lis1[1],lis2[1],lis3[1],lis4[1],lis5[1]]
    Nli = [lis1[2],lis2[2],lis3[2],lis4[2],lis5[2]]
    Gli = [lis1[3],lis2[3],lis3[3],lis4[3],lis5[3]]
    Oli = [lis1[4],lis2[4],lis3[4],lis4[4],lis5[4]]
    
    print('\n\nprinting vertical list: \n')
    print(Bli)
    print(Ili)
    print(Nli)
    print(Gli)
    print(Oli)
    

    if Bli == Glis:
        B=Bingo-1
        print('\n\n',B,'Bingos left."if"')
        
    else:
        B=Bingo
        print('\n\n',B,'Bingos left."else"')

Rand()
