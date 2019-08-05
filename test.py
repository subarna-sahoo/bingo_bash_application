import time
import random

ltr = ['B', 'I', 'N', 'G', 'O']

lis=(random.choice(ltr))
print('\nWhich list: ',lis)
print(type(lis))

element=str(random.randint(1,5))    #(start=1,end=5)
print('Element: ',element)
print(type(element))

B =[1,2,3,4,5]
I =[1,2,3,4,5]
N =[1,2,3,4,5]
G =[1,2,3,4,5]
O =[1,2,3,4,5]

index=lis.index(element)        # ValueError: suBstring not found
print('index: ',index)

ind=int(index)
lis[ind]=0  #changed that random index value to Zero

print(B,I,N,G,O)
