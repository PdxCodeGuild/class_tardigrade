ones_converter = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

teens_converter = {
    0: 'ten',
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: 'fourteen',
    5: 'fifteen',
    6: 'sixteen',
    7: 'seventeen',
    8: 'eighteen',
    9: 'nineteen',
}

tens_converter = {
    0: '',
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

hundreds_converter = {
    0: '',
    1: 'one hundred',
    2: 'two hundred',
    3: 'three hundred',
    4: 'four hundred',
    5: 'five hundred',
    6: 'six hundred',
    7: 'seven hundred',
    8: 'eight hundred',
    9: 'nine hundred',
}

def translator(number):
    """
    given an integer 0-999, will return
    the phrase version
    i.e: 67 becomes 'sixty-seven'
    """
    if type(number) is not int:
        raise TypeError('number must be an integer')
    if number < 0 or number > 999:
        raise ValueError('number must be in range 0-999')
    if number == 0:
        return 'zero'
    hundreds = number // 100
    tens = number // 10 % 10
    ones = number % 10
    if number < 10:
        return ones_converter[ones]
    if number < 20:
        return teens_converter[ones]
    if number < 100:
        return f'{tens_converter[tens]}-{ones_converter[ones]}'.strip('- ')
    if tens == 0:
        return f'{hundreds_converter[hundreds]} {ones_converter[ones]}'.strip(' ')
    if tens == 1:
        return f'{hundreds_converter[hundreds]} {teens_converter[ones]}'
    return f'{hundreds_converter[hundreds]} {tens_converter[tens]}-{ones_converter[ones]}'.strip('- ')

# print(translator(67))
# print(translator(42))
# print(translator(88))
# print(translator(-1))
# print(translator(1001))
# print(translator('one')) 