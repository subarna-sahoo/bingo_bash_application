import random
from random import randint
import time


#=================================================================================
#For Global Access
comp_li=[0,0,0,0,0]     # For Compare of Selection of ROW / COLUMN / DIAGONAL 
player_names=[]         # To Check non Duplications of Players
key=[]
v=[]
count={}    #Not to repeat any bingo evaluation #Also for check score.


#==================================================================================
#Every fucn Call will give you a Random Card
def Card(start=10, end=20, num=12):
    B = []
    I = []
    N = []
    G = []
    O = []
    #Random elements without repetition
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
    # Initial Show Card To Players
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
    print('     Your Card: \n')
    Check_Card()
    c={'B':B,'I':I,'N':N,'G':G,'O':O}
    v.append(c)
    
    
#=====================================================================
# Here you Solve the Actual Process
def solve():
    d = dict(zip(key,v))
    for p in d:
        value=[0,0,0,0,0,0,0,0]     #[v1, v2, v3, v4, v5, D1, D2, Score ]
        count[p] = value
    list_names = ['B', 'I', 'N', 'G', 'O']
    bingo = 8           #Given Bingos!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    c_li=[0,0,0,0,0]
    while bingo>0:
        which_list =(random.choice(list_names))   
        element=(random.randint(10,30))
        print(which_list,element)           #Global Call For All Players-


# B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B        
        if which_list =='B':
            for player in d:
                def Check_Card():
                    card = '''
                           B - {}  {}  {}  {}  {}
                           
                           I - {}  {}  {}  {}  {}
                           
                           N - {}  {}  {}  {}  {}
                           
                           G - {}  {}  {}  {}  {}
                           
                           O - {}  {}  {}  {}  {}
                            '''
                    try:
                        print (card.format(d[player]['B'][0],d[player]['B'][1],d[player]['B'][2],d[player]['B'][3],d[player]['B'][4],
                                           d[player]['I'][0],d[player]['I'][1],d[player]['I'][2],d[player]['I'][3],d[player]['I'][4],
                                           d[player]['N'][0],d[player]['N'][1],d[player]['N'][2],d[player]['N'][3],d[player]['N'][4],
                                           d[player]['G'][0],d[player]['G'][1],d[player]['G'][2],d[player]['G'][3],d[player]['G'][4],
                                           d[player]['O'][0],d[player]['O'][1],d[player]['O'][2],d[player]['O'][3],d[player]['O'][4]))
                    except (ValueError, IndexError):
                        pass
                if element in (d[player]['B']):
                    ind=(d[player]['B']).index(element)
                    ((d[player]['B'])[ind])=0
                    #Horizontal :
                    if (d[player]['B']) == c_li :
                        print('\n',player,'  Got a BINGO   !!!!!!!!')
                        Check_Card()
                        bingo -= 1
                        count[player][7] +=1
                        print('     Bingo Left: ',bingo)
                    #VERTICAL :
                    elif [(d[player]['B'][0]),(d[player]['I'][0]),(d[player]['N'][0]),(d[player]['G'][0]),(d[player]['O'][0])] == c_li :
                        if ( bingo>0 and count[player][0] == 0) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][0] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][1]),(d[player]['I'][1]),(d[player]['N'][1]),(d[player]['G'][1]),(d[player]['O'][1])] == c_li :
                        if ( bingo>0 and count[player][1] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][1] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][2]),(d[player]['I'][2]),(d[player]['N'][2]),(d[player]['G'][2]),(d[player]['O'][2])] == c_li :
                        if ( bingo>0 and count[player][2] ) == 0 :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][2] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][3]),(d[player]['I'][3]),(d[player]['N'][3]),(d[player]['G'][3]),(d[player]['O'][3])] == c_li :
                        if ( bingo>0 and count[player][3] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][3] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][4]),(d[player]['I'][4]),(d[player]['N'][4]),(d[player]['G'][4]),(d[player]['O'][4])] == c_li :
                        if ( bingo>0 and count[player][4] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][4] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    #Diagonal:
                    elif [(d[player]['B'][0]),(d[player]['I'][1]),(d[player]['N'][2]),(d[player]['G'][3]),(d[player]['O'][4])] == c_li :
                        if ( bingo>0 and count[player][5] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][5] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][4]),(d[player]['I'][3]),(d[player]['N'][2]),(d[player]['G'][1]),(d[player]['O'][0])] == c_li :
                        if ( bingo>0 and count[player][6] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][6] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                
                
