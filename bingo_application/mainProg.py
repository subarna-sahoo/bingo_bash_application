import random
import time

select_li=[0,0,0,0,0]
def Rand(start=10, end=35, num=5):
    B = []
    I = []
    N = []
    G = []
    O = []
    for j in range(num):
        B.append(random.randint(start, end))
        I.append(random.randint(start, end))
        N.append(random.randint(start, end))
        G.append(random.randint(start, end))
        O.append(random.randint(start, end))
    V1=[B[0],I[0],N[0],G[0],O[0]]
    V2=[B[1],I[1],N[1],G[1],O[1]]
    V3=[B[2],I[2],N[2],G[2],O[2]]
    V4=[B[3],I[3],N[3],G[3],O[3]]
    V5=[B[4],I[4],N[4],G[4],O[4]]

    def check_card():
        card = '''
               B - {}  {}  {}  {}  {}
               
               I - {}  {}  {}  {}  {}
               
               N - {}  {}  {}  {}  {}
               
               G - {}  {}  {}  {}  {}
               
               O - {}  {}  {}  {}  {}
                '''
        print (card.format(B[0],B[1],B[2],B[3],B[4],
                           I[0],I[1],I[2],I[3],I[4],
                           N[0],N[1],N[2],N[3],N[4],
                           G[0],G[1],G[2],G[3],G[4],
                           O[0],O[1],O[2],O[3],O[4]))

    print('Your Card: \n')
    check_card()
    bingo = 3#int(input('Enter Bingos: '))
    while bingo > 0:
        try:
            list_names = ['B', 'I', 'N', 'G', 'O']      
            for draw in range(500):    
                random_name =(random.choice(list_names))   
                element=(random.randint(10,35))  
                print(random_name,element)
                time.sleep(0.5)
                print('\n')
                if random_name == 'B':
                    index_value = B.index(element)
                    B[index_value] = 0
                    check_card()
                elif random_name=='I':
                    index_value = I.index(element)
                    I[index_value] = 0
                    check_card()
                elif random_name=='N':
                    index_value = N.index(element)
                    N[index_value] = 0
                    check_card()
                elif random_name=='G': 
                    index_value = G.index(element)
                    G[index_value] = 0
                    check_card()
                elif random_name=='O':
                    index_value = O.index(element)
                    O[index_value] = 0
                    check_card()
                else:
                    print('no value')
                #   remove bingo
                if  select_li == B:
                    bingo -=1
                    print("bingoleft",bingo)
                    check_card()
                    time.sleep(5)
                
                elif  select_li == I:
                    bingo -=1
                    print("bingoleft",bingo)
                    check_card()
                    time.sleep(5)
                    
                elif  select_li == N:
                    bingo -=1
                    print("bingoleft",bingo)
                    check_card()
                    time.sleep(5)
                    
                elif  select_li == G:
                    bingo -=1
                    print("bingoleft",bingo)
                    check_card()
                    time.sleep(5)
                    
                elif  select_li == O:
                    bingo -=1
                    print("bingoleft",bingo)
                    check_card()
                    time.sleep(5)
                #
                elif  select_li == V1:
                    check_card()
                    bingo -=1
                    print("bingoleft",bingo)
                    time.sleep(5)
                    
                elif  select_li == V2:
                    check_card()
                    bingo -=1
                    print("bingoleft",bingo)
                    time.sleep(5)
                    
                elif  select_li == V3:
                    check_card()
                    bingo -=1
                    print("bingoleft",bingo)
                    time.sleep(5)
                    
                elif  select_li == V4:
                    check_card()
                    bingo -=1
                    print("bingoleft",bingo)
                    time.sleep(5)
                    
                elif  select_li == V5:
                    check_card()
                    bingo -=1
                    print("bingoleft",bingo)
                    time.sleep(5)
                    
                else:
                    pass
                #
        
                time.sleep(1)
            
        except ValueError:
            pass
        
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
        print('        No New Scores Yet ("_")\n\n         LETS MAKE ONE  >>')
        main_menu()
    else:
        print('  !!!!!!!!!!!        Wrong input       !!!!!!!!!!!!    ')
        main_menu()
main_menu()
