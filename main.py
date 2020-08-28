from players import Players, count, players, name_list, global_verify



while len(players) < len(name_list):
    for call in range(0, len(name_list)):
        player = Players(name_list[call])
        players.append(player)

for all_player in players:
    all_player.distribute_of_deck()



while players[count].score != 500:    
    if global_verify == 1:
        count = 0
        global_verify = 0
    players[count].distribute_again()
    players[count].play_game()
    players[count].win_player()
    players[count].distribute_again()
    if count != len(name_list):
        count+=1
    if count == len(players):
        count = 0


    if __name__ == '__main__':
        'main'()
        