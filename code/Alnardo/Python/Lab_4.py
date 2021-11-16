digits = {
    0 : 'zero',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven', 
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
}

double_digits = {
    2 : 'twenty',
    3 : 'thirty',
    4 : 'fourty',
    5 : 'fifty',
    6 : 'sixty',
    7 : 'seventy',
    8 : 'eighty',
    9 : 'ninety'
}


hundred_digits = {
    1 : 'One hundred',
    2 : 'Two hundred',
    3 : 'Three hundred',
    4 : 'Four hundred',
    5 : 'Five hundred',
    6 : 'Six hundred',
    7 : 'Seven hundred',
    8 : 'Eight hundred',
    9 : 'Nine hundred'
}


num = int(input('Please enter a number between 0-999: '))

if num >= 100:
    hundreds = num // 100
    num = num - (hundreds * 100)
    if num >= 20:
        tens = num // 10
        singles = num % 10
        print(f'{hundred_digits[hundreds]} {double_digits[tens]} {digits[singles]}')
    elif num < 20:
        print(f'{hundred_digits[hundreds]} {digits[num]}')


elif num < 100:
    if num >= 20:
        tens = num // 10
        singles = num % 10
        print(f'{double_digits[tens]} {digits[singles]}')
    elif num < 20:
        print(digits[num])

