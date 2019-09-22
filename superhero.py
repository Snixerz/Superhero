import random

class Ability:
    def __init__(self, name, max_damange):
        self.name = name
        self.max_damange = max_damange
        self.attack_damage = random.randint(2, 7)
    def attack(self):
        print(self.attack_damage)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())    

