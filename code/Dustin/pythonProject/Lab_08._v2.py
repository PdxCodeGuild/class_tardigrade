"""Credit card validation"""
"""
proof number 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5

    Convert the input string into a list of ints
    Slice off the last digit. That is the check digit.
    Reverse the digits.
    Double every other element in the reversed list.
    Subtract nine from numbers over nine.
    Sum all values.
    Take the second digit of that sum.
    If that matches the check digit, the whole card number is valid.


4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
"""
tested_num = input("enter credit card number here: ")
list_num = tested_num.split()
for i in range(0, len(list_num)):
    list_num[i] = int(list_num[i])

check_num = list_num[15]
#print(check_num)
"5"
list_num = list_num[0:15:]
#print(list_num)
"4 5 5 6 7 3 7 5 8 6 8 9 9 8 5"
list_num.reverse()
#print(list_num)
"5 8 9 9 8 6 8 5 7 3 7 6 5 5 4"
list_num[::2] = [x*2 for x in list_num[::2]]
#print(list_num)
"10 8 18 9 16 6 16 5 14 3 14 6 10 5 8"
total = 0
for num in list_num:
    if num > 9:
        num = num -9
    else:
        num == num
    total = total + num
print(total)
"85"
total = total%10
#print(total)
"5"
if check_num == total:
    print("Valid!")
else:
    print("Invalid")

#print(check_num)





