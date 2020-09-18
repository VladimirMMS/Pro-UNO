from players import Player
from deck import total_card, colors, Deck
from board import card_table, Board, ult_board
from os import system
import random
import sys
import time


class Game:
    def __init__(self):
        self.players = []
        self.count = 0
        self.players_direction = 0



    def create_player(self):
        #check is a verification of the number of player that we can-
    #enter

        check = '234'
        inputopcion = input("Enter number of players:")
        if len(inputopcion) != 1:
            print("IT'S INVALID")
        
        while inputopcion not in check:
            #if the number is not in check the while don't-
            #go to break
            print("IT'S INVALID")
            inputopcion = input("Enter number of players:")

        verify_entre = int(inputopcion)
        for v_p in range(verify_entre):
            input_name = input("Enter name of player{}:".format(v_p + 1))
            if len(input_name) == 0 or len(input_name) > 20:
                while len(input_name) == 0:
                    print("Name is not valid, try again")
                    input_name = input("Entre name of players{}:".format(v_p + 1))
            self.players.append(Player(input_name))
    
    def check_compatibility(self):
        
        #the length of the cards that does not change color have two positions. 
        # Therefore its length is two.
        
        take = self.players[self.count].take
         
        if len(self.players[self.count].take) == 2:
            comparator_cube = card_table[0]
            if take[0] in comparator_cube[0] or str(take[1]) in str(comparator_cube[-1]):
                card_table.insert(0, take)
                self.players[self.count].play_check = 2
                 
            else:
                if self.players[self.count].play_check == 0:
                    print("THAT CARD IS INCORRECT")
                    self.players[self.count].deck_of_player.append(take)
                   
                
                if self.players[self.count].play_check == 1:
                    print("THAT CARD IS INCORRECT")
                    self.players[self.count].deck_of_player.append(take)
                   
            
    def add_ability(self):
        print(self.players[self.count].take)
        if self.players[self.count].take == ['change_of_color']:
            card_table.insert(0, self.players[self.count].take)
            intro_c = input("Enter the color of deck:")
            while intro_c not in colors:
                intro_c = input("Enter the color of deck:")
            card_table.insert(0,[intro_c, intro_c])
        
        if self.players[self.count].take == ['change_of_color+4']:
            verify_messeger = 0
            for r_d in self.players[self.count].deck_of_player:
                if len(r_d) != 1:
                    comparator_cube = card_table[0]
                    if r_d[0] in comparator_cube[0] or str(r_d[1]) in str(comparator_cube[-1]):
                        verify_messeger = 1
            
            
            if verify_messeger == 1:
                self.players[self.count].deck_of_player.append(self.players[self.count].take)
                print("You have card to play")
                print("Remember, you only can play that card, if don't have more")
                
            #if the player no longer has any more card to play and only 
            # has the change_of_color count_t it will not increase to one, and if they can play it
            
            if verify_messeger == 0:
                self.players[self.count].play_check == 1
                if self.count == len(self.players)- 1:
                    card_table.insert(0, self.players[self.count].take)
                    for search in total_card[0:4]:
                        for r in range(0, 1):
                            buck = total_card.pop(r)
                            self.players[0].deck_of_player.append(buck)
                    intro_c = input("Enter the color of deck:")
                    while intro_c not in colors:
                        intro_c = input("Enter the color of deck:")
                    card_table.insert(0,[intro_c, intro_c])
            
                #in case the player will be the ultime.

                else:
                    if self.count != len(self.players)- 1:
                        card_table.insert(0,self.players[self.count].take)
                        for search in total_card[0:4]:
                            for r in range(0, 1):
                                buck = total_card.pop(r)
                                self.players[self.count +1].deck_of_player.append(buck)
                        intro_c = input("Enter the color of deck:")
                        while intro_c not in colors:
                            intro_c = input("Enter the color of deck:")
                        card_table.insert(0,[intro_c, intro_c])
                        
        take = self.players[self.count].take         
        comparator_cube = card_table[0]
        if len(take) == 2:
            if take[0] in comparator_cube[0] or str(take[1]) in str(comparator_cube[-1]):
                    
                if self.players[self.count].take[-1] == 'Sum_two': #this card adds two to the next player
                    print("{} Played sum_two".format(self.players[self.count].name))
                    if self.count == len(self.players)-1:
                        for search in total_card[0:2]:
                            for r in range(0, 1):
                                buck = total_card.pop(r)
                                self.players[0].deck_of_player.append(buck)
                            
                    #in case the player will be the ultime.
                    
                    else:
                        if self.count != len(self.players)-1:
                            for search in total_card[0:2]:
                                for r in range(0, 1):
                                    buck = total_card.pop(r)
                                    self.players[self.count +1].deck_of_player.append(buck)    
            
            
                
                
                if self.players[self.count].take[-1] == 'Direction': #this card reverses directions.
                    print("{} Played Direction".format(self.players[self.count].name))
                    self.players_direction = 1
                    new = []
                    solo = self.players[self.count]
                    cont = []
                    for e in range(len(self.players)):
                        cont.append(e)
                        if self.players[e] == solo:
                            new.append(self.players[e])
                        if solo != self.players[0]:
                            if new:
                                for i in cont[::-1]:
                                    if self.players[i-1] != solo:
                                        new.append(self.players[i-1])
                                        
                                cont = []

                        #this condition will be fulfilled in case it 
                        # is not equal to first position.
                        
                        else:
                            if len(cont) == len(self.players):
                                for i in cont[::-1]:
                                    if self.players[i] != solo:
                                        new.append(self.players[i])
                    
                    #to update the shifts of the new positions.
                    
                    if len(self.players) == 4:
                        new = [new[1], new[2], new[3], new[0]]
                        self.players = new
                    if len(self.players) == 3:
                        new = [new[1], new[2], new[0]]
                        self.players = new
                    if len(self.players) == 2:
                        
                        new = [new[0], new[1]]
                        self.players = new
                        
                if self.players[self.count].take[-1] == 'Cancelation':
                    print("{} Played Cancelation".format(self.players[self.count].name))
                    replit = 0
                    if self.count == len(self.players) -2:
                        self.count = -1
                        
                    if self.count == len(self.players)-1:
                        self.count = 0
                        replit = 1
                        
                        
                    if replit == 0:
                        if len(self.players) == 4:
                            if self.count == 0 or self.count == 1:
                                self.count = self.count +1
                            
                    if len(self.players) == 3:
                        if self.count == 0:
                            self.count = self.count + 1

    
            
        time.sleep(1.5)
        system("cls")
        
    
    
    def win_player(self):
        global total_card
        global card_table
        #If don't have cards in total of decks.
        
        if len(total_card) == 0:
            for dist in range(0,len(card_table)):
                get = card_table[dist].pop(0)
                total_card.append(get)
        
        #If the players only have one cards, winer the round.
        
        if len(self.players[self.count].deck_of_player) == 1:
            UNO = input("ENTER 'UNO' TO WINNER THE ROUND:")
            if UNO == "UNO":
                
                #if someone winner add him 100 point, can winner with 500 point.
                
                self.players[self.count].score +=100
                print( "THE WINNER OF THIS ROUND IS:{}".format(self.players[self.count].name))
                Start = input("DO YOU WANT PLAY OTHER ROUND?:")
                if Start == "Yes":
                    conte = 0
                
                #This while is return all card to total.
                
                    while len(self.players[conte].deck_of_player) > 0:
                        self.players[conte].deck_of_player = []
                        conte+=1
                        if conte == len(self.players):
                            conte = 0    
                
                #This is return all score to zero.
                
                    if self.players[self.count].score == 500:
                        while self.players[conte].score > 0:
                            self.players[conte].score = 0
                            conte+=1
                    
                    total_card = []

                #Call of function again, for the new round.
                    
                    card = Deck()
                    normal_creation = card.create_cards()
                    special_creation = card.create_specialcards()
                    total_card = card.decks_compi
                    
                    ult_board.cart_of_table()
                    system("cls")
                    ult_board.create_table()
                    
                 
            #If the player does not want continue playing.
                else:
                    if Start != "Yes":
                        print("Game suspended")
                        sys.exit()

            #If players does not enter "UNO" correct.
            else:
                if UNO != "UNO":
                    print("You lost the opportunity of winner, you will have three more cards")
                    for inc in range(3):
                        card1 = total_card.pop(0)
                        self.players[self.count].deck_of_player.append(card1)
                        system("cls")
                        ult_board.create_table()
                        
                   
        if len(self.players[self.count].deck_of_player) == 0:
            for all_player in game.players:
                all_player.distribute_of_deck()
                
        if self.players[self.count].play_check == 0:
            self.count = self.count -1
    
                
                
game = Game()
        