file_path = 'code/pete/advent_of_code/day01/input.txt'
with open(file_path, 'r') as file:
    measurements = file.read().split('\n')

for n, measurement in enumerate(measurements):
    measurements[n] = int(measurement)
    # print(n, measurement)
    # if n == len(measurements) - 1:
    #     print(type(n), type(measurement))
print(measurements)

increase_counter = 0
for i in range(len(measurements)):
    if measurements[i] > measurements[i - 1]:
        increase_counter += 1

print(increase_counter)