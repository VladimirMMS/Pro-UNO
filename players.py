from board import t_b, Board, PlayerList, Ult_board, compro_d
from os import system
from pro import total,creation,will, Deck, Deck_see
import sys
import random
import time


players = []
count = 0
global_cont = 0


class Players:
    def __init__(self, name):
        self.name = name
        self.deck_of_player = []
        self.score = 0
        
        
        
    def Distribute_of_deck(self):
        random.shuffle(total)
        for i in range(7):
            card1 = total.pop(0)
            self.deck_of_player.append(card1)



    def PLay_game1(self):
        print("""                                      {}  """.format(self.name))
        print("""You card are:{} """.format(self.deck_of_player))
        print("You score is:{}".format(self.score))


#to be able to use variable outside of functions, we can global it.

        global take
        global players
        global global_cont
        global encapsula
        global count
        
        colors_spe = ['Blue', 'Red', 'Yellow','Green']
        
#in case the first position of t_b is equal to these two letters, 
# you will have to enter the colors stored in colors_spe.
        
        
        if t_b[0] == ['change_of_color'] or t_b[0] == ['change_of_color+4']:
            intro = input("Enter the color of deck:")
            for bus in colors_spe:
                if bus in intro:
                    t_b.insert(0,[intro, intro])
                    system("cls")
                    Ult_board.Table()
                    
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
        
        if t_b[0] != 'change_of_color' or t_b[0] != 'change_of_color+4':
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
                            
                            
                            #in case the selected card is this, 
                            # it will do its respective ability.
                            
                            if take == ['change_of_color']:
                                t_b.insert(0,take)
                                intro_c = input("Enter the color of deck:")
                                for bus in colors_spe:
                                    if bus in intro_c:
                                        t_b.insert(0,[intro_c, intro_c])
                                        
                            #in case the selected card is this, 
                            # it will do its respective ability.
                            
                            if take == ['change_of_color+4']:
                                count_m = 0
                                for r_d in self.deck_of_player:
                                    if len(r_d) != 1:
                                        
                            #This card can be played only if you no longer 
                            # have a card compatible with the table card.
                            
                                        conten = t_b[0]
                                        if r_d[0] in conten[0] or str(r_d[1]) in str(conten[-1]):
                                            print("You have card to play")
                                            print("Remember, you only can play that card, if don't have more")
                                            count_m = 1
                                            self.deck_of_player.append(take)

                                #if the player no longer has any more card to play and only 
                                # has the change_of_color count_t it will not increase to one, and if they can play it
                                
                                if count_m == 0:
                                    if count == len(players)- 1:
                                        t_b.insert(0,take)
                                        for search in total[0:4]:
                                            for r in range(0,1):
                                                buck = total.pop(r)
                                                players[0].deck_of_player.append(buck)
                                        intro_c = input("Enter the color of deck:")
                                        for bus in colors_spe:
                                            if bus in intro_c:
                                                t_b.insert(0,[intro_c,intro_c])
                                                
                                
                                #in case the player will be the ultime.
                                
                                    else:
                                        if count != len(players)- 1:
                                            t_b.insert(0,take)
                                            for search in total[0:4]:
                                                for r in range(0,1):
                                                    buck = total.pop(r)
                                                    players[count +1].deck_of_player.append(buck)
                                            intro_c = input("Enter the color of deck:")
                                            for bus in colors_spe:
                                                if bus in intro_c:
                                                    t_b.insert(0,[intro_c, intro_c])
                            
                            #the length of the cards that does not change color have two positions. 
                            # Therefore its length is two.
                            
                            if len(take) == 2:
                                conten = t_b[0]
                                if take[0] in conten[0] or str(take[1]) in str(conten[-1]):
                                    t_b.insert(0,take)
                                    
                                    
                                    if take[-1] == 'sum_tow': #this card adds two to the next player
                                        print("{} Played sum_two".format(self.name))
                                        if count == len(players)- 1:
                                            for search in total[0:2]:
                                                for r in range(0,1):
                                                    buck = total.pop(r)
                                                    players[0].deck_of_player.append(buck)
                                                
                                        #in case the player will be the ultime.
                                        
                                        else:
                                            if count != len(players) - 1:
                                                for search in total[0:2]:
                                                    for r in range(0,1):
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
                                        global_cont = 1
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
                                        
                                        if len(PlayerList) == 4:
                                            new = [new[1],new[2],new[3],new[0]]
                                            players = new
                                        if len(PlayerList) == 3:
                                            new = [new[1],new[2],new[0]]
                                            players = new
                                        if len(PlayerList) == 2:
                                            new = [new[1],new[0]]
                                            players = new
                                        
                                else:
                                    if take[0] not in conten[0] or str(take[1]) not in str(conten[-1]):
                                        print('Mov incorrect')         
                #If the player says that he has no card to play, 
                # he will have to take it from the table.
                else:
                    if veri == "No":
                        print("You don't have card that match")
                        mazo = input("Enter 'No' for take:")
                        if mazo == "No":
                            m = total.pop(0)
                            
                            
                            #We use the same logic as above, 
                            # in case the card you draw has an ability.
                            
                            if m != ['change_of_color']:  
                                if m != ['change_of_color+4']:
                                    conten = t_b[0]
                                    if m[0] in conten[0] or str(m[1]) in str(conten[-1]):
                                        len_p = len_p+1
                                        t_b.insert(0, m)
                                        
                                        
                                        if m[-1] == 'sum_tow':#this card adds two to the next player.
                                            print("{} Played sum_two".format(self.name))
                                            if count == len(players)- 1:
                                                for search in total[0:2]:
                                                    for r in range(0,1):
                                                        buck = total.pop(r)
                                                        players[0].deck_of_player.append(buck)
                                            else:
                                                if count != len(players) - 1:
                                                    for search in total[0:2]:
                                                        for r in range(0,1):
                                                            buck = total.pop(r)
                                                            players[count +1].deck_of_player.append(buck)
                                        
                                        
                                        if m[-1] == 'Cancelation': #this card cancels his turn for one round.
                                            print("{} Played Cancelation".format(self.name))
                                            encapsula = []
                                            if count != len(players)-1:
                                                elemento = players[count+1]
                                                for i in range(0, len(players)):
                                                    if elemento == players[i]:
                                                        encapsula.append(elemento)
                                                        encapsula.append(i)
                                                players.pop(encapsula[1])

                                            if count == len(players)-1:
                                                elemento = players[0]
                                                for e in range(0, len(players)):
                                                    if elemento == players[e]:
                                                        encapsula.append(elemento)
                                                        encapsula.append(e)
                                                players.pop(encapsula[1])
                                                
                                                
                                                
                                        if m[-1] == 'Direction': #this card reverses directions.
                                            print("{} Played Direction".format(self.name))
                                            global_cont = 1
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
                                                #is not equal to first position.
                                                
                                                else:
                                                    if len(cont) == len(players):
                                                            for i in cont[::-1]:
                                                                if players[i] != solo:
                                                                    new.append(players[i])
                                            
                                            #to update the shifts of the new positions.
                                            
                                            if len(PlayerList) == 4:
                                                new = [new[1],new[2],new[3],new[0]]
                                                players = new
                                            if len(PlayerList) == 3:
                                                new = [new[1],new[2],new[0]]
                                                players = new
                                            if len(PlayerList) == 2:
                                                new = [new[1],new[0]]
                                                players = new
                                    
                                    #in case you do not meet the conditions.
                                    else:
                                        self.deck_of_player.append(m)

                            #in case the selected card is this, 
                            # it will do its respective ability.
                            
                            if m == ['change_of_color']:
                                len_p = len_p+1
                                t_b.insert(0, m)
                                intro_c = input("Enter the color of deck:")
                                for bus in colors_spe:
                                    if bus in intro_c:
                                        t_b.insert(0,[intro_c, intro_c])
                                        
                            #if the player no longer has any more card to play and only 
                            # has the change_of_color count_t it will not increase to one, and if they can play it
                            
                            if m == ['change_of_color+4']:
                                len_p = len_p+1
                                t_b.insert(0, m)
                                if count == len(players)- 1:
                                    for search in total[0:4]:
                                        for r in range(0,1):
                                            buck = total.pop(r)
                                            players[0].deck_of_player.append(buck)
                                    intro_c = input("Enter the color of deck:")
                                    for bus in colors_spe:
                                        if bus in intro_c:
                                            t_b.insert(0,[intro_c, intro_c])
                                
                                #in case the player will be the ultime.
                                
                                else:
                                    if count != len(players)- 1:
                                        t_b.insert(0,m)
                                        for search in total[0:4]:
                                            for r in range(0,1):
                                                buck = total.pop(r)
                                                players[count +1].deck_of_player.append(buck)
                                        intro_c = input("Enter the color of deck:")
                                        for bus in colors_spe:
                                            if bus in intro_c:
                                                t_b.insert(0,[intro_c, intro_c])
        
        #This belongs to the cancellation card,
        #  this is to re-enter at a certain time the player
        #  whose turn is canceled in a defined way
        
        if len(PlayerList) == 4 or len(PlayerList) == 3:
            if len(players) != len(PlayerList):
                if encapsula[1] == len(PlayerList)-1:
                    if count == 0:
                        players.insert(encapsula[1],encapsula[0])
        
        #this is for different types of case
        
        if len(PlayerList) == 4 or len(PlayerList) == 3:
            if len(players) < len(PlayerList):
                if count == 1:
                    players.insert(encapsula[1],encapsula[0])
                    count +=1
                    
        #this is for different types of case
        
        if len(PlayerList) == 2:
            if len(players) < len(PlayerList):
                if counte == 1:
                    if encapsula[1] == 1:
                        players.insert(encapsula[1],encapsula[0])
        
        #this is for different types of case.
        
        if len(PlayerList) == 2:
            if len(players) < len(PlayerList):
                if counte == 1:
                    if encapsula[1] == 0:
                        players.insert(encapsula[1],encapsula[0])
                        count+=1
                        
        if len(players) != len(PlayerList):
            if len(self.deck_of_player) == 1:
                players.insert(encapsula[1], encapsula[0])

        time.sleep(1)
        system("cls")
        table = Ult_board.Table()





    def winner_of_player(self):
        global total
        global t_b
        global table
        global compro_d
        #If don't have cards in total of decks.
        
        if len(total) == 0:
            for dist in range(0,len(t_b)):
                get = t_b[dist].pop(0)
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
                        if conte == len(PlayerList):
                            conte = 0
                
                
                #This is return all score to zero.
                
                    if self.score == 500:
                        while players[conte].score > 0:
                            players[conte].score = 0
                            conte+=1
                    
                    total = []
                
                #Call of function again, for the new round.
                    
                    compro = Deck_see
                    total = compro.decks
                    will = Deck_see.creation_of_willcard()
                    
                    Ult_board.cart_of_table()
                    system("cls")
                    Ult_board.Table()
                    
                    
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
                        Ult_board.Table()

    def distribute_again(self):
        #In case a round ends, here the cards will be dealt again.
        
        if len(self.deck_of_player) == 0:
            random.shuffle(total)
            for i in range(7):
                card1 = total.pop(0)
                self.deck_of_player.append(card1)
                card_table = total.pop(0)
