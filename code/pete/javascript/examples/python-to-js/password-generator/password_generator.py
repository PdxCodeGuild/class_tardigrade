from random import choice
from string import ascii_letters, digits, punctuation

characters = ascii_letters + digits + punctuation

print(characters)

password = ''

for _ in range(10):
    password += choice(characters)

print(password)