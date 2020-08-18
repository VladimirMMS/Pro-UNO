from pro import total
from os import system
import random

compro_d = 0
system("cls")


class Board:
    def __init__(self):
        self.deck_table = []






    def cart_of_table(self):
        global compro_d
        # delete = []
        #The cards that draw from total and it's go to the t_b.
        #t_b is an abbreviation of table.
        
        random.shuffle(total)
        card_table = total.pop(0)
        self.deck_table.insert(0,card_table)
        
        if compro_d == 1:
            for ra in range(1, len(self.deck_table)-1):
                delete = self.deck_table.pop(ra)
            self.deck_table.pop(-1)
        compro_d = 1
        

#creation of the board, where we are going to watch
#the cards of the table.

    def Table(self):
        
#The table, where the players will put the cards.
        print("""                    __________________________________________________________                  
                    |                                                        |  
                    |                                                        |
                    |                                                        |
                    |                                                        |
                    |                                                        |
                    |                                                        |
                                        [DECKS]{} 
                    |                                                        |
                    |                                                        |
                    |                                                        |
                    |                                                        | 
                    |                                                        |
                    |                                                        |
                    |________________________________________________________|
                                                                """.format(self.deck_table[0]))


PlayerList = []
inputopcion = ''

def input_player():
    #check is a verification of the number of player that we can-
    #enter
    global inputopcion
    check = '234'
    inputopcion = input("Enter number of players:")
    if len(inputopcion) != 1:
        print("IT'S INVALID")
    
    while inputopcion not in check:
        #if the number is not in check the while don't-
        #go to break
        print("IT'S INVALID")
        inputopcion = input("Enter number of players:")
    return int(inputopcion)


#Here verify the number of letter from name create.
def creator_of_player():
    global inputopcion
    verify_entre = int(inputopcion)
    for v_p in range(verify_entre):
        input_name = input("Enter name of player{}:".format(v_p + 1))
        if len(input_name) == 0 or len(input_name) > 20:
            print("Name is not valid, try again")
            input_name = input("Entre name of players{}:".format(v_p + 1))
        PlayerList.append(input_name)
    return PlayerList

input_player()
creator_of_player()
system("cls")


Ult_board = Board()
t_b = Ult_board.deck_table
Ult_board.cart_of_table()
table = Ult_board.Table()

