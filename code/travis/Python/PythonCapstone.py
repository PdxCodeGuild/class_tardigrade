"""
Python Mini Capstone
Encrypted shopping search and list
Author: Travis Jackson
Date: 12 13 21

"""

import base64
import json
import os
from types import NoneType
import requests
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

#access secure data using "py -m pip install cryptography"


####mini capstone features:
#pull data from website. then edit, then encrypt to document then decrypt.
#create password, user and tie to cipher text with salt
#repl to enter data, retrieve data

new_encrypt_list = []
search_input = ""




def read_encrypted_list():

  file_location = "C:/Users/robot/pdx_code/bootcamp/class_tardigrade/code/travis/secret-list.txt" 
  with open(file_location, 'r', encoding="utf-8") as secret_file:
      secret_lines = secret_file.readlines()
      print("Decrypted list")

      #take items out of returned file
      for items in secret_lines:
        secret_lines_str = items        
        new_decrypt = Cryptography(verified_user_salt, input_user_password, secret_lines_str)

        decrypted_output = new_decrypt.perform_decrypt()

        print(f"--- {decrypted_output.decode()}")


def write_encrypted_list(test_save_data):

  file_location = "C:/Users/robot/pdx_code/bootcamp/class_tardigrade/code/travis/secret-list.txt"

  with open(file_location, 'w', encoding="utf-8") as secret_file_w:
    secret_file_w.write("\n".join(test_save_data))
 #   secret_file_w.write(test_save_data.decode())



# Create the cipher text and key:
# key is made with salt and password

def create_f(input_salt, user_password):
      
    #creates the first part of key using salt
    #SHA enables password functionality
    kdf = PBKDF2HMAC(
      algorithm=hashes.SHA256(),
      length=32,
      salt=input_salt,
      iterations=390000,
    )
    #combines user salt and user_password
    key = base64.urlsafe_b64encode(kdf.derive(user_password))

    #symmetric encryption ties it to key
    f = Fernet(key)
    return f


class User():

  def __init__(self, user_name, password):
    self.user_name = user_name
    self.password = password
    
  def __repr__(self):
 
    return self.user_name

  def create_user():
    ...


  def load_user_salt(self):
    """
    Checks user then loads, validates then returns their salt
    
    """
    user_filename = "C:/Users/robot/pdx_code/bootcamp/class_tardigrade/code/travis/user_info.txt"

    with open(user_filename, "r") as user:
      user_lines = user.read().split('\n')
    

    user_id = user_lines[0]
    user_file_salt = user_lines[1].encode()   
    user_encrypt = user_lines[2]


    
    user_salt = user_file_salt.decode("unicode-escape").encode('ISO-8859-1')
     
    if self.user_name.decode() != user_id:

      return False
  
    try:

      f = create_f(user_salt, self.password) 

      #uses entered password and checks it with saved cipher text
      f.decrypt(str.encode(user_encrypt))
    except:

        return False        

    #verifies the user password is correct
    try:
      decrypted_is_valid = f.decrypt(str.encode(user_encrypt)).decode()

   
    except:

      return False
    
    if decrypted_is_valid != "user_verified":

      return False

    #returns user salt to preform cryptography tasks
    return user_salt.decode("unicode-escape").encode('ISO-8859-1')   
 

class Cryptography():

  def __init__(self, user_salt, user_password, new_data):

    self.user_salt = user_salt
    self.new_data = new_data   
    self.user_password = user_password
 

  def perform_decrypt(self):
    """
    decrypt data
    """
    decrypt_f = create_f(self.user_salt, self.user_password)

    return (decrypt_f.decrypt(str.encode(self.new_data)))

  def create_encrypt_data(self):

    encrypt_f = create_f(self.user_salt, self.user_password)
    encrypt_token = encrypt_f.encrypt(self.new_data)


    return encrypt_token
  

print(f" {'-' * 30}")
print("Welcome to your encrypted shopping list!")
print(f" {'-' * 30}")


#User login and user verify
print("Login!!")
while True:

  input_user_name = input("Enter username: ").encode()
  input_user_password = input("Enter password: ").encode()

  ##check username and password and then gets salt
  new_user = User(input_user_name, input_user_password)

  verified_user_salt = new_user.load_user_salt()
  if verified_user_salt == False:
    print("Incorrect login")
  else:
    break 

#read list
if input("Would you like to read your list (y)? ") == "y":
  read_encrypted_list()

print("Make your new alcohol Christmas shopping list:")
print(f" {'-' * 30}")
print()
#####API Search
while True:
 
  search_input = input(f'Enter ("w" to write) ("q" to quit) or the type of alcohol from API you would like add to list: ')
  print()

  if search_input == "q":
    break


  if search_input == "w":

    encrypt_list = []

    if len(new_encrypt_list) == 0:

      print("Your list is empty!")
      continue

    else:

      print("Items added to list:")
      for item in new_encrypt_list:
        
        new_data = item
        new_encrypt = Cryptography(verified_user_salt, input_user_password, new_data)
        test_save_data = new_encrypt.create_encrypt_data()
        print(f"   {new_data.decode()}")
        encrypt_list.append(test_save_data.decode())

    write_encrypted_list(encrypt_list)

    break

  try:
    response = requests.get(f"http://www.thecocktaildb.com/api/json/v1/1/search.php?i={search_input}")

    data = response.json() 
    test_data = data["ingredients"][0]["strIngredient"]

    new_encrypt_list.append(test_data.encode())
    print(f"{test_data} added to encrypted list")
    print()


  except:
    print("Drink not found. Try again")
    print()

