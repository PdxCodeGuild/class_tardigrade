numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

multiply = lambda x, y: x * y

print(multiply(7, 11))