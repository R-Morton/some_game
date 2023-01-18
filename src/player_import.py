from classes import *

with open("player_save.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        saved_player = line.split()
    player = Player(saved_player[0], int(saved_player[1]), int(saved_player[2]), int(saved_player[3]), int(saved_player[4]), 100)