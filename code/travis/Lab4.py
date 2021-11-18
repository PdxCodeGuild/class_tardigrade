"""
Lab 4: Number to Phrase
Author: Travis Jackson
Date: 11/17/21

"""

dict_words = {
    0: ["", "zero"],
    1: [["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"], "one"],
    2: ["twenty", "two"],
    3: ["thirty", "three"],
    4: ["fourty", "four"],
    5: ["fifty", "five"],
    6: ["sixty", "six"],
    7: ["seventy", "seven"],
    8: ["eighty", "eight"],
    9: ["ninety", "nine"]
    }


user_input = input("Enter a number: ")

tens_digit = int(user_input) // 10
ones_digit = int(user_input) % 10


#check for special cases and prints
#teen numbers
if tens_digit == 1:

    tens_digit_output = dict_words[tens_digit][0][ones_digit]
    print(tens_digit_output)

#checks for zero
elif tens_digit == "" and ones_digit == 0:

    ones_digit_output = dict_words[ones_digit]
    print(ones_digit_output)
        
#checks for inputs with 0 at the end. ie.. 20 == twenty
elif ones_digit == 0 and tens_digit != "":

    tens_digit_output = dict_words[tens_digit][0]
    print(tens_digit_output)

#checks 1-9 entry 
elif tens_digit == 0:

    ones_digit_output = dict_words[ones_digit][1]
    print(ones_digit_output)

else:      

    tens_digit_output = dict_words[tens_digit][0]
    ones_digit_output = dict_words[ones_digit][1]

    print(tens_digit_output, ones_digit_output)

    