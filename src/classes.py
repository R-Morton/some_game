class NPC:
    
    npc_dead = False
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, attacker):
        print(f"{attacker.name} deals 10 damage to {self.name}")
        self.health -= 10   
    

class Player(NPC):

    def __init__(self, name, health):
        super().__init__(name, health)

    def player_death(self):
        print("Player died")
