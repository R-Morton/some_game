from classes import *
import os

player = Player('Rhys', 100)
npc = NPC("Noob", 100)

def fight():
    while True:
        input("Press something to attack")
        os.system('clear')
        NPC.attack(npc, player)
        display_health()
        if death_checker() == True:
            break
        NPC.attack(player, npc)
        display_health()
        if death_checker() == True:
            break

def death_checker():
    if player.health <= 0:
            print(f"{player.name} died")
            return True
    elif npc.health <= 0:
        print(f"{npc.name} died")
        return True

def display_health():
    print(f"NPC health - {npc.health}")
    print(f"Player health - {player.health}")

fight()
        