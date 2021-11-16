import time

""" Types """

x = 1
y = 1.0
z = '1'

print(x, type(x)) # int
print(y, type(y)) # float
print(z, type(z)) # string

print(True, type(True))
print(False, type(False))

# print 'hello world' as literal
print('hello world')

# print 'hello world' as variable
message = 'hello world'
print(message)

print(bool('False')) # True
print(bool(1)) # True

num1 = input('enter a number: ')
num2 = input('enter a number: ')

print(f'calculating {num1} + {num2}')
time.sleep(2)
print(int(num1) + int(num2))

"""Colorama"""
from colorama import Fore, Back, Style
print(Fore.GREEN + 'this is red text')
print(Back.WHITE + 'this is red text on a blue background')
print(Style.RESET_ALL)
print('back to normal')


"""Floor Division"""

print(10 / 3) # floats do weird math (this one ends with 3.33333333335)
print(10 // 3)

print(11 / 3)
print(11 // 3)


""" for loops """
# index:0  1  2  3  4  5  6  7
nums = [3, 6, 1, 9, 3, 6, 9, 2]

# plain for loop
for num in nums:
    print(num)

# for loop using range:
for i in range(len(nums)):
    print(i, nums[i])

# print(nums[3], nums[2])

""" while loop REPL (read evaluate print loop) """
# pt 2 of average nums

while True: # loop, it will come back here and start again
    user_input = input('tell me something (or type \'done\' to quit): ') # reads user input
    if user_input == 'done': # evaluating based on user input
        print('thanks for using this application')
        break
    print('You said: ' + '"' + user_input + '"') # prints out a new string based on user input