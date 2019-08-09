from random import randint

#Get Cards
def Card(start=10, end=18, num=10):
    print('Your Card')
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
    def check_card():
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
    check_card()
Card()
