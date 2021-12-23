import random

students = [
    'dart',
    'alnardo',
    'dustin',
    'vanessa',
    'christian',
    'auriel',
    'travis',
    'lujock',
    'shad',
]


"""
V1: prints a random student name and then terminates
"""

# print(random.choice(students))

# student = random.choice(students)
# print(student)

"""
V2: cycle through the names in a random order
"""

random.shuffle(students)

for student in students:
    end_loop = input(student)
    if end_loop:
        break