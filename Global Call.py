import random
import time

#Global Call
for draw in range(10000):
    list_names = ['B','I','N','G','O']
    random_name =(random.choice(list_names))   
    element=(random.randint(10,35))  
    print(random_name,element)

    print('\n')
    time.sleep(0.5)
