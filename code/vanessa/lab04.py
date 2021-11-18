#Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'.
#Hint: you can use modulus to extract the ones and tens digit.
#x = 67
#tens_digit = x//10
#ones_digit = x%10
#Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

#recieve an input, break down single and ten digits, use list or dict to generate word rep, print

from os import X_OK


ones = {
    0: " ",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
            }
tens = {
    2: "twenty",
    3: "thirty",
    4: "fourty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
            }
special = {
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

x= input("Enter a number: ")
x = int(x)
while True:
    if x in special:
        print(special.get(x))
        break
    elif x not in special:
        tens_digit = x//10
        ones_digit = x%10
        print(tens.get(tens_digit),ones.get(ones_digit))
        break

