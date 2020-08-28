from pro import total
from os import system
import random

binary_count = 0
system("cls")


class Board:
    def __init__(self):
        self.deck_table = []






    def cart_of_table(self):
        global binary_count
        #The cards that draw from total and it's go to the t_b.
        
        random.shuffle(total)
        cube = total.pop(0)
        self.deck_table.insert(0,cube)
        
        if binary_count == 1:
            for ra in range(1, len(self.deck_table)-1):
                delete = self.deck_table.pop(ra)
            self.deck_table.pop(-1)
            binary_count = 0
        binary_count = 1
        

#creation of the board, where we are going to watch
#the cards of the table.

    def table(self):
        
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


name_list = []
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
def create_players():
    global inputopcion
    verify_entre = int(inputopcion)
    for v_p in range(verify_entre):
        input_name = input("Enter name of player{}:".format(v_p + 1))
        if len(input_name) == 0 or len(input_name) > 20:
            print("Name is not valid, try again")
            input_name = input("Entre name of players{}:".format(v_p + 1))
        name_list.append(input_name)
    return name_list

input_player()
create_players()
system("cls")


ult_board = Board()
card_table = ult_board.deck_table
ult_board.cart_of_table()
table = ult_board.table()
