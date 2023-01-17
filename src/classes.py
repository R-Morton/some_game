import random
class NPC:

    def __init__(self, name, endurance, strength, agility, luck, health):
        self.name = name
        self.endurance = endurance
        self.strength = strength
        self.agility = agility
        self.luck = luck
        self.health = health + (endurance * 10)
        self.dodge_chance = agility * 3
        self.crit_chance = 5 + (luck * 2)
    

    def attack(self, attacker):
        damage = 10 + (attacker.strength)
        print(f"{self.name} has a {self.dodge_chance}% chance to dodge")
        print(f"{self.name} has a {self.crit_chance}% chance to criticaly hit")
        if self.dodge_chance_func() == True:
            print(f"{self.name} dodged the attack")
        elif self.crit_chance_func() == True:
            print("Critical hit!")
            print(f"{attacker.name} deals {damage * 2} damage to {self.name}")
            self.health -= damage * 2
        else:
            print(f"{attacker.name} deals {damage} damage to {self.name}")
            self.health -= damage
    
    def dodge_chance_func(self):
        if random.randint(1, 100) <= self.dodge_chance:
            return True
    
    def crit_chance_func(self):
        if random.randint(1, 100) <= self.crit_chance:
            return True



class Player(NPC):

    def __init__(self, name, endurance, strength, agility, luck, health):
        super().__init__(name, endurance, strength, agility, luck, health)

