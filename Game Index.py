# Game Index
def main_menu():
    print('''******************************************************************************

                        <<  Wllcome to Bingo Python >>
           
                        [   < 1 > For New Game.     ]   
           
                        [   < 2 > For Check Score.  ]

                    
______________________________________________________________________________
''')
    inp=input(':')
    if (inp=='1'):
        #Card()
        main_menu()
    elif (inp=='2'):
        print('''
                       !!!   No New Scores Yet   !!!
                             LETS MAKE ONE  >>>
                             
                                      
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


''')
        main_menu()
    else:
        print('''

!!!!!!!!!!!!!!!!!!!!!!!!!        Wrong Input       !!!!!!!!!!!!!!!!!!!!!!!!!!

''')
        main_menu()
        
main_menu()
