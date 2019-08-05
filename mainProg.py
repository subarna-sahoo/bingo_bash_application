import random

import time                 #for use of time.sleep

Glis=[0,0,0,0,0]

def Rand(start=10, end=35, num=5):
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
    B = [lis1[0],lis2[0],lis3[0],lis4[0],lis5[0]]
    I = [lis1[1],lis2[1],lis3[1],lis4[1],lis5[1]]
    N = [lis1[2],lis2[2],lis3[2],lis4[2],lis5[2]]
    G = [lis1[3],lis2[3],lis3[3],lis4[3],lis5[3]]
    O = [lis1[4],lis2[4],lis3[4],lis4[4],lis5[4]]
    print('Your Card: \n')
    def check_card():
        card = '''                 B   I   N   G   O
                 {}  {}  {}  {}  {}
                 {}  {}  {}  {}  {}
                 {}  {}  {}  {}  {}
                 {}  {}  {}  {}  {}
                 {}  {}  {}  {}  {}
                '''
        print (card.format(lis1[0],lis1[1],lis1[2],lis1[3],lis1[4],
                           lis2[0],lis2[1],lis2[2],lis2[3],lis2[4],
                           lis3[0],lis3[1],lis3[2],lis3[3],lis3[4],
                           lis4[0],lis4[1],lis4[2],lis4[3],lis4[4],
                           lis5[0],lis5[1],lis5[2],lis5[3],lis5[4]))
    check_card()
    bingo = int(input('Enter Bingos: '))    #you can take it randomly,as player's
    while bingo > 0:
        print(bingo,'Bingos left.')
        bingo -= 1                          # This is the same as count = bingo + 1
        #-----------
        ltr = ['B', 'I', 'N', 'G', 'O']
        for draw in range(5):    
            drawn_numbers=list()
            bingo_draw=random.randint(10,35)
            if not bingo_draw in drawn_numbers:
                print((random.choice(ltr)),',',(bingo_draw))
                print('\n')
                drawn_numbers.append(bingo_draw)
                time.sleep(1.5)                     #import time
                check_card()

        #-----------    

# Game Index
def main_menu():
    print('''
           <<  Wllcome to Bingo Python >>
           
               < A > For New Game.     
           
               < B > For Check Score.
           ''')
    inp=input(':')
    if (inp=='A'):
        Rand()
    elif (inp=='B'):
        print('No New Scores Yet')
    else:
        print('wrong input')
main_menu()
