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
# include class and methods
#create password, hash to key
#repl to enter data, retrieve data

#salt = os.urandom(16)
def read_encrypted_list():
  file_location = "C:/Users/robot/pdx_code/bootcamp/class_tardigrade/code/travis/secret-list.txt" 
  with open(file_location, 'r', encoding="utf-8") as secret_file:
      secret_lines = secret_file.readlines()

      #take items out of returned file
      for items in secret_lines:
        secret_lines_str = items

        print(f" items from doc {secret_lines_str}")
        
        ##decodes item from document
        
      # print(salt)
      #  print(input_user_password)
        # print(secret_lines_str)
        #new_crypt = Cryptography(salt, input_user_password, secret_lines_str)

        # try:
      new_decrypt = Cryptography(verified_user_salt, input_user_password, secret_lines_str)

      decrypted_output = new_decrypt.perform_decrypt()

      print(f"This data is decrypted from file {decrypted_output}")
        # except:
        #   print("error")

def write_encrypted_list(test_save_data):

  file_location = "C:/Users/robot/pdx_code/bootcamp/class_tardigrade/code/travis/secret-list.txt"

  with open(file_location, 'w', encoding="utf-8") as secret_file_w:
    
    secret_file_w.write(test_save_data.decode())


def create_f(input_salt, user_password):
      
    kdf = PBKDF2HMAC(
      algorithm=hashes.SHA256(),
      length=32,
      salt=input_salt,
      iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(user_password))
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
    Checks user then loads their hash
    
    """
    user_filename = "C:/Users/robot/pdx_code/bootcamp/class_tardigrade/code/travis/user_info.txt"

    with open(user_filename, "r") as user:
      user_lines = user.read().split('\n')
    

    user_id = user_lines[0]
    user_file_salt = user_lines[1].encode()   
    user_encrypt = user_lines[2]

    user_salt = user_file_salt.decode("unicode-escape").encode('ISO-8859-1')
     
    if self.user_name.decode() == user_id:

      print(f"Welcome {self.user_name}")

    else: 

      print("Enter valid username")
    
    f = create_f(user_salt, self.password)
 
    f.decrypt(str.encode(user_encrypt))

    decrypted_is_valid = f.decrypt(str.encode(user_encrypt)).decode()

    print(f"Verified user? : {decrypted_is_valid}")

  #  if decrypted_is_valid != "user_verified":
  #    return False

 #   elif decrypted_is_valid == "user_verified":

    return user_salt.decode("unicode-escape").encode('ISO-8859-1')   
 

class Cryptography():

  def __init__(self, user_salt, user_password, new_data):

    self.user_salt = user_salt
    self.new_data = new_data   
    self.user_password = user_password
 
  # def perform_encrypt(self, input_data):
  #   """
  #   Encrypt method
  #   """
  #   #changes to byte
  #   data_to_encrypt = str.encode(input_data) 
  #   encrypt_f = create_f(self.user_salt, self.user_password)

  #   #encrypt data using key
  #   token = encrypt_f.encrypt(data_to_encrypt) 

  #   return token


  def perform_decrypt(self):
    """
    decrypt data
    """
    decrypt_f = create_f(self.user_salt, self.user_password)

    return (decrypt_f.decrypt(str.encode(self.new_data)))

  def create_encrypt_data(self):

    print(f"this is new data: {self.new_data}")
    encrypt_f = create_f(self.user_salt, self.user_password)
    encrypt_token = encrypt_f.encrypt(self.new_data)

    print(f"this is new encrypted data {encrypt_token}")
    return encrypt_token
  


#User login and user verify
while True:

######User Login input
 # input_user_name = input("Enter username")
 # input_user_password = input("Enter password: ")
  input_user_name = "travis".encode()
  input_user_password = "password".encode()
  


  ##check username get salt
  new_user = User(input_user_name, input_user_password)

 # if new_user.load_user_salt() == False:

 #   print("Incorrect Login")

 # else:

  verified_user_salt = new_user.load_user_salt()

  #verify user exists and password is correct

  if input("Read list? ") == "y":
    read_encrypted_list()

  break




#####API Search
while True:

  search_input = input(f'Enter the type of alcohol you would like add to list? ("q" to quit' )

  if search_input == "q":
    if input("write list? ") == "y":
      
      new_data = test_data.encode()
      new_encrypt = Cryptography(verified_user_salt, input_user_password, new_data)
      test_save_data = new_encrypt.create_encrypt_data()

      write_encrypted_list(test_save_data)
    break

  try:
    response = requests.get(f"http://www.thecocktaildb.com/api/json/v1/1/search.php?i={search_input}")

    data = response.json() 
    test_data = data["ingredients"][0]["strIngredient"]
    print(f"{test_data} added to encrypted list")



  except:
    print("drink not found. Try again")

