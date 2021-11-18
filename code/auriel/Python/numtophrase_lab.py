#Version 1 of Lab
import random

# Create a list for ones, teens and tens
ones = { 1 : 'one', 2 : 'two', 3 : 'three', 4 :'four', 5 : 'five', 6 :'six', 7 : 'seven', 8 : 'eight', 9 :'nine', 10 : 'ten'}
teens = { 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eightteen', 19 : 'nineteen'}
tens = { 20 : 'twenty', 30 : 'thirty', 40 : 'fourty', 50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}

# Covert a given number into its english representation (0-99)
number = random.randint(0, 99)

one_digit = number % 10
ten_digit = number - one_digit

print(number)

if number == 0:
    print('zero')
elif number > 0 and number < 11:
    print(ones[number])
elif number > 10 and number < 20:
    print(teens[number])
elif number == 20 or number == 30 or number == 40 or number == 50 or number == 60 or number == 70 or number == 80 or number == 90:
    print(tens[number])
else:
    print(tens[ten_digit] + '-' + ones[one_digit])


# Version 2 of Lab

# Create a list for ones, teens and tens and hundreds
ones = { 0: '', 1 : 'one', 2 : 'two', 3 : 'three', 4 :'four', 5 : 'five', 6 :'six', 7 : 'seven', 8 : 'eight', 9 :'nine', 10 : 'ten'}
teens = { 0 : '', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eightteen', 19 : 'nineteen'}
tens = { 0 : '', 20 : 'twenty', 30 : 'thirty', 40 : 'fourty', 50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}
hundreds = { 100 : 'one hundred', 200 : 'two hundred', 300 : 'three hundred', 400 : 'four hundred', 500 : 'five hundred', 600 : 'six hundred', 700 : 'seven hundred',
800 : 'eight hundred', 900 : 'nine hundred'}

# Covert a given number into its english representation (0-999)
num = random.randint(0, 999)

one_digit = num % 10
ten_digit = (num % 100) - one_digit
hun_digit = (num - ten_digit) - one_digit
teens_digit = num - hun_digit

print(num)

if num == 0:
    print('zero')
elif num > 0 and num < 11:
    print(ones[num])
elif num > 10 and num < 20:
    print(teens[num])
elif num == 20 or num == 30 or num == 40 or num == 50 or num == 60 or num == 70 or num == 80 or num == 90:
    print(tens[num])
elif num > 19 and num < 100:
    print(tens[ten_digit] + '-' + ones[one_digit])
elif num == 100 or num == 200 or num == 300 or num == 400 or num == 500 or num == 600 or num == 700 or num == 800 or num == 900:
    print(hundreds[num])
elif teens_digit == 10:
    print(hundreds[hun_digit] + ' and ' + ones[teens_digit])
elif teens_digit > 11 and teens_digit < 20:
    print(hundreds[hun_digit] + ' and ' + teens[teens_digit])
else:
    print(hundreds[hun_digit] + ' and ' + tens[ten_digit] + ' ' + ones[one_digit])