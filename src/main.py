from classes import *
import os
from time import sleep
import random
import merchants
from player_import import player
npc = NPC("Noob", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0)

def main_screen():
    while True:
        os.system('cls')
        print("1: Fight opponent")
        print("2: Go Shopping")
        print("3: View Stats")
        print("4: View Equipment")
        print("5: Developer Tools")
        print("6: Save/Exit")
        user_input = input("Select an option: ")
        match user_input:
            case '1':
                fight()
            case '2':
                merchants.shopping()
            case '3':
                view_stats()
            case '4':
                view_equipment()
            case '5':
                developer_tools()
            case '6':
                save_exit()
                os.system('exit')


def view_stats():
    while True:
        os.system('cls')
        print(f"Health - {player.max_health}")
        print(f"Stamina - {player.max_stamina}")
        print(f"Level - {player.level} ({player.level_exp}/{player.level_max_exp}) \n")
        print("Major Stats")
        print(f"Strength - {player.strength}")
        print(f"Endurance - {player.endurance}")
        print(f"Agility - {player.agility}")
        print(f"Luck - {player.luck} \n")
        print("Weapons Skills")
        print(f"Blade - {player.blade} ({player.blade_exp}/{player.blade_max_exp})")
        print(f"Blunt - {player.blunt} ({player.blunt_exp}/{player.blunt_max_exp})")
        print(f"Light - {player.light} ({player.light_exp}/{player.light_max_exp})")
        print(f"Heavy - {player.heavy} ({player.heavy_exp}/{player.heavy_max_exp})")
        print(f"Block - {player.block} ({player.block_exp}/{player.block_max_exp}) \n")
        input("Press enter to go back")
        break

def view_equipment():
    while True:
        os.system('cls')
        print("Armour")
        print(f"Head - {player.equipped_head[0]} ({player.equipped_head[1][2]} - armour)")
        print(f"Chest - {player.equipped_chest[0]} ({player.equipped_chest[1][2]} - armour)")
        print(f"Hands - {player.equipped_hands[0]} ({player.equipped_hands[1][2]} - armour)")
        print(f"Legs - {player.equipped_legs[0]} ({player.equipped_legs[1][2]} - armour)")
        print(f"Feet - {player.equipped_feet[0]} ({player.equipped_feet[1][2]} - armour) \n")
        print("Weapons/Shield")
        print(f"Weapon - {player.equipped_weapon[0]} ({player.equipped_weapon[1][1]} - damage)")
        print(f"Shield - {player.equipped_shield[0]} ({player.equipped_head[1][2]} - block rating) \n")
        input("Press enter to go back")
        break

def save_exit():
    save_info = f"{player.name} {player.endurance} {player.strength} {player.agility} {player.luck} {player.blade} {player.blunt} {player.light} {player.heavy} {player.block} {player.level} {player.blade_exp} {player.blunt_exp} {player.light_exp} {player.heavy_exp} {player.block_exp} {player.level_exp}"
    with open("player_save.txt", "w") as f:
        f.write(save_info)
        return

def fight():
    while True:
        os.system('cls')
        display_health_stamina()
        print("1 - Light Attack")
        print("2 - Heavy Attack")
        print("3 - Defensive Stance")
        print("4 - Normal Stance")
        user_input = input("Choose an option: ")
        match user_input:
            case "1":
                if player.stamina < 15:
                    print("Not enough Stamina")
                    sleep(2)
                    os.system('cls')
                else:
                    attack(npc, player, 'light')
                    if death_checker() == True:
                        break
                    attack(player, npc, 'light')
                    if death_checker() == True:
                        break
            case "2":
                if player.stamina < 40:
                    print("Not enough Stamina")
                    sleep(2)
                    os.system('cls')
                else:
                    attack(npc, player, 'heavy')
                    if death_checker() == True:
                        break
                    attack(player, npc, 'light')
                    if death_checker() == True:
                        break
            case "3":
                defensive_stance(player)
                if death_checker() == True:
                    break
            case "4":
                normal_stance(player)
                if death_checker() == True:
                    break


def death_checker():
    if player.health <= 0:
            print(f"{player.name} died")
            return True
    elif npc.health <= 0:
        print(f"{npc.name} died")
        sleep(3)
        npc.health = npc.max_health
        player.health = player.max_health
        player.stamina = player.max_stamina
        player.gold += 50
        player.general_leveling(20)
        return True

def display_health_stamina():
    print(f"{npc.name} health - {npc.health}")
    #print(f"{npc.name} stamina - {npc.stamina}")
    print(f"{player.name} health - {player.health}")
    print(f"{player.name} stamina - {player.stamina} \n")

def attack(self, attacker, type):
    damage = attacker.damage - (self.armor_rating / 10)
    attacker.stamina -= 15
    if attacker.equipped_weapon[1][0] == 0:
        damage = damage + (attacker.blade / 2)
    if attacker.equipped_weapon[1][0] == 1:
        damage = damage + (attacker.blunt / 2)
    if type == 'heavy':
        damage += (damage * 20/100)
        attacker.stamina -= 25
    os.system('cls')
    print(f"{attacker.name} uses {type} attack on {self.name}")
    sleep(2)
    if dodge_chance_func(self) == True:
        return
    if block_chance_func(self) == True:
        if self == player:
            player.skill_leveling(4)
        return
    elif crit_chance_func(attacker) == True:
        print(f"{attacker.name} deals {damage * 2} damage to {self.name}")
        if attacker == player:
            player.skill_leveling(player.equipped_weapon[1][0])
        elif self == player:
            player.skill_leveling(player.equipped_chest[1][0])
        sleep(2)
        os.system('cls')
        self.health -= damage * 2
        return
    else:
        print(f"{attacker.name} deals {damage} damage to {self.name}")
        if attacker == player:
            player.skill_leveling(player.equipped_weapon[1][0])
        elif self == player:
            player.skill_leveling(player.equipped_chest[1][0])
        self.health -= damage
        sleep(2)
        return

def defensive_stance(self):
    count = 0
    while self.stamina < self.max_stamina:
        count += 1
        if count == 31:
            break
        else:
            self.stamina += 1
    os.system('cls')
    print(f'{self.name} uses defensive stance')
    self.defensive_block()
    sleep(2)
    attack(self, npc, 'light')
    self.reverse_defensive_block()

def normal_stance(self):
    count = 0
    while self.stamina < self.max_stamina:
        count += 1
        if count == 51:
            break
        else:
            self.stamina += 1
    os.system('cls')
    print(f'{self.name} uses normal stance')
    self.normal_stance()
    sleep(2) 
    attack(self, npc, 'light')
    self.reverse_normal_stance()


def dodge_chance_func(self):
    if random.randint(1, 100) <= self.dodge_chance:
        print(f"Dodged! Due to {self.name}'s {self.dodge_chance}% chance")
        sleep(2)
        os.system('cls')
        return True

def crit_chance_func(self):
    if random.randint(1, 100) <= self.crit_chance:
        print(f"Critical hit! due to {self.name} {self.crit_chance}% chance")
        return True

def block_chance_func(self):
    if random.randint(1, 100) <= self.block_chance:
        print(f"Blocked! Due to {self.name}'s {self.block_chance}% chance")
        sleep(2)
        os.system('cls')
        return True
        
def developer_tools():
    while True:
        print("1 - +100 level exp")
        print("2 - Go back")
        user_input = input("Select option: ")
        match user_input:
            case "1":
                player.general_leveling(100)
                continue
            case "2":
                return
main_screen()

        