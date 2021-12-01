"""FIRST VERSION (DOESN'T ACCOUNT FOR SPACES)"""

# def encryption(phrase):
#     abc = "abcdefghijklmnopqrstuvwxyz"
#     output = ""
#     for letter in phrase:
#         output += abc[(abc.find(letter) + 13) % 26]
#     return output

# phrase = input("Enter a phrase and I shall encrypt it: ")
# print(encryption(phrase))

"""SECOND VERSION (DOES ACCOUNT FOR SPACES)"""

from slowprint.slowprint import *

def encryption(phrase):
    key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    encrypt = dict(zip(key, value))
    return "".join(encrypt.get(char, char) for char in phrase)

phrase = input("Enter a phrase and I shall encrypt it: ")
slowprint(encryption(phrase), 2)

"""VERSION 2 (ALLOW USER TO INPUT AMOUNT OF ROTATION USED IN THE ENCRYPTION)"""

# def encryption(phrase):
#     key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     value = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
#     encrypt = dict(zip(key, value))
#     phrase = input("Enter your phrase: ")
#     shift = input("Enter the amount you would like to rotate by: ")
#     abc = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_phrase = ""   
#     shift = int(shift)

#     new_ind = 0 
#     for i in phrase:
#         if i.lower() in abc:
#             new_ind = abc.index(i) + shift
#             encrypted_phrase += abc[new_ind % 26]
#         else:
#             encrypted_phrase += i

#     return "".join(encrypt.get(char, char) for char in phrase)

# phrase = input("Enter a phrase and I shall encrypt it: ")
# print(encryption(phrase))
  
# print(f"Your phrase encrypted is {encrypted_phrase}.")