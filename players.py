from board import card_table, Board, name_list, ult_board
from os import system
from pro import total,creation,will, Deck, deck_see
import sys
import random
import time


players = []
count = 0
global_verify = 0


class Players:
    def __init__(self, name):
        self.name = name
        self.deck_of_player = []
        self.score = 0
        
        
        
    def distribute_of_deck(self):
        random.shuffle(total)
        for i in range(7):
            card_1 = total.pop(0)
            self.deck_of_player.append(card_1)



    def play_game(self):
        print("""You name:                                      {}  """.format(self.name))
        print("""You card are:{} """.format(self.deck_of_player))
        print("You score is:{}".format(self.score))
        verif_input = 0 

#to be able to use variable outside of functions, we can global it.

    
        global players
        global global_verify
        global count
        
        colors_spe = ['Blue', 'Red', 'Yellow','Green']
        
#in case the first position of t_b is equal to these two letters, 
# you will have to enter the colors stored in colors_spe.
        
        
        if card_table[0] == ['change_of_color'] or card_table[0] == ['change_of_color+4']:
            intro = input("Enter the color of deck:")
            while intro not in colors_spe:
                intro_c = input("Enter the color of deck:")
            card_table.insert(0,[intro, intro])
            system("cls")
            ult_board.table()
            print("""You name:                                         {}  """.format(self.name))
            print("""You card are:{} """.format(self.deck_of_player))
            print("You score is:{}".format(self.score))
    #this is corresponding to the cancellation deck.

        if len(players) == 1:
            counte = 1
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
                            take = self.deck_of_player.pop(get)
                            verif_input = 1
                else:
                    if veri == "No":
                        print("You don't have card that match")
                        confi_veri = input("Enter 'No' for take:")
                        if confi_veri == "No":
                            take = total.pop(0)
                            len_p = len_p+1
                            verif_input = 1
                
                if verif_input == 1:
                    if take == ['change_of_color']:
                        card_table.insert(0, take)
                        intro_c = input("Enter the color of deck:")
                        while intro_c not in colors_spe:
                            intro_c = input("Enter the color of deck:")
                        card_table.insert(0,[intro_c, intro_c])
                                
                    #in case the selected card is this, 
                    # it will do its respective ability.
                    
                    if take == ['change_of_color+4']:
                        verify_num = 0
                        for r_d in self.deck_of_player:
                            if len(r_d) != 1:
                                comparator_cube = card_table[0]
                                if r_d[0] in comparator_cube[0] or str(r_d[1]) in str(comparator_cube[-1]):
                                    print("You have card to play")
                                    print("Remember, you only can play that card, if don't have more")
                                    verify_num = 1
                                    self.deck_of_player.append(take)

                        #if the player no longer has any more card to play and only 
                        # has the change_of_color count_t it will not increase to one, and if they can play it
                        
                        if verify_num == 0:
                            if count == len(players)- 1:
                                card_table.insert(0, take)
                                for search in total[0:4]:
                                    for r in range(0, 1):
                                        buck = total.pop(r)
                                        players[0].deck_of_player.append(buck)
                                intro_c = input("Enter the color of deck:")
                                while intro_c not in colors_spe:
                                    intro_c = input("Enter the color of deck:")
                                card_table.insert(0,[intro_c, intro_c])
                    
                    
                        #in case the player will be the ultime.
                        
                            else:
                                if count != len(players)- 1:
                                    card_table.insert(0,take)
                                    for search in total[0:4]:
                                        for r in range(0, 1):
                                            buck = total.pop(r)
                                            players[count +1].deck_of_player.append(buck)
                                    intro_c = input("Enter the color of deck:")
                                    while intro_c not in colors_spe:
                                        intro_c = input("Enter the color of deck:")
                                    card_table.insert(0,[intro_c, intro_c])
                
                #the length of the cards that does not change color have two positions. 
                # Therefore its length is two.
                if verif_input == 1:
                    if len(take) == 2:
                        comparator_cube = card_table[0]
                        if take[0] in comparator_cube[0] or str(take[1]) in str(comparator_cube[-1]):
                            card_table.insert(0, take)
                            
                            
                            if take[-1] == 'sum_two': #this card adds two to the next player
                                print("{} Played sum_two".format(self.name))
                                if count == len(players)-1:
                                    for search in total[0:2]:
                                        for r in range(0, 1):
                                            buck = total.pop(r)
                                            players[0].deck_of_player.append(buck)
                                        
                                #in case the player will be the ultime.
                                
                                else:
                                    if count != len(players)-1:
                                        for search in total[0:2]:
                                            for r in range(0, 1):
                                                buck = total.pop(r)
                                                players[count +1].deck_of_player.append(buck)
                            
                            
                            
                            if take[-1] == 'Cancelation': #this card cancels his turn for one round.
                                print("{} Played Cancelation".format(self.name))
                                encapsula = []
                                if count != len(players)-1:
                                    elemento = players[count+1]
                                    for i in range(0, len(players)):
                                        if elemento == players[i]:
                                            encapsula.append(elemento)
                                            encapsula.append(i)
                                    players.pop(encapsula[1])
                                    
                                #in case the player will be the ultime.

                                if count == len(players)-1:
                                    elemento = players[0]
                                    for e in range(0, len(players)):
                                        if elemento == players[e]:
                                            encapsula.append(elemento)
                                            encapsula.append(e)
                                    players.pop(encapsula[1])
                                    
                            
                            if take[-1] == 'Direction': #this card reverses directions.
                                print("{} Played Direction".format(self.name))
                                global_verify = 1
                                new = []
                                solo = players[count]
                                cont = []
                                for e in range(len(players)):
                                    cont.append(e)
                                    if players[e] == solo:
                                        new.append(players[e])
                                    if solo != players[0]:
                                        if new:
                                            for i in cont[::-1]:
                                                if players[i-1] != solo:
                                                    new.append(players[i-1])
                                                    
                                            cont = []

                                    #this condition will be fulfilled in case it 
                                    # is not equal to first position.
                                    
                                    else:
                                        if len(cont) == len(players):
                                            for i in cont[::-1]:
                                                if players[i] != solo:
                                                    new.append(players[i])
                                
                                #to update the shifts of the new positions.
                                
                                if len(name_list) == 4:
                                    new = [new[1], new[2], new[3], new[0]]
                                    players = new
                                if len(name_list) == 3:
                                    new = [new[1], new[2], new[0]]
                                    players = new
                                if len(name_list) == 2:
                                    new = [new[1], new[0]]
                                    players = new
                                
                        else:
                            print('the deck is not compatible')
                            self.deck_of_player.append(take)
                            len_p = len_p - 1
        
        #This belongs to the cancellation card,
        #  this is to re-enter at a certain time the player
        #  whose turn is canceled in a defined way
        
        if len(name_list) == 4 or len(name_list) == 3:
            if len(players) != len(name_list):
                if encapsula[1] == len(name_list)-1:
                    if count == 0:
                        players.insert(encapsula[1], encapsula[0])
        
        #this is for different types of case
        
        if len(name_list) == 4 or len(name_list) == 3:
            if len(players) < len(name_list):
                if count == 1:
                    players.insert(encapsula[1], encapsula[0])
                    count +=1
                    
        #this is for different types of case
        
        if len(name_list) == 2:
            if len(players) < len(name_list):
                if counte == 1:
                    if encapsula[1] == 1:
                        players.insert(encapsula[1], encapsula[0])
        
        #this is for different types of case.
        
        if len(name_list) == 2:
            if len(players) < len(name_list):
                if counte == 1:
                    if encapsula[1] == 0:
                        players.insert(encapsula[1], encapsula[0])
                        count+=1
                        
        if len(players) != len(name_list):
            if len(self.deck_of_player) == 1:
                players.insert(encapsula[1], encapsula[0])

        time.sleep(1)
        system("cls")
        table = ult_board.table()





    def win_player(self):
        global total
        global card_table
        #If don't have cards in total of decks.
        
        if len(total) == 0:
            for dist in range(0,len(card_table)):
                get = card_table[dist].pop(0)
                total.append(get)
        
        #If the players only have one cards, winer the round.
        
        if len(self.deck_of_player) <= 1:
            UNO = input("ENTER 'UNO' TO WINNER THE ROUND:")
            if UNO == "UNO":
                
                #if someone winner add him 100 point, can winner with 500 point.
                
                self.score +=100
                print( "THE WINNER OF THIS ROUND IS:{}".format(self.name))
                Start = input("DO YOU WANT PLAY OTHER ROUND?:")
                if Start == "Yes":
                    conte = 0
                
                #This while is return all card to total.
                
                    while len(players[conte].deck_of_player) > 0:
                        players[conte].deck_of_player = []
                        conte+=1
                        if conte == len(name_list):
                            conte = 0
                
                
                #This is return all score to zero.
                
                    if self.score == 500:
                        while players[conte].score > 0:
                            players[conte].score = 0
                            conte+=1
                    
                    total = []

                #Call of function again, for the new round.
                    
                    last_decks = deck_see
                    total = last_decks.decks
                    will = deck_see.create_willcard()
                    
                    ult_board.cart_of_table()
                    system("cls")
                    ult_board.table()
                    
                    
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
                        card1 = total.pop(0)
                        self.deck_of_player.append(card1)
                        system("cls")
                        ult_board.Table()

    def distribute_again(self):
        #In case a round ends, here the cards will be dealt again.
        
        if len(self.deck_of_player) == 0:
            random.shuffle(total)
            for i in range(7):
                card1 = total.pop(0)
                self.deck_of_player.append(card1)
                card_table = total.pop(0)
