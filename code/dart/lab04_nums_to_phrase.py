import random

ones = {
    0: "", 
    1: "one", 
    2: "two", 
    3: "three", 
    4: "four", 
    5: "five", 
    6: "six", 
    7: "seven", 
    8: "eight", 
    9: "nine", 
    10: "ten"
}

teens = {
    0: "", 
    11: "eleven", 
    12: "twelve", 
    13: "thirteen", 
    14: "fourteen", 
    15: "fifteen", 
    16: "sixteen", 
    17: "seventeen", 
    18: "eighteen", 
    19: "nineteen"
}

tens = {
    0: "", 
    20: "twenty",  
    30: "thirty",  
    40: "fourty",  
    50: "fifty",  
    60: "sixty", 
    70: "seventy",  
    80: "eighty",  
    90: "ninety"
}

hundreds = {
    0: "",
    100: "one hundred",  
    200: "two hundred",  
    300: "three hundred",  
    400: "four hundred",  
    500: "five hundred", 
    600: "six hundred",  
    700: "seven hundred",  
    800: "eight hundred", 
    900 : "nine hundred"
}

number = random.randint(0, 999)

one_digit = number % 10
ten_digit = (number % 100) - one_digit
hundred_digit = (number - ten_digit) - one_digit
teens_digit = number - hundred_digit

print(number)

if number == 0:
    print("Zero")
elif number > 0 and number < 11:
    print(ones[number])
elif number > 10 and number < 20:
    print(teens[number])
elif number == 20 or number == 30 or number == 40 or number == 50 or number == 60 or number == 70 or number == 80 or number == 90:
    print(tens[number])
elif number > 19 and number < 100:
    print(tens[ten_digit] + " " + ones[one_digit])
elif number == 100 or number == 200 or number == 300 or number == 400 or number == 500 or number == 600 or number == 700 or number == 800 or number == 900:
    print(hundreds[number])
elif teens_digit > 10 and teens_digit < 20:
    print(hundreds[hundred_digit] + " " + teens[teens_digit])
else:
    print(hundreds[hundred_digit] + " " + tens[ten_digit] + " " + ones[one_digit])