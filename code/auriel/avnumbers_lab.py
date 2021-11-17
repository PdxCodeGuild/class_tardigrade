nums = [5, 0, 8, 3, 4, 1, 6]
total = 0

for num in nums:
    total = total + num

avg = total / len(nums)

print(avg)


user_list = []
user_total = 0

while True:
    user = input('Enter a number, or \'done\' to quit: ')

    if user == 'done':
        break
    else:
        user == int(user)
        user_list.append(int(user))

for list in user_list:     
    user_total = user_total + list

average = user_total / len(user_list)

print('Your average is: ',average)