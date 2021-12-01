#RNG Password Creater

import random
import string

letters = string.ascii_letters 
# print(letters)  abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
digits = string.digits
# print(digits) 0123456789
punctuation = string.punctuation
# print(punctuation) !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
lett_characters = letters
lett_num_characters = letters + digits
all_characters = letters + digits + punctuation
# print(all_characters) abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


password = ''
# pass_len = int(input('How long would you like your password?: '))

# while len(password) <= pass_len:
#     password += random.choice(all_characters)
# print(password)
"""
message = input('Would you like letters, numbers and punctuation in your password? yes/no: ')

if message == 'yes':
    while len(password) <= pass_len:
        password += random.choice(all_characters)
    print(password)
else:
    lett_num_pass = input('Would you like letters and numbers only? yes/no: ')
    if lett_num_pass == 'yes':
        while len(password) <= pass_len:
            password += random.choice(lett_num_characters)
        print(password)
    else:
        while len(password) <= pass_len:
            password += random.choice(lett_characters)
        print(password)

"""
#RNG Password optional
"""

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase

lower_case = int(input('How many lowercase letters would you like?: '))
numbers = int(input('How many numbers would you like?: '))
upper_case = int(input('How many uppercase letters would you like?: '))
special_characters = int(input('How many special characters would you like?: '))

for i in range(lower_case):
    password += random.choice(lower_letters)
for i in range(numbers):
    password += random.choice(digits)
for i in range(upper_case):
    password += random.choice(upper_letters)
for i in range(special_characters):
    password += random.choice(punctuation)
print(password)
random_password = ''.join(random.sample(password, len(password)))
print(random_password)


"""