from random import randint
import random
import time



comp_li=[0,0,0,0,0]
player_names=[]
#CARD
def Card(start=10, end=20, num=12):
    B = []
    I = []
    N = []
    G = []
    O = []
    #Horizental
    for draw in range(num):
        if len(B) != 5:
            element=randint(start,end)
            if not element in B:
                B.append(element)
    for draw in range(num):
        if len(I) != 5:
            element=randint(start,end)
            if not element in I:
                I.append(element)
    for draw in range(num):
        if len(N) != 5:
            element=randint(start,end)
            if not element in N:
                N.append(element)
    for draw in range(num):
        if len(G) != 5:
            element=randint(start,end)
            if not element in G:
                G.append(element)
    for draw in range(num):
        if len(O) != 5:
            element=randint(start,end)
            if not element in O:
                O.append(element)
    #CHECK CARD
    def Check_Card():
        card = '''
               B - {}  {}  {}  {}  {}
               
               I - {}  {}  {}  {}  {}
               
               N - {}  {}  {}  {}  {}
               
               G - {}  {}  {}  {}  {}
               
               O - {}  {}  {}  {}  {}
                '''
        try:
            print (card.format(B[0],B[1],B[2],B[3],B[4],
                               I[0],I[1],I[2],I[3],I[4],
                               N[0],N[1],N[2],N[3],N[4],
                               G[0],G[1],G[2],G[3],G[4],
                               O[0],O[1],O[2],O[3],O[4]))
        except (ValueError, IndexError):
            pass
    
    print('Your Card: \n')
    Check_Card()
    
    input('PRESS ENTER TO START THE GAME.\n')
    bingo = 3#int(input('Enter Bingos: '))

    #for one time exicution of rows/column/diagonal
    count_B = 0
    count_I = 0
    count_N = 0
    count_G = 0
    count_O = 0
    count_V1 = 0
    count_V2 = 0
    count_V3 = 0
    count_V4 = 0
    count_V5 = 0
    count_D1 = 0
    count_D2 = 0
    #GLOBAL CALL
    global_call =[]
    while bingo > 0:
        try:
            list_names = ['B', 'I', 'N', 'G', 'O']      
            for draw in range(200):    
                random_name =(random.choice(list_names))   
                element=(random.randint(10,30))
                call = random_name,element
                if not call in global_call:
                    if bingo>0:
                        print(call)
                        global_call.append(call)
                    else:
                        pass
                else:
                    pass
                time.sleep(0.5)
                print('\n')

                #----------------------------
                V1=[B[0],I[0],N[0],G[0],O[0]]
                V2=[B[1],I[1],N[1],G[1],O[1]]
                V3=[B[2],I[2],N[2],G[2],O[2]]
                V4=[B[3],I[3],N[3],G[3],O[3]]
                V5=[B[4],I[4],N[4],G[4],O[4]]

                #----------------------------
                D1=[B[0],I[1],N[2],G[3],O[4]]
                D2=[B[4],I[3],N[2],G[1],O[0]]

                #----------------------------
                if random_name == 'B':
                    index_value = B.index(element)
                    B[index_value] = 0
                    print ('after changed by machine : ')
                    Check_Card()
                elif random_name=='I':
                    index_value = I.index(element)
                    I[index_value] = 0
                    print ('after changed by machine : ')
                    Check_Card()
                elif random_name=='N':
                    index_value = N.index(element)
                    N[index_value] = 0
                    print ('after changed by machine : ')
                    Check_Card()
                elif random_name=='G': 
                    index_value = G.index(element)
                    G[index_value] = 0
                    print ('after changed by machine : ')
                    Check_Card()
                elif random_name=='O':
                    index_value = O.index(element)
                    O[index_value] = 0
                    print ('after changed by machine : ')
                    Check_Card()
                else:
                    print('End Game.')
                    
                # Remove Bingo !!
                # Horizontal >>
                if  (bingo > 0 and count_B==0 and comp_li == B):
                    bingo -=1
                    count_B += 1
                    print("bingoleft",bingo)
                    Check_Card()
                    time.sleep(2)
                
                elif  (bingo > 0 and count_I==0 and comp_li == I):
                    bingo -=1
                    count_I += 1
                    print("bingoleft",bingo)
                    Check_Card()
                    time.sleep(2)
                    
                elif  (bingo > 0 and count_N==0 and comp_li == N):
                    bingo -=1
                    count_N += 1
                    print("bingoleft",bingo)
                    Check_Card()
                    time.sleep(2)
                    
                elif  (bingo > 0 and count_G==0 and comp_li == G):
                    bingo -=1
                    count_G += 1
                    print("bingoleft",bingo)
                    Check_Card()
                    time.sleep(2)
                    
                elif  (bingo > 0 and count_O==0 and comp_li == O):
                    bingo -=1
                    count_O += 1
                    print("bingoleft",bingo)
                    Check_Card()
                    time.sleep(2)
                    
                # Vertical >>
                elif  (bingo > 0 and count_V1==0 and comp_li == V1):
                    bingo -=1
                    count_V1 += 1
                    print("bingoleft",bingo)
                    Check_Card()
                    time.sleep(2)
                    
                elif  (bingo > 0 and count_V2==0 and comp_li == V2):
                    bingo -=1
                    count_V2 += 1
                    print("bingoleft",bingo)
                    Check_Card()
                    time.sleep(2)
                    
                elif  (bingo > 0 and count_V3==0 and comp_li == V3):
                    bingo -=1
                    count_V3 += 1
                    print("bingoleft",bingo)
                    Check_Card()
                    time.sleep(2)
                    
                elif  (bingo > 0 and count_V4==0 and comp_li == V4):
                    bingo -=1
                    count_V4 += 1
                    print("bingoleft",bingo)
                    Check_Card()
                    time.sleep(2)
                    
                elif  (bingo > 0 and count_V2==0 and comp_li == V5):
                    bingo -=1
                    count_V2 += 1
                    print("bingoleft",bingo)
                    Check_Card()
                    time.sleep(2)
                    
                # Diagonal >>
                elif  (bingo > 0 and count_D1==0 and comp_li == D1):
                    bingo -=1
                    count_D1 += 1
                    print("bingoleft",bingo)
                    Check_Card()
                    time.sleep(2)

                elif  (bingo > 0 and count_D2==0 and comp_li == D2):
                    bingo -=1
                    count_D2 += 1
                    print("bingoleft",bingo)
                    Check_Card()
                    time.sleep(2)
         
                else:
                    pass
                time.sleep(0)
                
        except ValueError:
            pass

    #====================================================
    print('                 End Game                 ')
    #====================================================



    

