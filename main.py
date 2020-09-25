from players import Player
from game import  Game
from os import system

game = Game()
game.create_players()


for all_player in game.players:
    all_player.distribute_of_deck()

while game.players[game.count].score != 500:
    if game.players_direction == 1:
        game.count = 0
        game.players_direction = 0
    game.players[game.count].play_game()
    game.check_compatibility()
    game.add_ability()
    game.win_player()
    game.count+=1
    if game.count == len(game.players):
        game.count = 0
