#Day 1 Part 1
"""
relative_path = 'github/class_tardigrade/code/Alnardo/Advent/'

with open('sonar_sweep.txt', 'r') as f:
    depth = f.read().split('\n')

for n, measurement in enumerate(depth):
    depth[n] = int(measurement)

# print(depth)

depth_counter = 0
for i in range(len(depth)):
    if depth[i] > depth[i - 1]:
        depth_counter += 1

print(depth_counter)

"""

#Day 1 Part 2
