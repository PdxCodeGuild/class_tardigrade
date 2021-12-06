import random

class Dog:
    """Represents a dog"""
    
    def __init__(self, name, ears, breed, color, needs_to_be_walked, size):
        self.name = name
        self.ears = ears
        self.breed = breed
        self.color = color
        self.needs_to_be_walked = needs_to_be_walked
        self.size = size

    species = 'Canis familiaris'

    def bark(self):
        if self.size == 'small':
            print('arf')
        elif self.size == 'medium':
            print('ruff')
        elif self.size == 'large':
            print('bark')

    def roll_over(self):
        if random.random() > 0.5:
            print(f'{self.name} rolled over. good boy!')
        else:
            print(f'{self.name} didn\'t roll over. still a good boy!')

    def __str__(self):
        return f'{self.name}, a {self.breed}'

    def __eq__(self, other):
        """how to evaluate dog_instance1 == dog_instance2"""
        # other is another dog
        if self.size == other.size:
            return True
        else:
            return False
    
    def __lt__(self, other):
        """how to evaluate dog1 < dog2"""
        if self.size == 'small':
            if other.size in ('medium', 'large'):
                return True
        if self.size == 'medium':
            if other.size == 'large':
                return True
        return False
    
    # other comparison dunder (double underscore) methods:
    # __gt__, __gte__, __lte__


# instantiate an instance of the Dog class
rocky = Dog('Rocky', 'small and pointy', 'yorkie', 'black and brown', False, 'small')
print(rocky)
rocky.bark()

kaner = Dog('Kaner', 'floppy', 'mutt', 'brown', True, 'medium')
print(kaner)
kaner.bark()

clifford = Dog('Clifford', 'big and floppy', 'bloodhound', 'red', True, 'large')
print(clifford)
clifford.bark()

billie = Dog('Billie', 'small and pointy', 'westie', 'white', False, 'small')

dogs = [rocky, kaner, clifford]

for dog in dogs:
    dog.roll_over()

print(rocky == kaner)
print(rocky == billie)

for dog in dogs:
    print()
    print(dog)
    print(billie < dog)