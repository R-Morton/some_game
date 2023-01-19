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
        user_input = input("Please Select Option: ")
        match user_input:
            case "1":
                weapon_merchant()
            case "2":
                armour_merchant()
        break

def weapon_merchant():
    while True:
        os.system("cls")
        print("Buy/Sell")
        print("Go Back")
        user_input = input("Please Select Option: ")
        os.system('cls')
        match user_input:
            case "1":
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
                        print(f"{weapons[0]} has been equipped")
                        player.equipped_weapon = weapons
                        sleep(3)
                        break
                    else:
                        selection += 1
                        continue
            case "2":
                return

def armour_merchant():
    while True:
        os.system("cls")
        print("Buy/Sell")
        print("Go Back")
        user_input = input("Please Select Option: ")
        os.system("cls")
        match user_input:
            case "1":
                items = []
                while True:
                    count = 1
                    os.system("cls")
                    for key in leather_armour.items():
                        print(f'{count} - {key[0]}')
                        items.append(key)
                        count += 1
                    for key in iron_armour.items():
                        print(f'{count} - {key[0]}')
                        items.append(key)
                        count += 1
                    print(f"{count} - Go back")
                    user_input2 = int(input("Select Item to buy or go back: "))
                    selection = 1
                    break
                for armour in items:
                    if user_input2 == selection:
                        armour_slot = armour[1][1]
                        print(f"{armour[0]} has been equipped")
                        sleep(3)
                        match armour_slot:
                            case 0:
                                player.equipped_chest = armour
                            case 1:
                                player.equipped_legs = armour
                            case 2:
                                player.equipped_hands = armour
                            case 3:
                                player.equipped_head = armour
                            case 4:
                                player.equipped_feet = armour
                            case 5:
                                player.equipped_shield = armour
                        break
                    else:
                        selection += 1
                        continue
            case "2":
                return


#weapon_merchant()
#print(player.damage)