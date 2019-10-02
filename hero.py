import random

class Ability():
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        return random.randint(0, self.attack_strength)

class Armor():
    def __init__(self, name, max_block=20):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

class Hero():
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health
        self.abilities = []
        self.armors = []

    def add_ability(self, ability):
        return self.abilities.append(ability)

    def add_armor(self, armor):
        return self.armors.append(armor)

    def attack(self):
        attack_value = 0
        for ability in self.abilities:
            attack_value += ability.attack()
        return attack_value

    def defend(self, damage_amt):
        defended = damage_amt
        for armor in self.armors:
            defended += armor.block()
        return defended

    def take_damage(self, damage_amt):
        self.current_health -= self.defend(damage_amt)
        
    def is_alive(self):
        if self.current_health <= 1:
            return False
        else:
            return True
        pass

    def fight(self, opponent):
        while self.current_health >= 0 and opponent.current_health >= 0:
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if self.current_health < 0:
            print(self.name, "won!")
        else:
            print(opponent.name, "won!")

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        attack1 = self.attack_strength//2
        attack2 = self.attack_strength

        return random.randint(attack1, attack2)
        
class Team(Hero):
    def __init__(self, name):
        ''' Initialize your team with its team name
    '''
    # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
        self.name = name
        self.heros =[]
    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        ''' 
        if (len(self.heros) == 0):
            return 0
        else:
            for hero in self.heros:
                if hero.name == self.name:
                    self.heros.remove(name)
    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # TODO: Loop over the list of heroes and print their names to the terminal.
        for i in self.heros:
            print(i)


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
