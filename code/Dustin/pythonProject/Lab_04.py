"""Numbers to words"""
number = int(input("Enter the number here: "))

hundred_digit = number//100
tens_digit = number%100//10
ones_digit = number%20

if number == 0:
    print('zero')

ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

#i just added this here

if number > 999:
    print(f"{number} has too many digits, please enter a number below 1,000: ")
elif number < 19:
    print(ones[number])
elif number < 99:
    print(tens[tens_digit], ones[ones_digit])
else:
    print(ones[hundred_digit], " Hundred ", tens[tens_digit],ones[ones_digit])

'''
potential dictionary use
ones = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}
'''