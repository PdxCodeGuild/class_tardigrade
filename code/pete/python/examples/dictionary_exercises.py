miles_morales = {
    'superhero': 'Spider-Man',
    'age': 17,
    'home': 'New York City',
    'family': ['Jefferson Davis', 'Rio Morales'],
    'occupation': 'student'
}

"""
Access: dict[key] or dict.get(key)
Access the 'superhero' key to print Miles' superhero name
"""
print(miles_morales['superhero'])
print(miles_morales.get('superhero'))
# print(miles_morales['supervillain']) # KeyError
print(miles_morales.get('supervillain')) # None
print(miles_morales.get('supervillain', 'not a supervillain')) # 'not a supervillain'

"""
Update: dict[key] = value
Happy Birthday Miles 🎂
Increase Miles' age by 1
"""
miles_morales['age'] += 1
# miles_morales['age'] = miles_morales['age'] + 1
# miles_morales['occupation'] = 'superhero'
print(miles_morales)

"""
Add Miles' uncle, Aaron Davis, to the family value
"""
miles_morales['family'].append('Aaron Davis')

print(miles_morales) # dictionary
print(miles_morales['family']) # list
print(miles_morales['family'][2]) # string



"""
Add key/value pair: dict[key] = value
Add more info to the miles_morales dictionary
"""
miles_morales['love_interest'] = 'Gwen Stacy'
miles_morales['allies'] = ['Peter Parker', 'Spider-Pig']
miles_morales['allies'].append('Gwen Stacy')
miles_morales['enemies'] = ['Kingpin', 'Doc Oct', 'Green Goblin', 'The Prowler']

print(miles_morales)

"""dict.keys()"""
keys = miles_morales.keys()
for key in keys:
    print()
    print(key, miles_morales[key])

"""dict.values()"""
print(miles_morales.values())

"""dict.items()"""
# print(miles_morales.items())
for key_value_pair in miles_morales.items():
    print(key_value_pair)