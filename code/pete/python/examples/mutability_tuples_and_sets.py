"""Mutability"""

# mutable types: lists, dictionaries, sets, most other objects
nums = [1, 2, 3, 4, 5] 
print(id(nums)) # 4516792704
nums.append(6)
print(id(nums)) # 4516792704 same id as before
print(nums) # [1, 2, 3, 4, 5, 6]

teacher = {'name': 'pete', 'favorite_food': 'pizza'}
print(id(teacher)) # 4515262720
teacher['favorite_food'] = 'thai'
print(id(teacher)) # 4515262720 same id as before
print(teacher) # {'name': 'pete', 'favorite_food': 'thai'}

# immutable types: integers, floats, strings, tuples
number = 1
print(id(number)) # 4514269488
number += 1
number = number + 1
print(id(number)) # 4514269520 different id than before
print(number) # 3

message = 'welcome to class'
print(message, id(message)) # welcome to class 4492042928
message += '!' # message = message + '!'
print(message, id(message)) # welcome to class! 4492042848
titled_message = message.title()
print(message, id(message)) # welcome to class! 4492042848
print(titled_message, id(titled_message)) # Welcome To Class! 4492043088

"""Tuples"""
# tuples are like lists but immutable, they cannot be changed in any way
# after being declared

seasons = ('spring', 'summer', 'fall', 'winter')
print(id(seasons)) # 4335021008
try:
    seasons.append('the fifth season')
except AttributeError as e:
    print(e)

try:
    seasons[2] = 'autumn'
except TypeError as e:
    print(e)

seasons = ('spring', 'summer', 'autun', 'winter')
print(id(seasons)) # 4335056512

"""Sets"""
# sets are like lists but every object is unique
set1 = {1, 2, 3, 2, 1}
print(set1) # {1, 2, 3}

# set2 = {1, 2, 3, [1, 2, 3], [1, 2, 3]} # TypeError: unhashable type: 'list'

# unhashable type
# test = {[1]: 1} # TypeError: unhashable type: 'list'

# set1.union(set2)

some_months = {'december', 'october', 'january'}
some_other_months = {'february', 'december', 'june'}
still_not_all_the_months = some_months.union(some_other_months)
print(still_not_all_the_months) # {'january', 'june', 'february', 'october', 'december'}

intersection = some_other_months.intersection(some_months)
print(intersection) # {'december'}