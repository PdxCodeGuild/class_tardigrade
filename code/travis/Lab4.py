"""
Lab 4: Number to Phrase
Author: Travis Jackson
Date: Updated on 12/1/2021

"""


dict_words = {
    0: ["", "zero", ""],

    1: [["ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"], "one", "one hundred"  ] ,
    2: ["twenty", "two" , "two hundred"],
    3: ["thirty", "three" , "three hundred"],
    4: ["forty", "four", "four hundred"],
    5: ["fifty", "five", "five hundred"],
    6: ["sixty", "six", "six hundred"],
    7: ["seventy", "seven", "seven hundred"],
    8: ["eighty", "eight", "eight hundred"],
    9: ["ninety", "nine", "nine hundred"]
    }



user_input = input("Enter a number: ")

hundreds_digit = int(user_input) // 100
tens_digit = int(user_input) // 10 % 10
ones_digit = int(user_input) % 10


#check for special cases and prints

#teen numbers
if tens_digit == 1:
    
    hundreds_digit_output = dict_words[hundreds_digit][2]
    tens_digit_output = dict_words[tens_digit][0][ones_digit]

    if hundreds_digit == 0:
        print(f"{tens_digit_output}")
    
    elif hundreds_digit != 0:
        print( f"{hundreds_digit_output} {tens_digit_output}")



#checks for zero
elif hundreds_digit == 0 and tens_digit == 0 and ones_digit == 0:

    ones_digit_output = dict_words[ones_digit][1]
    print(f"{ones_digit_output}")
        

#checks for inputs with 0 at the end. ie.. 20 == twenty
elif ones_digit == 0 and tens_digit != 0 and hundreds_digit == 0:

    hundreds_digit_output = dict_words[hundreds_digit][2]
    tens_digit_output = dict_words[tens_digit][0]

    print(f"{tens_digit_output}")

elif ones_digit == 0 and tens_digit != 0 and hundreds_digit != 0:

    hundreds_digit_output = dict_words[hundreds_digit][2]
    tens_digit_output = dict_words[tens_digit][0]

    print(f"{hundreds_digit_output} {tens_digit_output}")

#checks 1-9 entry 
elif tens_digit == 0 and hundreds_digit == 0:

    ones_digit_output = dict_words[ones_digit][1]

    print(f"{ones_digit_output}")

#checks for inputs with no tens or ones. ie.. 100 = one hundred
elif tens_digit == 0 and ones_digit == 0:

    hundreds_digit_output = dict_words[hundreds_digit][2]
    print(f"{hundreds_digit_output}")
    
    #checks for no tens
elif tens_digit == 0 and ones_digit != 0:
    hundreds_digit_output = dict_words[hundreds_digit][2]
    ones_digit_output = dict_words[ones_digit][1]
    print(f"{hundreds_digit_output} {ones_digit_output}")

elif hundreds_digit == 0:
    tens_digit_output = dict_words[tens_digit][0]
    ones_digit_output = dict_words[ones_digit][1]

    print(f"{tens_digit_output}-{ones_digit_output}")


elif ones_digit == 0 and tens_digit != 0 and hundreds_digit == 0:

    hundreds_digit_output = dict_words[hundreds_digit][2]
    tens_digit_output = dict_words[tens_digit][0]

    print(f"{tens_digit_output}")


else:      
    hundreds_digit_output = dict_words[hundreds_digit][2]
    tens_digit_output = dict_words[tens_digit][0]

    ones_digit_output = dict_words[ones_digit][1]

    print(f"{hundreds_digit_output} {tens_digit_output}-{ones_digit_output}")

