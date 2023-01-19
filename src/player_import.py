from classes import *

with open("player_save.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        saved_player = line.split()
    player = Player(saved_player[0], int(saved_player[1]), int(saved_player[2]), int(saved_player[3]), int(saved_player[4]), int(saved_player[5]), int(saved_player[6]), int(saved_player[7]), int(saved_player[8]), int(saved_player[9]), int(saved_player[10]), int(saved_player[11]), int(saved_player[12]), int(saved_player[13]), int(saved_player[14]), int(saved_player[15]), int(saved_player[16]))