# I I I I I I I I I I I I I I I I I I I I I I I I I I I  I I I I I I I I I I I  I I I I I I I I I    
        if which_list == 'I':
             for player in d:
                def Check_Card():
                    card = '''
                           B - {}  {}  {}  {}  {}
                           
                           I - {}  {}  {}  {}  {}
                           
                           N - {}  {}  {}  {}  {}
                           
                           G - {}  {}  {}  {}  {}
                           
                           O - {}  {}  {}  {}  {}
                            '''
                    try:
                        print (card.format(d[player]['B'][0],d[player]['B'][1],d[player]['B'][2],d[player]['B'][3],d[player]['B'][4],
                                           d[player]['I'][0],d[player]['I'][1],d[player]['I'][2],d[player]['I'][3],d[player]['I'][4],
                                           d[player]['N'][0],d[player]['N'][1],d[player]['N'][2],d[player]['N'][3],d[player]['N'][4],
                                           d[player]['G'][0],d[player]['G'][1],d[player]['G'][2],d[player]['G'][3],d[player]['G'][4],
                                           d[player]['O'][0],d[player]['O'][1],d[player]['O'][2],d[player]['O'][3],d[player]['O'][4]))
                    except (ValueError, IndexError):
                        pass
                if element in (d[player]['I']):
                    ind=(d[player]['I']).index(element)
                    ((d[player]['I'])[ind])=0
                    #Horizontal :
                    if (d[player]['I']) == c_li :
                       print('\n',player,'  Got a BINGO   !!!!!!!!')
                       Check_Card()
                       bingo -= 1
                       count[player][7] +=1
                       print('Bingo Left: ',bingo)
                    #VERTICAL :
                    elif [(d[player]['B'][0]),(d[player]['I'][0]),(d[player]['N'][0]),(d[player]['G'][0]),(d[player]['O'][0])] == c_li :
                        if ( bingo>0 and count[player][0] == 0) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][0] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][1]),(d[player]['I'][1]),(d[player]['N'][1]),(d[player]['G'][1]),(d[player]['O'][1])] == c_li :
                        if ( bingo>0 and count[player][1] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][1] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][2]),(d[player]['I'][2]),(d[player]['N'][2]),(d[player]['G'][2]),(d[player]['O'][2])] == c_li :
                        if ( bingo>0 and count[player][2] ) == 0 :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][2] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][3]),(d[player]['I'][3]),(d[player]['N'][3]),(d[player]['G'][3]),(d[player]['O'][3])] == c_li :
                        if ( bingo>0 and count[player][3] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][3] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][4]),(d[player]['I'][4]),(d[player]['N'][4]),(d[player]['G'][4]),(d[player]['O'][4])] == c_li :
                        if ( bingo>0 and count[player][4] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][4] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    #Diagonal:
                    elif [(d[player]['B'][0]),(d[player]['I'][1]),(d[player]['N'][2]),(d[player]['G'][3]),(d[player]['O'][4])] == c_li :
                        if ( bingo>0 and count[player][5] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][5] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][4]),(d[player]['I'][3]),(d[player]['N'][2]),(d[player]['G'][1]),(d[player]['O'][0])] == c_li :
                        if ( bingo>0 and count[player][6] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][6] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                            

#  N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N                 
        if which_list == 'N':
             for player in d:
                def Check_Card():
                    card = '''
                           B - {}  {}  {}  {}  {}
                           
                           I - {}  {}  {}  {}  {}
                           
                           N - {}  {}  {}  {}  {}
                           
                           G - {}  {}  {}  {}  {}
                           
                           O - {}  {}  {}  {}  {}
                            '''
                    try:
                        print (card.format(d[player]['B'][0],d[player]['B'][1],d[player]['B'][2],d[player]['B'][3],d[player]['B'][4],
                                           d[player]['I'][0],d[player]['I'][1],d[player]['I'][2],d[player]['I'][3],d[player]['I'][4],
                                           d[player]['N'][0],d[player]['N'][1],d[player]['N'][2],d[player]['N'][3],d[player]['N'][4],
                                           d[player]['G'][0],d[player]['G'][1],d[player]['G'][2],d[player]['G'][3],d[player]['G'][4],
                                           d[player]['O'][0],d[player]['O'][1],d[player]['O'][2],d[player]['O'][3],d[player]['O'][4]))
                    except (ValueError, IndexError):
                        pass
                if element in (d[player]['N']):
                    ind=(d[player]['N']).index(element)
                    ((d[player]['N'])[ind])=0
                    #Horizontal :
                    if (d[player]['N']) == c_li :
                       print('\n',player,'  Got a BINGO   !!!!!!!!')
                       Check_Card()
                       bingo -= 1
                       count[player][7] +=1
                       print('Bingo Left: ',bingo)
                    #VERTICAL :
                    elif [(d[player]['B'][0]),(d[player]['I'][0]),(d[player]['N'][0]),(d[player]['G'][0]),(d[player]['O'][0])] == c_li :
                        if ( bingo>0 and count[player][0] == 0) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][0] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][1]),(d[player]['I'][1]),(d[player]['N'][1]),(d[player]['G'][1]),(d[player]['O'][1])] == c_li :
                        if ( bingo>0 and count[player][1] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][1] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][2]),(d[player]['I'][2]),(d[player]['N'][2]),(d[player]['G'][2]),(d[player]['O'][2])] == c_li :
                        if ( bingo>0 and count[player][2] ) == 0 :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][2] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][3]),(d[player]['I'][3]),(d[player]['N'][3]),(d[player]['G'][3]),(d[player]['O'][3])] == c_li :
                        if ( bingo>0 and count[player][3] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][3] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][4]),(d[player]['I'][4]),(d[player]['N'][4]),(d[player]['G'][4]),(d[player]['O'][4])] == c_li :
                        if ( bingo>0 and count[player][4] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][4] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    #Diagonal:
                    elif [(d[player]['B'][0]),(d[player]['I'][1]),(d[player]['N'][2]),(d[player]['G'][3]),(d[player]['O'][4])] == c_li :
                        if ( bingo>0 and count[player][5] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][5] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][4]),(d[player]['I'][3]),(d[player]['N'][2]),(d[player]['G'][1]),(d[player]['O'][0])] == c_li :
                        if ( bingo>0 and count[player][6] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][6] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)


