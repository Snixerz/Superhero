import random

class Ability:
    def __init__(self, name, max_damange):
        self.name = name
        self.max_damange = max_damange
        self.attack_damage = random.randint(2, 7)
    def attack(self):
        return self.attack_damage

class Armor: 
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = random.randint(0, 7)
    def block(self):
        return self.max_block
class Hero:
    def __init__(self, name, current_health, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = current_health

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    armor = Armor("Shield", 7)
    my_hero = Hero("Grace Hopper", 200)
    print(ability.name)
    print(ability.attack())
    print(armor.block())
    print(my_hero.name)
    print(my_hero.current_health)
