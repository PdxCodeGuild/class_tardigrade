class Cat:
    """Blueprints for cat object"""
    def __init__(self, name, lives, color):
        self.name = name
        self.lives = lives
        self.color = color
    
    def meow(self):
        print('meow')

    def talk(self):
        print(f"Hey I'm {self.name} the cat.  I have {self.lives} lives and I am {self.color}.")

    def __str__(self):
        return self.name

# instantiate a class (make an instance of the Cat class)
garfield = Cat('Garfield', 9, 'orange') # the Cat object is created
garfield.talk()
print(garfield)
# print(garfield.name) # .name is an attribute of a Cat object
# print(garfield.lives) # .lives is an attribute of a Cat object
# print(garfield.color) # .color is an attribute of a Cat object

# garfield.meow() # .meow is a method of a Cat object

heathcliff = Cat('Heathcliff', 7, 'orange')
heathcliff.talk()
print(heathcliff)
print(heathcliff.name) # .name is an attribute of a Cat object
print(heathcliff.lives) # .lives is an attribute of a Cat object
print(heathcliff.color) # .color is an attribute of a Cat object

# heathcliff.meow() # .meow is a method of a Cat object