class Character:
    def __init__(self, name, species, klass, health_points = 100, attack_points = 10):
        self.name = name
        self.species = species
        self.klass = klass
        self.health_points = health_points
        self.attack_points = attack_points
        self.alive = True

    def attack(self, other):
        """self attacks other, reducing other's health_points
        by self's attack_points"""
        print(f'{self.name} attacks {other.name}')
        other.take_damage(self.attack_points)
        # other.health_points -= self.attack_points

    def take_damage(self, damage):
        print(f'{self.name} takes {damage} damage')
        self.health_points -= damage
        self.hp_check()

    def hp_check(self):
        """If character is out of health_points,
        character dies"""
        if self.health_points <= 0:
            self.health_points = 0
            self.alive = False
            print(f'{self.name} has died.')
    
    def __repr__(self):
        return f"Character('{self.name}', '{self.species}', '{self.klass}', {self.health_points}, {self.attack_points})"

    def __str__(self):
        return f'{"-"*40}\n{self.klass} {self.name}\nHP: {self.health_points}\n{"-"*40}'
    
arthur = Character('Arthur', 'human', 'King', attack_points=15)
morgan = Character('Morgan La Fey', 'humna', 'Witch', 85, 23)
lancelot = Character('Lancelot', 'human', 'Knight')

print(repr(lancelot))

# import time

# i = 0
# fighters = [arthur, lancelot]
# while lancelot.alive == True and arthur.alive == True:
#     fighter1 = fighters[i % len(fighters)]
#     fighter2 = fighters[(i + 1) % len(fighters)]
#     fighter1.attack(fighter2)
#     time.sleep(1)
#     print(fighter2)
#     time.sleep(1)
#     i += 1

# print(arthur)
# print(morgan)

# arthur.attack(morgan)

# for i in range(10):
#     print(arthur)
#     morgan.attack(arthur)
#     if arthur.alive == False:
#         print('arthur died')
#         break

# print(arthur)