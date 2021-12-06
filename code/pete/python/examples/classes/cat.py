# python uses snake_case for most variables
# but uses PascalCase for classes
# javascript uses camelCase
# html uses kebab-case

import random

cat_dict = {'name': 'Garfield', 'color': 'orange', 'lives': 9}

# declare a new class with the class keyword
class Cat:
    """Represents a cat"""
    # create methods of the class with the def keyword, like functions
    # the __init__ is the initializer, it runs when you first create
    # a Cat object
    def __init__(self, name, color, lives=9):
        # the following are instance attributes
        self.name = name
        self.color = color
        self.lives = lives
    
    # class attributes belong to each instance of the class
    species = 'Felis catus'
    
    # methods are called off the object: cat.meow()
    def meow(self):
        print('meow')
    
    def give_bio(self):
        # you can reference attributes within methods &
        # you can call methods within other methods
        self.meow()
        print(f"""My name is {self.name}.
I am a {self.color} cat.
I have {self.lives} lives.""")
        self.meow()

    def climb_curtains(self):
        if self.lives < 3:
            print(f'"I\'m getting to old for that", said {self.name}.')
            return
        if random.random() > 0.25:
            print(f'{self.name} successfully climbed the curtains')
            return
        print('ouch')
        self.lives -= 1
        print(f'{self.name} fell climbing the curtains.  {self.lives} lives remaining.')
        

    # the __str__ method tells the object how to print itself out
    def __str__(self):
        return self.name

# instantiate, or make an instance of, the Cat object
garfield = Cat('Garfield', 'orange and black')
heathcliff = Cat('Heathcliff', 'orange', 7)
felix = Cat('Felix', 'black', 4)

cats = [garfield, heathcliff, felix]

for _ in range(10):
    for cat in cats:
        print()
        cat.climb_curtains()

# for cat in cats:
#     print()
#     cat.give_bio()

# print(garfield, type(garfield))
# print(cat_dict, type(cat_dict))
# garfield.color is the color attribute of the Cat object: garfield
# print(cat_dict['color'], garfield.color)

garfield.meow()

# print(f"""{garfield} and {heathcliff} are friends.
# {garfield} has {garfield.lives} lives.
# {heathcliff} has {heathcliff.lives} lives.""")

# instance attributes vs Class attributes
print(Cat.species, garfield.species)
# print(Cat.lives) # AttributeError only instances have the lives attribute