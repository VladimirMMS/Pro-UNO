from board import t_b, Board, PlayerList
from os import system
from pro import total,creation,will, cumcolor, copy_total
import sys
import random

players = []
count = 0
global_cont = 0
voucher = 0




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



    def Play_game1(self):
        global voucher
        global take
        global players
        global global_cont
        global count
        global encapsula
        len_player = len(self.deck_of_player)
        ult = int(len_player)
        for com  in range(1, ult+1):
            if com == len_player:
                len_player = com
        colors_spe = ['Blue', 'Red', 'Yellow','Green']
        if len(players) == 1:
                counte = 1
        len_players = len(players)-1
        if t_b[0] == 'change_of_color' or t_b[0] == 'change_of_color+4':
            while len(self.deck_of_player) == len_player:
                voucher = 1
                introduc = input("PUT THE POSITION OF THE CARD:")
                conver = int(introduc)
                for get in range(0, len(self.deck_of_player)):
                    if get == conver:
                        take = self.deck_of_player.pop(get)
                    t_b.append(take)
                    if take[-1] == 'sum_tow':
                        print("{} Played sum two.".format(self.name))
                        if count == len(players)-1:
                            for search in total[0:2]:
                                for r in range(0,1):
                                    buck = total.pop(r)
                                    players[0].deck_of_player.append(buck)
                        else:
                            if count != len(players)-1:
                                for search in total[0:2]:
                                    for r in range(0,1):
                                        buck = total.pop(r)
                                        players[count +1].deck_of_player.append(buck)
                                        print(self.deck_of_player)
                    if take[-1] == 'Cancelation':
                        print("{} Played Cancelation".format(self.name))
                        print(self.name)
                        print(count)
                        encapsula = []
                        if count != len(players)-1:
                            elemento = players[count+1]
                            for i in range(0, len(players)):
                                if elemento == players[i]:
                                    encapsula.append(elemento)
                                    encapsula.append(i)
                            players.pop(encapsula[1])

                        if count == len_players:
                            elemento = players[0]
                            for e in range(0, len(players)):
                                if elemento == players[e]:
                                    encapsula.append(elemento)
                                    encapsula.append(e)
                            players.pop(encapsula[1])
                            
                    if take[-1] == 'Direction':
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
                            else:
                                if len(cont) == len(players):
                                    for i in cont[::-1]:
                                        if players[i] != solo:
                                            new.append(players[i])
                        if len(PlayerList) == 4:
                            new = [new[1],new[2],new[3],new[0]]
                            players = new
                        if len(PlayerList) == 3:
                            new = [new[1],new[2],new[0]]
                            players = new
                        if len(PlayerList) == 2:
                            new = [new[1],new[0]]
                            players = new

        if len(PlayerList) == 4 or len(PlayerList) == 3:
            if len(players) != len(PlayerList):
                if encapsula[1] == len(PlayerList)-1:
                    if count == 0:
                        players.insert(encapsula[1],encapsula[0])
                        
        if len(PlayerList) == 4 or len(PlayerList) == 3:
            if len(players) < len(PlayerList):
                if count == 1:
                    players.insert(encapsula[1],encapsula[0])
                    count +=1
            
        if len(PlayerList) == 2:
            if len(players) < len(PlayerList):
                if counte == 1:
                    if encapsula[1] == 1:
                        players.insert(encapsula[1],encapsula[0])
                    
        if len(PlayerList) == 2:
            if len(players) < len(PlayerList):
                if counte == 1:
                    if encapsula[1] == 0:
                        players.insert(encapsula[1],encapsula[0])
                        count+=1




    def PLay_game2(self):
        print(t_b[-1])
        print("""                                      {}  """.format(self.name))
        print("""You card are:{} """.format(self.deck_of_player))
        global take
        global players
        global global_cont
        global encapsula
        global count
        global voucher
        if len(players) == 1:
            counte = 1
        colors_spe = ['Blue', 'Red', 'Yellow','Green']
        if len(t_b[0]) == 0:
            intro = input("Enter the color of deck:")
            for bus in colors_spe:
                if bus in intro_c:
                    t_b.append([intro, intro])   
        
        len_p = len(self.deck_of_player)
        ult = int(len_p)
        for com  in range(1, ult+1):
            if com == len_p:
                len_player = com
        if voucher == 0:
            if t_b[0] != 'change_of_color' or t_b[0] != 'change_of_color+4':
                while len(self.deck_of_player) == len_p:
                    veri = input("""                          Do you have card for play:""")
                    if veri == "Yes":
                        introduc = input("PUT THE POSITION OF THE CARD:")
                        conver = int(introduc)
                        for get in range(0, len(self.deck_of_player)):
                            if get == conver:
                                take = self.deck_of_player.pop(get)
                                print(take)
                                if take == ['change_of_color']:
                                    t_b.append(take)
                                    intro_c = input("Enter the color of deck:")
                                    for bus in colors_spe:
                                        if bus in intro_c:
                                            t_b.append([intro_c, intro_c])
                                    
                                if take == ['change_of_color+4']:
                                    count_m = 0
                                    for r_d in self.deck_of_player:
                                        if len(r_d) != 1:
                                            if r_d[0] in t_b[-1] or r_d[1] in t_b[-1]:
                                                print("You have card to play")
                                                print("Remember, you only can play that card, if don't have more")
                                                count_m = 1
                                                
                                    if count_m == 0:
                                        if count == len(players)- 1:
                                            t_b.append(take)
                                            for search in total[0:4]:
                                                for r in range(0,1):
                                                    buck = total.pop(r)
                                                    players[0].deck_of_player.append(buck)
                                            intro_c = input("Enter the color of deck:")
                                            for bus in colors_spe:
                                                if bus in intro_c:
                                                    t_b.append([intro_c,intro_c])
                                        else:
                                            if count != len(players)- 1:
                                                for search in total[0:4]:
                                                    for r in range(0,1):
                                                        buck = total.pop(r)
                                                        players[count +1].deck_of_player.append(buck)
                                                intro_c = input("Enter the color of deck:")
                                                for bus in colors_spe:
                                                    if bus in intro_c:
                                                        t_b.append([intro_c, intro_c])    
                                                    
                                if len(take) == 2:
                                    if take[0] in t_b[-1] or take[1] in t_b[-1]:
                                        t_b.append(take)
                                        if take[-1] == 'sum_tow':
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
                                                            
                                        if take[-1] == 'Cancelation':
                                            print("{} Played Cancelation".format(self.name))
                                            encapsula = []
                                            len_players = len(players)-1
                                            if count != len(players)-1:
                                                elemento = players[count+1]
                                                for i in range(0, len(players)):
                                                    if elemento == players[i]:
                                                        encapsula.append(elemento)
                                                        encapsula.append(i)
                                                players.pop(encapsula[1])

                                            if count == len_players:
                                                elemento = players[0]
                                                for e in range(0, len(players)):
                                                    if elemento == players[e]:
                                                        encapsula.append(elemento)
                                                        encapsula.append(e)
                                                players.pop(encapsula[1])
                                                        
                                        if take[-1] == 'Direction':
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
                                                else:
                                                    if len(cont) == len(players):
                                                        for i in cont[::-1]:
                                                            if players[i] != solo:
                                                                new.append(players[i])
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
                                        print('Mov incorrect')         
                                
                    else:
                        if veri == "No":
                            print("You don't have card that match")
                            mazo = input("Enter 'No' for take")
                            
                            if mazo == "No":
                                m = total.pop(0)
                                if m != ['change_of_color']:  
                                    if m != ['change_of_color+4']:
                                        if m[0] in t_b[-1] or m[1] in t_b[-1]:
                                            len_p = len_p+1
                                            print(len_player)
                                            print(len(self.deck_of_player))
                                            t_b.append(m)
                                            if m[-1] == 'sum_tow':
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
                                            if m[-1] == 'Cancelation':
                                                print("{} Played Cancelation".format(self.name))
                                                encapsula = []
                                                if count != len(players)-1:
                                                    elemento = players[count+1]
                                                    for i in range(0, len(players)):
                                                        if elemento == players[i]:
                                                            encapsula.append(elemento)
                                                            encapsula.append(i)
                                                    players.pop(encapsula[1])

                                                if count == len_players:
                                                    elemento = players[0]
                                                    for e in range(0, len(players)):
                                                        if elemento == players[e]:
                                                            encapsula.append(elemento)
                                                            encapsula.append(e)
                                                    players.pop(encapsula[1])
                                            if m[-1] == 'Direction':
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
                                                    else:
                                                        if len(cont) == len(players):
                                                                for i in cont[::-1]:
                                                                    if players[i] != solo:
                                                                        new.append(players[i])
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
                                            self.deck_of_player.append(m)
        
                                if m == ['change_of_color']:
                                    len_p = len_p+1
                                    t_b.append(m)
                                    intro_c = input("Enter the color of deck:")
                                    for bus in colors_spe:
                                        if bus in intro_c:
                                            t_b.append([intro_c, intro_c])
                                if m == ['change_of_color+4']:
                                    len_player = len_player+1
                                    t_b.append(take)
                                    if count == len(players)- 1:
                                        for search in total[0:4]:
                                            for r in range(0,1):
                                                buck = total.pop(r)
                                                players[0].deck_of_player(buck)
                                        intro_c = input("Enter the color of deck:")
                                        for bus in colors_spe:
                                            if bus in intro_c:
                                                t_b.append([intro_c, intro_c])
                                    else:
                                        if count != len(players)- 1:
                                            for search in total[0:4]:
                                                for r in range(0,1):
                                                    buck = total.pop(r)
                                                    players[count +1].deck_of_player.append(buck)
                                            intro_c = input("Enter the color of deck:")
                                            for bus in colors_spe:
                                                if bus in intro_c:
                                                    t_b.append([intro_c, intro_c])  

        if len(PlayerList) == 4 or len(PlayerList) == 3:
            if len(players) != len(PlayerList):
                if encapsula[1] == len(PlayerList)-1:
                    if count == 0:
                        players.insert(encapsula[1],encapsula[0])
                        
        if len(PlayerList) == 4 or len(PlayerList) == 3:
            if len(players) < len(PlayerList):
                if count == 1:
                    players.insert(encapsula[1],encapsula[0])
                    count +=1
            
        if len(PlayerList) == 2:
            if len(players) < len(PlayerList):
                if counte == 1:
                    if encapsula[1] == 1:
                        players.insert(encapsula[1],encapsula[0])
                    
        if len(PlayerList) == 2:
            if len(players) < len(PlayerList):
                if counte == 1:
                    if encapsula[1] == 0:
                        players.insert(encapsula[1],encapsula[0])
                        count+=1
    
    def winner_of_player(self):
        global total
        if len(total) == 0:
            for dist in range(0,len(t_b)):
                get = t_b[dist].pop(0)
                total.append(get)
        if len(self.deck_of_player) == 1:
            UNO = input("ENTER 'UNO' TO WINNER THE ROUND:")
            if UNO == "UNO":
                self.score +=100
                print( "THE WINNER OF THE ROUND IS:{}".format(self.name))
                Start = input("DO YOU WANT PLAY OTHER ROUND?:")
                if Start == "Yes":
                    conte = 0
                    while len(players[conte].deck_of_player) > 0:
                        players[conte].deck_of_player = []
                        conte+=1
                        if conte == len(PlayerList):
                            conte = 0
                    if self.score == 500:
                        while players[conte].score > 0:
                            players[conte].score = 0
                            conte+=1
                        
                else:
                    if Start != "Yes":
                        print("Game suspended")
                        sys.exit()

            else:
                if UNO != "UNO":
                    print("You lost the opportunity of winner, you will have three more cards")
                    for inc in range(3):
                        card1 = total.pop(0)
                        self.deck_of_player.append(card1)
    
    def distribute_again(self):
        if len(self.deck_of_player) == 0:
            t_b = []
            total = copy_total
            random.shuffle(total)
            for i in range(7):
                card1 = total.pop(0)
                self.deck_of_player.append(card1)
                card_table = total.pop(0)
            t_b.append(card_table)
        
        
    # def prueba(self):
    #     print(self.deck_of_player)
    #     colors_spe = ['Blue', 'Red', 'Yellow','Green']
    #     take = (input("Dite algo:"))
    #     take = [take]
    #     count_m = 0
    #     if (take) != ['']:
    #         index = self.deck_of_player.index(take)
    #         for r_c in self.deck_of_player:
    #             if len(r_c) != 1:
    #                 if r_c[0] in t_b[-1] or r_c[1] in t_b[-1]:
    #                     print("You have card to play")
    #                     print("Remember, you only can play that card, if don't have more")
    #                     count_m = 1
                        
    #         if count_m == 0:
    #             if count == len(players)- 1:
    #                 t_b.append(take)
    #                 for search in total[0:4]:
    #                     for r in range(0,1):
    #                         buck = total.pop(r)
    #                         players[0].deck_of_player.append(buck)
    #                 intro_c = input("Enter the color of deck:")
    #                 for bus in colors_spe:
    #                     if bus in intro_c:
    #                         t_b.append([intro_c,intro_c])
    #             else:
    #                 if count != len(players)- 1:
    #                     for search in total[0:4]:
    #                         for r in range(0,1):
    #                             buck = total.pop(r)
    #                             players[count +1].deck_of_player.append(buck)
    #                     intro_c = input("Enter the color of deck:")
    #                     for bus in colors_spe:
    #                         if bus in intro_c:
    #                             t_b.append([intro_c, intro_c])

















while len(players) < len(PlayerList):
    for call in range(0, len(PlayerList)):
        player = Players(PlayerList[call])
        players.append(player)

for all_player in players:
    all_player.Distribute_of_deck()
    


while True:
    if global_cont ==1:
        count = 0
        global_cont = 0
    # players[count].prueba()
    players[count].distribute_again()
    players[count].Play_game1()
    players[count].winner_of_player()
    players[count].distribute_again()
    players[count].PLay_game2()
    if count != len(PlayerList):
        count+=1
    if count == len(PlayerList):
        count = 0

