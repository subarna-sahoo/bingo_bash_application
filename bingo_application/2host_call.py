from random import randint
import random
import time


ltr = ['B', 'I', 'N', 'G', 'O']
for draw in range(1000):    
    drawn_numbers=list()
    bingo_draw=randint(1,90)
    
    if not bingo_draw in drawn_numbers:
        print((random.choice(ltr)),'-',(bingo_draw))
        #print(bingo_draw)
        print('\n')
        
        drawn_numbers.append(bingo_draw)
        time.sleep(0.5)
