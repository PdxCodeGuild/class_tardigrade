# Exercise 1

# teachers = [
#     {
#         'name': 'Pete',
#         'city': 'Portland',
#         'job': 'programmer',
#         'computer': 'Mac',
#     },
#     {
#         'name': 'Lisa',
# 		'city': 'Portland',
# 		'job': 'programmer',
# 		'computer': 'windows',
# 		'cat': 'Heather'
#     },
# ]
# keys = ['name', 'city', 'job', 'computer', 'cat']
# for teacher in teachers:
#     for key in keys:
#         try:
#             print(f'Their {key} is {teacher[key]}')
#         except KeyError:
#             print(f'They have no {key}')
#     print()


# Exercise 2


def add(x, y):
    return int(x) + int(y)


test_inputs = [
    (2, 2),
    ('2', '2'),
    (2, '2'),
    ('two', 2),
]

for nums in test_inputs:
    try:
        result = add(nums[0], nums[1])
        print(result)
    except (TypeError, ValueError) as e:
        print(nums, 'error occured', e)
