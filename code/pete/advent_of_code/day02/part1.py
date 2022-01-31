# sample input
"""
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

# sample list of dictionaries
commands = [
    # {}, # command = {}
    # {'direction': 'forward'}, # command['direction'] = command_list[0]
    # {'direction': 'forward', 'value': 5}, # command['value'] = int(command_list[1])
    {'direction': 'forward', 'value': 5},
    {'direction': 'down', 'value': 5},
    {'direction': 'forward', 'value': 8},
    {'direction': 'up', 'value': 3},
    {'direction': 'down', 'value': 8},
    {'direction': 'forward', 'value': 2},
]

filepath = 'code/pete/advent_of_code/day02/input.txt'
with open(filepath, 'r') as f:
    contents = f.read()
# print(contents)

# 1. get a list of individual lines
raw_commands = contents.split('\n')
# print(raw_commands)

# 2. create a new list and loop over raw_commands to get the
# necessary data for the new list of dictionaries
commands = []
for command_str in raw_commands:
    # make a dictionary
    command = {}
    # split string into list with direction at index 0
    # and value at index 1
    command_list = command_str.split()
    # add direction and value to dictionary
    command['direction'] = command_list[0]
    command['value'] = int(command_list[1])

    # append that dictionary to commands
    commands.append(command)

# 3. establish counters for horizontal position and depth
horizontal = 0
depth = 0

# loop over commands list of dictionaries
for command in commands:
    # implement 'forward' direction
    if command['direction'] == 'forward':
        horizontal += command['value']
    # implement 'down' direction
    elif command['direction'] == 'down':
        depth += command['value']
    # implement 'up' direction
    elif command['direction'] == 'up':
        depth -= command['value']

# print(commands)
print(horizontal)
print(depth)

print(horizontal * depth)