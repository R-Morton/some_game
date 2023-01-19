import random
from weapons import *


class NPC:

    def __init__(self, name, endurance, strength, agility, luck, blade, blunt, light, heavy, block, level):
        self.name = name
        self.endurance = endurance
        self.strength = strength
        self.agility = agility
        self.luck = luck
        self.level = level
        self.level_exp = 0
        self.level_max_exp = 90 + (level * 10)
        self.blade = blade
        self.blade_exp = 0
        self.blade_max_exp = 80 + (blade * 20)
        self.blunt = blunt
        self.blunt_exp = 0
        self.blunt_max_exp = 80 + (blunt * 20)
        self.light = light
        self.light_exp = 0
        self.light_max_exp = 80 + (light * 20)
        self.heavy = heavy
        self.heavy_exp = 0
        self.heavy_max_exp = 80 + (heavy * 20)
        self.block = block
        self.block_exp = 0
        self.block_max_exp = 80 + (block * 20)
        self.health = 100
        self.max_health = self.health + (endurance * 10)
        self.dodge_chance = agility * 4
        self.crit_chance = 5 + (luck * 2)
        self.block_chance = 10 + (endurance * 3) + self.equipped_shield[1][1]
        self.max_stamina = 100 + (agility * 5)
        self.stamina = self.max_stamina
        self.equipped_weapon = ('iron sword', [0, 2, 100])
        self.damage = 5 + (strength + self.equipped_weapon[1][1])
        self.equipped_chest = ('nothing', [5, 0, 0])
        self.equipped_legs = ('nothing', [5, 0, 0])
        self.equipped_hands = ('nothing', [5, 0, 0])
        self.equipped_head = ('nothing', [5, 0, 0])
        self.equipped_feet = ('nothing', [5, 0, 0])
        self.equipped_shield = ('nothing', [4, 0, 0])
        self.armor_rating = self.equipped_chest[1][1] + self.equipped_legs[1][1] + self.equipped_hands[1][1] + self.equipped_head[1][1] + self.equipped_feet[1][1]




class Player(NPC):
    
    def __init__(self, name, endurance, strength, agility, luck, blade, blunt, level):
        super().__init__(name, endurance, strength, agility, luck, blade, blunt, level)
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

    def skill_leveling(self):
        player_skill = self.equipped_weapon[1][0]
        match player_skill:
            case 0:
                self.blade_exp += 20
                if self.blade_exp >= self.blade_max_exp:
                    self.blade_exp = 0 + (self.blade_exp - self.blade_max_exp)
                    self.blade += 1
                    self.general_leveling(20)
                    print(f'Your blade skill has leveled up to {self.blade}')
                return
            case 1:
                self.blunt_exp += 10
                if self.blunt_exp >= self.blunt_max_exp:
                    self.blunt_exp = 0 + (self.blunt_exp - self.blunt_max_exp)
                    self.blunt += 1
                    self.general_leveling(20)
                    print(f'Your blunt skill has leveled up to {self.blunt}')
            case 2:
                self.light_exp += 10
                if self.light_exp >= self.light_max_exp:
                    self.light_exp = 0 + (self.light_exp - self.light_max_exp)
                    self.light += 1
                    self.general_leveling(20)
                    print(f'Your light skill has leveled up to {self.light}')
            case 3:
                self.heavy_exp += 10
                if self.heavy_exp >= self.heavy_max_exp:
                    self.heavy_exp = 0 + (self.heavy_exp - self.heavy_max_exp)
                    self.heavy += 1
                    self.general_leveling(20)
                    print(f'Your heavy skill has leveled up to {self.heavy}')
            case 4:
                self.block_exp += 10
                if self.block_exp >= self.block_max_exp:
                    self.block_exp = 0 + (self.block_exp - self.block_max_exp)
                    self.block += 1
                    self.general_leveling(20)
                    print(f'Your block skill has leveled up to {self.block}')

    def general_leveling(self, amount):
        self.level_exp += amount
        if self.level >= self.level_max_exp:
            self.blade_exp = 0 + (self.level_exp - self.level_max_exp)
            self.level += 1
            print(f"You have leveled up!")
