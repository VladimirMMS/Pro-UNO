from board import card_table, Board, ult_board
from os import system
from deck import total_card , normal_creation, special_creation, Deck, colors
import sys
import random
import time





class Player:
    def __init__(self, name):
        self.name = name
        self.deck_of_player = []
        self.score = 0
        self.take = []
        self.play_check = 0

        
        
    def distribute_of_deck(self):
        random.shuffle(total_card)
        for i in range(7):
            card_1 = total_card.pop(0)
            self.deck_of_player.append(card_1)


    def play_game(self):
        system("cls")
        ult_board.create_table()
        table = ult_board.table
        print(table)
        print("""You name:                                      {}  """.format(self.name))
        print("""You card are:{} """.format(self.deck_of_player))
        print("You score is:{}".format(self.score))
 

#in case the first position of t_b is equal to these two letters, 
# you will have to enter the colors stored in colors_spe.
        
        if card_table[0] == ['change_of_color'] or card_table[0] == ['change_of_color+4']:
            intro = input("Enter the color of deck:")
            while intro not in colors:
                intro_c = input("Enter the color of deck:")
            card_table.insert(0,[intro, intro])
            
            system("cls")
            ult_board.create_table()
            table = ult_board.table
            print(table)
            
            print("""You name:                                         {}  """.format(self.name))
            print("""You card are:{} """.format(self.deck_of_player))
            print("You score is:{}".format(self.score))


    #here we save the length of the card number that the player has, 
    # to keep it present in the loop

        len_p = len(self.deck_of_player)
        ult = int(len_p)
        for com  in range(1, ult+1):
            if com == len_p:
                len_player = com

        #Here we enter the game system.
        if card_table[0] != 'change_of_color' or card_table[0] != 'change_of_color+4':
            while len(self.deck_of_player) == len_p:
                
                #the player is asked if he has a card to play, 
                # because it is optional to play
                
                veri = input("""                          Do you have card for play:""")
                if veri == "Yes":
                    
                    #In case the answer is yes, you will have to enter the position 
                    # of the card you want to draw, taking into account that it starts at zero.
                    
                    while True:
                        try:
                            introduc = int(input("PUT THE POSITION OF THE CARD:"))
                            break
                        except Exception:
                            print("IT HAVE TO BE A INTERGE, TRY AGAIN.")
                            
                    #In case the answer is yes, you will have to enter the position
                    #of the card you want to draw, taking into account that it starts at zero.
                    
                    for get in range(0, len(self.deck_of_player)):
                        if get == introduc:
                            self.take = self.deck_of_player.pop(get)
                            
                else:
                    if veri == "No":
                        print("You don't have card that match")
                        confi_veri = input("Enter 'No' for take:")
                        if confi_veri == "No":
                            self.take = total_card.pop(0)
                            self.play_check = 1
                            len_p = len_p+1
                           

        time.sleep(1)
        system("cls")
