import random
from weapons import *


class NPC:

    def __init__(self, name, endurance, strength, agility, luck, blade, blunt, level, health):
        self.name = name
        self.endurance = endurance
        self.strength = strength
        self.agility = agility
        self.luck = luck
        self.level = level
        self.level_exp = 0
        self.level_max_exp = 100 + (level * 10)
        self.blade = blade
        self.blade_exp = 0
        self.blade_max_exp = 100 + (blade * 10)
        self.blunt = blunt
        self.blunt_exp = 0
        self.blade_max_exp = 100 + (blunt * 10)
        self.health = health
        self.max_health = self.health + (endurance * 10)
        self.dodge_chance = agility * 4
        self.crit_chance = 5 + (luck * 2)
        self.block_chance = 15 + (endurance * 3)
        self.max_stamina = 100 + (agility * 5)
        self.stamina = self.max_stamina
        self.equipped_weapon = ('iron sword', [0, 2, 100])
        self.damage = 5 + (strength + self.equipped_weapon[1][1])
        self.equipped_chest = ('nothing', [2, 0, 0])
        self.equipped_legs = ('nothing', [2, 0, 0])
        self.equipped_hands = ('nothing', [2, 0, 0])
        self.equipped_head = ('nothing', [2, 0, 0])
        self.equipped_feet = ('nothing', [2, 0, 0])
        self.armor_rating = self.equipped_chest[1][0] + self.equipped_legs[1][0] + self.equipped_hands[1][0] + self.equipped_head[1][0] + self.equipped_feet[1][0]




class Player(NPC):
    
    def __init__(self, name, endurance, strength, agility, luck, blade, health):
        super().__init__(name, endurance, strength, agility, luck, blade, health)
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

    def weapon_skill_leveling(self):
        player_skill = self.equipped_weapon[1][0]
        match player_skill:
            case 0:
                self.blade_exp += 10
                print(self.blade_exp)
                if self.blade_exp >= self.blade_max_exp:
                    self.blade_exp = 0 + (self.blade_exp - self.blade_max_exp)
                    self.blade += 1
                    self.general_leveling(20)
                    print(f'Your blade skill has leveled up to {self.blade}')
                return
            case 1:
                pass
    def general_leveling(self, amount):
        self.level += amount
        if self.level >= self.level_max_exp:
            self.blade_exp = 0 + (self.level_exp - self.level_max_exp)
            self.level += 1
            print(f"You have leveled up!")
