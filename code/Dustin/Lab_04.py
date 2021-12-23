"""Numbers to words"""
number = int(input("Enter the number here: "))

hundred_digit = number//100
tens_digit = number%100//10
ones_digit = number%20


ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
        'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']



if number > 999:
    print(f"{number} has too many digits, please enter a number below 1,000: ")
elif number < 19:
    print(ones[number])
elif number < 99:
    print(tens[tens_digit], ones[ones_digit])
else:
    print(ones[hundred_digit], " Hundred ", tens[tens_digit],ones[ones_digit])
