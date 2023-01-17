from classes import *
import os
from time import sleep
import random

player = Player('Rhys', 2, 3, 2, 2, 100)
npc = NPC("Noob", 1, 1, 1, 1, 50)

def fight():
    while True:
        os.system('cls')
        display_health_stamina()
        print("1 - Light Attack")
        print("2 - Heavy Attack")
        print("3 - Defensive Stance")
        user_input = input("Choose an option")
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
        return True

def display_health_stamina():
    print(f"{npc.name} health - {npc.health}")
    print(f"{npc.name} stamina - {npc.stamina}")
    print(f"{player.name} health - {player.health}")
    print(f"{player.name} stamina - {player.stamina} \n")

def attack(self, attacker, type):
    damage = 10 + (attacker.strength)
    attacker.stamina -= 15
    if type == 'heavy':
        damage += (damage * 20/100)
        attacker.stamina -= 25
    os.system('clear')
    print(f"{attacker.name} uses {type} attack on {self.name}")
    sleep(2)
    if dodge_chance_func(self) == True:
        return
    if block_chance_func(self) == True:
        return
    elif crit_chance_func(attacker) == True:
        print(f"{attacker.name} deals {damage * 2} damage to {self.name}")
        sleep(2)
        self.health -= damage * 2
        return
    else:
        print(f"{attacker.name} deals {damage} damage to {self.name}")
        self.health -= damage
        sleep(2)
        return

def defensive_stance(self):
    self.stamina += 30
    print(f'{self.name} uses defensive stance')
    self.defensive_block()
    sleep(2)
    attack(self, npc, 'light')
    self.reverse_defensive_block()

def normal_stance(self):
    self.stamina += 50
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
        sleep(2)
        os.system('cls')
        return True

def block_chance_func(self):
    if random.randint(1, 100) <= self.block_chance:
        print(f"Blocked! Due to {self.name}'s {self.block_chance}% chance")
        sleep(2)
        os.system('cls')
        return True
        

fight()

        