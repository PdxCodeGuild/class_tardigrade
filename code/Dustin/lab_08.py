"""
    Convert the input string into a list of ints
    Slice off the last digit. That is the check digit.
    Reverse the digits.
    Double every other element in the reversed list.
    Subtract nine from numbers over nine.
    Sum all values.
    Take the second digit of that sum.
    If that matches the check digit, the whole card number is valid.

For example, the worked out steps would be:

    4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
    4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
    5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
    10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
    1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
    85
    5
    """
cc_num = (input("Enter the credit card number: "))
cc_num = cc_num.split()
for i in range(0, len(cc_num)):
    cc_num[i] = int(cc_num[i])
check = cc_num[:14:-1]
cc_num = cc_num[::-1]
print(check)
print(cc_num)

"""function will go here but want to figure code out first before moving it into function"""
def verify(num):
    num = num
