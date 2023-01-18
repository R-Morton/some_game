from classes import *
from player_import import player

def weapon_skill_leveling():
    player_skill = player.equipped_weapon[1][0]
    match player_skill:
        case 0:
            player.blade_exp += 10
            print(player.blade_exp)
            return
        case 2:
            pass

