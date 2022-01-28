# lists

colors = ['red', 'green', 'blue']
# list.append(element)
colors.append('yellow')

# for color in colors:
#     print(color)

# i = 0
# while i < len(colors):
#     print(colors[i])
#     i += 1








# dictionaries

# print(type(1), type('hello'), type([1,2,3]), type({'a': 1}))

day = {
    'month': 'January',
    'weather': 'cold',
    'day-of-week': 'Friday'
}

dict_keys = ['month', 'weather', 'day-of-week']

print(day['month'], day['weather'], day['day-of-week'])

for key in dict_keys:
    print(f'The {key} is {day[key]}')