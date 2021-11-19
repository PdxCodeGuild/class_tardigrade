"""
Lab 5: Blackjack Advice
Author: Travis Jackson
Date: 11/17/21

"""


first_input = input("What is your first card?")
second_input = input("What is your second card?")
third_input = input("What is your third card?")

# check for face cards or ace, change to numerical values
if first_input == "k" or first_input == "q" or first_input == "j":
    first_input = "10"
elif first_input == "a":
    first_input = "1"

if second_input == "k" or second_input ==  "q" or second_input == "j":
    second_input = "10"
elif second_input == "a":
    second_input = "1"

if third_input == "k" or third_input == "q" or third_input == "j":
    third_input = "10"
elif third_input == "a":
    third_input = "1"


#add up cards
total_value = int(first_input) + int(second_input) + int(third_input)


if total_value < 17:
    print(f" {total_value} You should Hit")
elif 17 == total_value < 21:
    print(f" {total_value} You should Hold")
elif total_value == 21:
    print(f" {total_value} Blackjack!")
else:
    print(f" {total_value} Already Busted")
    