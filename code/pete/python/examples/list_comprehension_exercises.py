"""
EXERCISE 1
Translate for loop to list comprehension
"""
hats = ['baseball cap', 'fedora', 'derby', 'panama']

for hat in hats:
	print(hat)

# list comprehension version...
nones = [print(hat) for hat in hats]
print(nones) # [None, None, None, None]


"""
EXERCISE 2
Translate for loop to list comprehension
"""
dogs = ['pluto', 'fido', 'clifford', 'lassie']
dog_facts = []
for dog in dogs:
	dog_facts.append(f"{dog.capitalize()} is a good boy.")
print(dog_facts)

# list comprehension version...
dog_facts = [f"{dog.capitalize()} is a good boy." for dog in dogs]
print(dog_facts)


"""
EXERCISE 3
Translate for loop to list comprehension
"""
numbers = [1, 238, 74, 364, 65, 23, 765]
evens = []
odds = []
for number in numbers:
	if number % 2 == 0:
		evens.append(number)
	else:
		odds.append(number)
# list comprehension version
evens = [number for number in numbers if number % 2 == 0]

print(evens)
odds = [number for number in numbers if number % 2 == 1]
print(odds)


"""
EXERCISE 4
Translate for loop to list comprehension
"""
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
fall = ['september', 'october', 'november']
winter = ['december', 'january', 'febuary']
seasons2d = [spring, summer, fall, winter]

for season in seasons2d:
    # print(season)
    for month in season:
        print(month)

# list comprehension version...
# [print(season) for season in seasons2d]
[[print(month) for month in season] for season in seasons2d]
