"""

Lab 10: ROT Cipher

Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the
corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so
encryption is the same as decryption.
"""

message_in = input("Type message here for encryption:"  )
key = int(input("Enter number for encryption rotation: "))
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def cipher(message, rotation):
    message = message.lower()
    coded_message = ""
    for letter in message:
        if letter.isalpha():
            coded_message += alphabet[(alphabet.index(letter) + rotation ) % 26]
        else:
            coded_message += letter
    return coded_message


print(cipher(message_in, key))