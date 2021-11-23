# Credit Card Lab

import random

credit_card_numbers = []

while len(credit_card_numbers) < 16:
    # new_number = int(input('Please enter a number between 0-9 until it stops: '))
    new_number = random.randint(0, 9)
    credit_card_numbers.append(new_number)

print(credit_card_numbers)
check_number = credit_card_numbers.pop(15)
credit_card_numbers.reverse()
print(credit_card_numbers, check_number)

# nums = []
# for x in range(10):
#     if x % 2:
#         nums.append(x*2)
#     elif x % 1:
#         pass

for i, number in enumerate(credit_card_numbers):
    if i % 2 == 0:
        credit_card_numbers[i] = (number * 2)
        if credit_card_numbers[i] > 9:
            credit_card_numbers[i] = credit_card_numbers[i] - 9
total = sum(credit_card_numbers)
print(f'total is {total}, \ncheck number is {check_number}')
if total % 10 == check_number:
    print('Valid credit card number!')
elif total % 10 != check_number:
    print('Not a valid credit card')


# print(credit_card_numbers)

# print(credit_card_numbers)

# def doubled_numbers():
#     for x in credit_card_numbers[::2]:
#         x = x*2
#         if x > 9:
#             x = x - 9
#             return x
# print(doubled_numbers())
# for x in credit_card_numbers[::2]:
#     x = x*2
#     if x > 9:
#         x = x  - 9
#     print(x)



# print(credit_card_numbers[::2], credit_card_numbers[::2]*2)




# for i in credit_card_numbers:
#     if i > 9:
#         i - 9
#     elif i <=9:
#         i = i
# print(i)
# print(nums)
# print(58 % 10)