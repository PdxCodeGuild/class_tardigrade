"""Lists"""


colors = ['red', 'green', 'blue']
# print out each color
for banana in colors:
    # banana is a loop variable
    # banana = colors[0]
    # banana = colors[1]
    # banana = colors[2]
    print(banana)

# add 'yellow' to list
colors.append('yellow')
print(colors)

# replace 'green' with 'purple'
colors[1] = 'purple'
print(colors)


"""Errors"""
# a = '1'
# b = 1
# c = a + b
# print(c)

# abc123 = {'a': 1, 'b': 2, 'c': 3}
# print(abc123['d'])

"""Modules"""
import random
# random color from the colors list
print(random.choice(colors))

import time
# print out all the colors, but have a 1 second
# pause in between each
for pretty_color in colors:
    print(time.time()) # gives current time in seconds since Jan 1 1970
    time.sleep(1)
    print(pretty_color)


