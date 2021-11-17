"""Booleans"""
"""and"""

print(True and True) # True
print(True and False) # False
print(True and True and True and True) # True
print(True and False and True and True and True) # False

"""or"""
print(True or True) # True
print(False or False) # False
print(False or False or True or False) # True
print(False or False or False or False or False or False or False or False or False or False or True) # True

"""not"""
print(not True) # False
print(not False) # True
print(not True or not False) # True


"""Comparisons"""
print(1 > 5) # False
print(1 >= 1) # True

print(1 < 0 or 5 > 1) # True
    # False or True


"""Shorthand"""
print(5 > 1 and 1 > 0) # True
print(5 > 1 > 0) # True

print(5 == 5 == 5)
print((5 == 5) == 5)
print(True == 5)

"""in & not in"""

colors = ['red', 'green', 'blue']
print('red' in colors) # True
print('yellow' in colors) # False
print('red' not in colors) # False
print('yellow' not in colors) # True

"""is & is not"""

print(1 is 1) # True
colors2 = ['red', 'green', 'blue']
print(colors == colors2) # True
print(colors is colors2) # False
colors3 = colors
print(colors is colors3) # True
print(id(colors), id(colors2), id(colors3))

"""Conditionals"""
"""if, elif, else"""
import random


temperature = random.randint(0, 100)
print('temperature: ' + str(temperature))

if temperature < 40:
    print('cold')
elif temperature < 80:
    print('warm')
else:
    print('hot')

temperature = random.randint(50, 100)
print('temperature: ' + str(temperature))

if temperature < 60:
    print('cold')
elif temperature < 70:
    print('warm')
elif temperature < 80:
    print('pretty warm')
elif temperature < 90:
    print('hot')
else:
    print("wow it's so hot!")


"""short-circuited evaluation"""
print(True and True and False and True and True) # False
#                       ^   ^
# doesn't need to check after seeing the first False

print(False or False or True or False or True) # True
#                       ^  ^
# doesn't need to check after seeing the first True

print(True and False and True or False or True) # True
print(False or False or True) # True

"""shorthand or one-line conditionals"""

temperature = 75
forecast = 'warm' if temperature > 70 else 'cold'
print(temperature, forecast)

temperature = 65
forecast = 'warm' if temperature > 70 else 'cold'
print(temperature, forecast)


"""Truthy and Falsey"""
"""
Falsey Values:
'', 0, [], None, {}, 0.0
"""
if 'hello':
    print('hello is truthy')
if '':
    print('empty strings are truthy')
else:
    print('empty strings are falsey')

if 1:
    print('1 is truthy')
if 0:
    print('0 is truthy')
else:
    print('0 is falsey')

if ['things', 'other things']:
    print('this list is truthy')
if []:
    print('empty lists are truthy')
else:
    print('empty lists are falsey')

if {'a': 1, 'b': 2}:
    print('non-empty dictionaries are truthy')
if {}:
    print('empty dictionaries are truthy')
else:
    print('empty dictionaries are falsey')

inputs = [1, None, 4, None, 3, 0, 5]
# all inputs should be numbers, if None do not process!
for input in inputs:
    if input:
        print(f'input {input} successfully processed')
error = ''
for input in inputs:
    if input is not None:
        print(f'input {input} successfully processed')
    else:
        error += 'invalid input entered, '
if error:
    print('errors occured: ' + error)

# if error != ''