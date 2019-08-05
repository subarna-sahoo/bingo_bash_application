import random
Glis=[0,0,0,0,0]
Bingo=5
def Rand(start=1, end=30, num=5):
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
    Bli = [lis1[0],lis2[0],lis3[0],lis4[0],lis5[0]]
    Ili = [lis1[1],lis2[1],lis3[1],lis4[1],lis5[1]]
    Nli = [lis1[2],lis2[2],lis3[2],lis4[2],lis5[2]]
    Gli = [lis1[3],lis2[3],lis3[3],lis4[3],lis5[3]]
    Oli = [lis1[4],lis2[4],lis3[4],lis4[4],lis5[4]]
    print('Your Card: \n')
    print('\n',lis1,'\n',lis2,'\n',lis3,'\n',lis4,'\n',lis5)
    print('\n',Bli,'\n',Ili,'\n',Nli,'\n',Gli,'\n',Oli)
#Rand()
r=Rand()
print(r.lis1)
