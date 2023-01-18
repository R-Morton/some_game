import random
from weapons import *


class NPC:

    def __init__(self, name, endurance, strength, agility, luck, health):
        self.name = name
        self.endurance = endurance
        self.strength = strength
        self.agility = agility
        self.luck = luck
        self.health = health
        self.max_health = self.health + (endurance * 10)
        self.dodge_chance = agility * 4
        self.crit_chance = 5 + (luck * 2)
        self.block_chance = 15 + (endurance * 3)
        self.max_stamina = 100 + (agility * 5)
        self.stamina = self.max_stamina
        self.equipped_weapon = ('iron sword', [2, 100])
        self.damage = 5 + (strength + self.equipped_weapon[1][0])



class Player(NPC):
    
    def __init__(self, name, endurance, strength, agility, luck, health):
        super().__init__(name, endurance, strength, agility, luck, health)
        self.gold = 0

    def defensive_block(self):
        self.block_chance *= 2
        self.dodge_chance /= 2


    def reverse_defensive_block(self):
        self.block_chance /= 2
        self.dodge_chance *= 2

    def normal_stance(self):
        self.dodge_chance *= 2
    
    def reverse_normal_stance(self):
        self.dodge_chance /= 2

