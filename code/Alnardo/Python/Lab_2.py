#LAB 2

#Version 1

nums = [5, 0, 8, 3, 4, 1, 6]

# # loop over the elements
# for num in nums:
#     print(num)

# loop over the indices
# for i in range(len(nums)):
#     print(nums[i])

#Looked back on previous lessons for Intro 102 Lab 2 for help. Also Googled to figure out the proper wording
total = 0


for num in range(len(nums)):
    total = total + nums[num]
    print(total)

print(total / len(nums))




# for num in nums:
#     total = 0
#     num = num + total
#     print(num)


#Version 2
print('Welcome to the calculator!')

message = input('Would you like to enter a number? y/n: ')
# enter_number = int(input('Enter a number: '))

num = []


while message == 'y':
    enter_numbers = int(input('What numbers would you like to add?: '))
    num.append(enter_numbers)
    more_numbers = input('Do you have more numbers to add? y/n: ')
    if more_numbers == 'y':
        continue
    elif more_numbers == 'n':
        print(f'Your total is {sum(num)}')
        average = sum(num) / len(num)
        print(f'Your average is {average}!')
        break
    else:
        print('Error, try again with correct responses.')
        break