# Game Index-------------------------------------------------------------

#==============================SINGLE PLAYER=============================
def single_player():
    player_name = input ("Enter Your Name: ")
    if not player_name in player_names:
        player_names.append(player_name)
        print('New player Added: ',player_name)
        Card()
    else:
        print('''
                 A player with same name already exist.   !!!
                ''')
        single_player()

        
#==============================MULTI PLAYER=============================
def multi_player():
    r=int(input('how many player :'))
    for player in range(r):
        name = input('Player Name: ')
        player_names.append(name)
        print('\n\nNext Player Name:\n ')
    print('You have Entered: ',player_names)
    game=input('\nPress ENTER for Continue.. \n')
    for i in player_names:
        print (i)
        Card()
    sgame=input('Press 2 for Start The Game >')
    startgame()
    

#==============================MAIN MENU================================
def main_menu():
    inp=input('''
 <<<<<<<<<<   Wllcome to Bingo Python  >>>>>>>>>>>>>
           
               < 1 > For New Game.     
           
               < 2 > For Check Score.
           :-''')
    if (inp=='1'):
        in_pl = input('''
                < 1 >  For SIngle Player.
                
                < 2 >  For Multiplayer.
           :-''')
        if (in_pl=='1'):
            single_player()
        elif (in_pl=='2'):
            multi_player()
    elif (inp=='2'):
        print(' \n\n      !!!!        No New Scores Yet ("_")       !!!!\n\n                  LETS MAKE ONE  >>\n\n')
        main_menu()
    else:
        print('\n\n  !!!!!!!!!!!        Wrong input       !!!!!!!!!!!!    ')
        main_menu()
        
        
#=============================**==============================

main_menu()