# G G G G G G G G G G G G G G G G G G G G G G G G G  G G G G G G G G G G G G G G G G G G  G G G G G G G G  G G                    
        if which_list == 'G':
             for player in d:
                def Check_Card():
                    card = '''
                           B - {}  {}  {}  {}  {}
                           
                           I - {}  {}  {}  {}  {}
                           
                           N - {}  {}  {}  {}  {}
                           
                           G - {}  {}  {}  {}  {}
                           
                           O - {}  {}  {}  {}  {}
                            '''
                    try:
                        print (card.format(d[player]['B'][0],d[player]['B'][1],d[player]['B'][2],d[player]['B'][3],d[player]['B'][4],
                                           d[player]['I'][0],d[player]['I'][1],d[player]['I'][2],d[player]['I'][3],d[player]['I'][4],
                                           d[player]['N'][0],d[player]['N'][1],d[player]['N'][2],d[player]['N'][3],d[player]['N'][4],
                                           d[player]['G'][0],d[player]['G'][1],d[player]['G'][2],d[player]['G'][3],d[player]['G'][4],
                                           d[player]['O'][0],d[player]['O'][1],d[player]['O'][2],d[player]['O'][3],d[player]['O'][4]))
                    except (ValueError, IndexError):
                        pass
                if element in (d[player]['G']):
                    ind=(d[player]['G']).index(element)
                    ((d[player]['G'])[ind])=0
                    #Horizontal :
                    if (d[player]['G']) == c_li :
                       print('\n',player,'      Got a BINGO   !!!!!!!!')
                       Check_Card()
                       bingo -= 1
                       count[player][7] +=1
                       print('Bingo Left: ',bingo)
                    #VERTICAL :
                    elif [(d[player]['B'][0]),(d[player]['I'][0]),(d[player]['N'][0]),(d[player]['G'][0]),(d[player]['O'][0])] == c_li :
                        if ( bingo>0 and count[player][0] == 0) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][0] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][1]),(d[player]['I'][1]),(d[player]['N'][1]),(d[player]['G'][1]),(d[player]['O'][1])] == c_li :
                        if ( bingo>0 and count[player][1] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][1] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][2]),(d[player]['I'][2]),(d[player]['N'][2]),(d[player]['G'][2]),(d[player]['O'][2])] == c_li :
                        if ( bingo>0 and count[player][2] ) == 0 :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][2] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][3]),(d[player]['I'][3]),(d[player]['N'][3]),(d[player]['G'][3]),(d[player]['O'][3])] == c_li :
                        if ( bingo>0 and count[player][3] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][3] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][4]),(d[player]['I'][4]),(d[player]['N'][4]),(d[player]['G'][4]),(d[player]['O'][4])] == c_li :
                        if ( bingo>0 and count[player][4] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][4] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    #Diagonal:
                    elif [(d[player]['B'][0]),(d[player]['I'][1]),(d[player]['N'][2]),(d[player]['G'][3]),(d[player]['O'][4])] == c_li :
                        if ( bingo>0 and count[player][5] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][5] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][4]),(d[player]['I'][3]),(d[player]['N'][2]),(d[player]['G'][1]),(d[player]['O'][0])] == c_li :
                        if ( bingo>0 and count[player][6] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][6] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)

          
