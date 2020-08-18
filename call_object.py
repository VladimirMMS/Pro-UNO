from players import Players, count, players, PlayerList, global_cont
from Win import *



while len(players) < len(PlayerList):
    for call in range(0, len(PlayerList)):
        player = Players(PlayerList[call])
        players.append(player)

for all_player in players:
    all_player.Distribute_of_deck()
    


while players[count].score != 500:
    if global_cont ==1:
        count = 0
        global_cont = 0
    players[count].distribute_again()
    players[count].PLay_game1()
    players[count].winner_of_player()
    players[count].distribute_again()
    if count != len(PlayerList):
        count+=1
    if count == len(PlayerList):
        count = 0