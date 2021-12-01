"""
Lab 8: Credit Card Validation
Author: Travis Jackson
Date: 11/22/21

"""


card_num_list = []

#card_num_list_verification = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9 ,9 ,8, 5, 5]

list_sum = 0


# 1: convert input into list of ints
input_nums = input("Enter credit card number with each digit separated by a space: ")

card_num_list = input_nums.rsplit(" ")

for i, num_string in enumerate(card_num_list):

        card_num_list.pop(i)
        card_num_list.insert(i, (int(num_string)))


#2: remove last digit (check digit)
check_digit = card_num_list.pop(-1)

#3: reverse digits
card_num_list.reverse()

#4: double every other element in the list
for i, double in enumerate(card_num_list):

    if i % 2 == 0:
        double *= 2
        card_num_list.pop(i)
        card_num_list.insert(i, double)


#5 subtract nine from nums over 9
for i, subtract in enumerate(card_num_list):

    if subtract > 9:
        subtract -= 9
        card_num_list.pop(i)
        card_num_list.insert(i, subtract)


#6: sum all values
for i, sum_num in enumerate(card_num_list):

    list_sum += sum_num


#7: take the second digit of that sum for check digit
second_check_digit = list_sum % 10


#8: check matches to the check digit
if check_digit == second_check_digit:

    print("Valid")
else:
    print("Error")


