from deck import total_card
from os import system
import random


system("cls")

class Board:
    def __init__(self):
        self.table = ""
        self.deck_table = []



    def cart_of_table(self):
        global card_table
        card_table = []
        #The cards that draw from total and it's go to the t_b.
        
        random.shuffle(total_card)
        cube = total_card.pop(0)
        self.deck_table.insert(0,cube)

        

#creation of the board, where we are going to watch
#the cards of the table.

    def create_table(self):
        
#The table, where the players will put the cards.
        print("""
              
                            * * * * * *  * * * * *  *        *  * * * *
                            *            *       *  *  *   * *  *
                            * * * * * *  * * * * *  *    *   *  * * * *
                            *         *  *       *  *        *  *
                            * * * * * *  *       *  *        *  * * * *
              """)
        self.table=("""                    
                    __________________________________________________________                  
                    |                                                        |  
                    |                                                        |
                    |                                                        |
                    |                                                        |
                    |                                                        |
                    |                                                        |
                                        [CARD]{} 
                    |                                                        |
                    |                                                        |
                    |                                                        |
                    |                                                        | 
                    |                                                        |
                    |                                                        |
                    |________________________________________________________|
                                                                """.format(self.deck_table[0]))
        




ult_board = Board()
ult_board.cart_of_table()
card_table = ult_board.deck_table
ult_board.create_table()
table = ult_board.table
