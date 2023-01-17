import random
class NPC:

    def __init__(self, name, endurance, strength, agility, luck, health):
        self.name = name
        self.endurance = endurance
        self.strength = strength
        self.agility = agility
        self.luck = luck
        self.health = health + (endurance * 10)

    def attack(self, attacker):
        damage = 10 + (attacker.strength)
        print(f"{self.name} has a {self.agility * 3}% chance to dodge")
        if self.dodge_chance() == True:
            print(f"{self.name} dodged the attack")
        else:
            print(f"{attacker.name} deals 10 damage to {self.name}")
            self.health -= damage
    
    def dodge_chance(self):
        dodge_chance = self.agility * 3
        if random.randint(1, 100) <= dodge_chance:
            return True



class Player(NPC):

    player_damage = 0

    def __init__(self, name, endurance, strength, agility, luck, health):
        super().__init__(name, endurance, strength, agility, luck, health)

