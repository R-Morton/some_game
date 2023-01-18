import weapons
from classes import *
import os
from time import sleep
from player_import import player

def shopping():
    while True:
        os.system('cls')
        print(f"Your gold {player.gold}")
        print("1 - Weapons merchant")
        print("2 - Armour merchant")
        user_input = input("Please Select Option")
        match user_input:
            case "1":
                weapon_merchant()
        break

def weapon_merchant():
    while True:
        print("Buy/Sell")
        print("Go Back")
        user_input = input("Please Select Option: ")
        match user_input:
            case "1":
                os.system('cls')
                items = []
                while True:
                    count = 1
                    os.system("cls")
                    for key in iron_weapons.items():
                        print(f'{count} - {key[0]}')
                        items.append(key)
                        count += 1
                    print(f"{count} - Go back")
                    user_input2 = int(input("Select Item to buy or go back: "))
                    selection = 1
                    break
                for weapons in items:
                    if user_input2 == selection:
                        print(player.equipped_weapon)
                        print(type(player.equipped_weapon))
                        print(f"You have selected {weapons}")
                        player.equipped_weapon = weapons
                        print(player.equipped_weapon)
                        print(type(player.equipped_weapon))
                        sleep(3)
                        break
                    else:
                        selection += 1
                        continue



#weapon_merchant()
#print(player.damage)