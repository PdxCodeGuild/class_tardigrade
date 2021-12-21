"""
Lab 10: ROT Cipher
Author: Travis Jackson
Date: 11/29/21

"""


input_to_list = []
encrypted_list = []
rotated_ASCII_int = 0
output_encrypted = ""


#version 1 value
chiper_rotation_amount = 13


input_string = input("Enter a string to encrypt: ")

#Version 2
chiper_rotation_amount = int(input("What value would you like to rotate by: "))


input_string = input_string.lower()


#adds inputs to list
for input_char in input_string:

    input_to_list.append(input_char)


# rotates input character along ascii values by the chiper rotation amount
# ASCII "a" = 97, "z" = 122
for input_char in input_to_list:

    #checks to see if entered character goes past "z" (122) or is a space (32)
    if ord(input_char) == 32:

        rotated_ASCII_int = 32

    elif ord(input_char) + chiper_rotation_amount > 122:

        over_rotation = 122 - ord(input_char)
        rotated_ASCII_int = 122 - over_rotation + chiper_rotation_amount - 26

    else:

        rotated_ASCII_int = ord(input_char) + chiper_rotation_amount


    encrypted_list.append(chr(rotated_ASCII_int))
    

#adds items in encrypted list to output string
for item in encrypted_list:

    output_encrypted += item


print("Encrypted text: " + output_encrypted)
