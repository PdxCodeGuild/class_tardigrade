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
    0: "and",
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
    0:  "zero",
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
hundreds={
    0: " ",
    1: "one-hundred",
    2: "two-hundred",
    3: "three-hundred",
    4: "four-hundred",
    5: "five-hundred",
    6: "six-hundred",
    7: "seven-hundred",
    8: "eight-hundred",
    9: "nine-hundred",
}
x= input("Enter a number (0-999): ")
x = int(x)
while True:
    if x in special:
        print(special.get(x))
        break
    elif x not in special:
        hundreds_digit = x//100
        tens_digit = (x%100)//10
        ones_digit = x%10
        print(hundreds.get(hundreds_digit),tens.get(tens_digit),ones.get(ones_digit))
        break

