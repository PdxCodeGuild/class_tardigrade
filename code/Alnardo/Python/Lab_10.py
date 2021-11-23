# Lab 10 ROT 13 cypher

import string
letters = string.ascii_lowercase
message = input('What do you want to encode?: ')
cypher = ''

for i, letter in enumerate(message):
    # print(letter)
    # print(i)
    i = letters.index(letter)
    
    if i + 13 < 26:
        i += 13
        print(i, letters[i])
        cypher += letters[i]
    elif i + 13 >= 26:
        i -= 13
        print(i, letters[i])
        cypher += letters[i] 
    # print(letters[i])

print(cypher)

# #Optional
# import string
# letters = string.ascii_lowercase
# message = input('What do you want to encode?: ')
# number = int(input('Please enter a number to cypher: '))
# cypher = ''

# for i, letter in enumerate(message):
#     # print(letter)
#     # print(i)
#     i = letters.index(letter)
#     # print(i)
    
#     if i + number < 26:
#         i += number
#         print(i, letters[i])
#         cypher += letters[i]
#     elif i + number >= 26:
#         i = (i + number) - 26
#         print(i, letters[i])
#         cypher += letters[i] 
#     # print(letters[i])

# print(cypher)





"""
#Optional
import string
letters = string.ascii_lowercase
cypher = ''
number = int(input('Please enter a number to cypher: '))
for i in range(len(letters)):
    if i + number < 26:
        # i += 13
        i += number
        print(i, letters[i])
        cypher += letters[i]
    elif i + number >= 26:
        # i -= 13
        i = (i + number) - 26
        print(i, letters[i])
        cypher += letters[i] 
    # print(letters[i])
print(cypher)
"""