import random
"""Lists"""
numbers = [1, 4, 8, 2, 87, 32, 65]
random.shuffle(numbers)

odds = []
for n in numbers:
    if n % 2 == 1:
        odds.append(n)

print(numbers)
print(odds)

evens = [n for n in numbers if n % 2 == 0] # conditionals at the end of the
# list comprehension will either append or not append the item

evens_or_Nones = [n if n % 2 == 0 else None for n in numbers] # conditionals at
# the start of the list comprehension will result in different values being
# appended to the list

numbers_2 = [n for n in numbers]

print(evens_or_Nones)
# print(evens, numbers_2)

# print([i for i in range(20)])