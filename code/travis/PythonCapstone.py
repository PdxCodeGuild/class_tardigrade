"""
Python Mini Capstone
Encrypted shopping search and list
Author: Travis Jackson
Date: 12 13 21

"""
import requests
from cryptography.fernet import Fernet
import json
#access secure data using "pip install cryptography"


#pull data from website. then edit, then encrypt to document then decrypt.


#search_input = input(f"Enter the type of alcohol you would like to see: ")
search_input = "gin"
response = requests.get(f"http://www.thecocktaildb.com/api/json/v1/1/search.php?i={search_input}")


#data = response.json()
#print(response.url)
#print(response.text)

#print(data["ingredients"][0]["strIngredient"])


key = Fernet.generate_key()
print(key)

f = Fernet(key)

token = f.encrypt(b"testing encrypt")
print(token)


print(f.decrypt(token))


file_location = "C:/Users/robot/pdx_code/bootcamp/class_tardigrade/code/travis/secret-list.txt"
with open(file_location, 'r', encoding="utf-8") as secret_file:
    secret_lines = secret_file.readlines()
  #  print(secret_lines) # ['First line\n', 'Second line\n']



with open(file_location, 'w', encoding="utf-8") as secret_file_w:
    secret_file_w.write(f"{token} {f.decrypt(token)}")