# O O O O O O O O O O O O O O  O O O O O O O O O O O O O O O O O O O O O  O O O O O O O O O O O O O O                 
        if which_list == 'O':
             for player in d:
                def Check_Card():
                    card = '''
                           B - {}  {}  {}  {}  {}
                           
                           I - {}  {}  {}  {}  {}
                           
                           N - {}  {}  {}  {}  {}
                           
                           G - {}  {}  {}  {}  {}
                           
                           O - {}  {}  {}  {}  {}
                            '''
                    try:
                        print (card.format(d[player]['B'][0],d[player]['B'][1],d[player]['B'][2],d[player]['B'][3],d[player]['B'][4],
                                           d[player]['I'][0],d[player]['I'][1],d[player]['I'][2],d[player]['I'][3],d[player]['I'][4],
                                           d[player]['N'][0],d[player]['N'][1],d[player]['N'][2],d[player]['N'][3],d[player]['N'][4],
                                           d[player]['G'][0],d[player]['G'][1],d[player]['G'][2],d[player]['G'][3],d[player]['G'][4],
                                           d[player]['O'][0],d[player]['O'][1],d[player]['O'][2],d[player]['O'][3],d[player]['O'][4]))
                    except (ValueError, IndexError):
                        pass
                if element in (d[player]['O']):
                    ind=(d[player]['O']).index(element)
                    ((d[player]['O'])[ind])=0
                    #Horizontal
                    if (d[player]['O']) == c_li :
                       print('\n',player,'      Got a BINGO   !!!!!!!!')
                       Check_Card()
                       bingo -= 1
                       count[player][7] +=1
                       print('Bingo Left: ',bingo)
                    #VERTICAL :
                    elif [(d[player]['B'][0]),(d[player]['I'][0]),(d[player]['N'][0]),(d[player]['G'][0]),(d[player]['O'][0])] == c_li :
                        if ( bingo>0 and count[player][0] == 0) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][0] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][1]),(d[player]['I'][1]),(d[player]['N'][1]),(d[player]['G'][1]),(d[player]['O'][1])] == c_li :
                        if ( bingo>0 and count[player][1] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][1] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][2]),(d[player]['I'][2]),(d[player]['N'][2]),(d[player]['G'][2]),(d[player]['O'][2])] == c_li :
                        if ( bingo>0 and count[player][2] ) == 0 :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][2] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][3]),(d[player]['I'][3]),(d[player]['N'][3]),(d[player]['G'][3]),(d[player]['O'][3])] == c_li :
                        if ( bingo>0 and count[player][3] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][3] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][4]),(d[player]['I'][4]),(d[player]['N'][4]),(d[player]['G'][4]),(d[player]['O'][4])] == c_li :
                        if ( bingo>0 and count[player][4] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][4] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    #Diagonal:
                    elif [(d[player]['B'][0]),(d[player]['I'][1]),(d[player]['N'][2]),(d[player]['G'][3]),(d[player]['O'][4])] == c_li :
                        if ( bingo>0 and count[player][5] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][5] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                    elif [(d[player]['B'][4]),(d[player]['I'][3]),(d[player]['N'][2]),(d[player]['G'][1]),(d[player]['O'][0])] == c_li :
                        if ( bingo>0 and count[player][6] == 0 ) :
                            print('\n',player,'  Got a BINGO   !!!!!!!!')
                            Check_Card()
                            bingo -= 1
                            count[player][6] +=1
                            count[player][7] +=1
                            print('Bingo Left: ',bingo)
                        
#======================================================================================================================================
                
        else:
            #print('no match')
            pass

        time.sleep(0.1)     # Adjust if you have Patience.
        #print(count)           #Use Print(count) to Check the code for every itaration of Calls.
        
    print('''                  ___       __        ___   _       ___
                 |___ |\ | |  \      |  _  /_\ |\/||___
                 |___ | \| |__/      |_| ||   ||  ||___
            ''')
    
    #Final Result Of ALl Players : 
    for p in count:
        print('Player',p,'Got',count[p][7],'Bingos !!')
               
#=======================================================================================================================================
    

        
#==============================MULTI PLAYER============================


def multi_player():
    PlayerNo=int(input('Enter how many players:'))
    print('\nEnter Names of',PlayerNo,'Player: ')
    for player in range(PlayerNo):
        while len(player_names) != PlayerNo :
            name = input('\n Player Name: ')
            if not name in player_names:
                player_names.append(name)
            else:
                print('\n A player with same name already exist. !! \n')
    
    print('\nYou have Entered Player Names: ',player_names)
    game=input('\nPress ENTER for Continue.. \n')
    for p in player_names:
        print (p)
        key.append(p)
        Card()
    s=input('Press Enter for Start The Game >')
    solve()
multi_player()
