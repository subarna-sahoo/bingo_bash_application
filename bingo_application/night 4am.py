from random import randint


def a(start=10, end=20, num=12):
    global B
    B = []
    I = []
    N = []
    G = []
    O = []
    
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
    v={'B':B,'I':I,'N':N,'G':G,'O':O}
    return v
#Card()
value = []
def start():
   b = a()
   value.append(b)
   print(type(value))
   e=(value[0])
   print(e['I'])
start()
