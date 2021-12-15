"""
Python Mini Capstone
Encrypted shopping search and list
Author: Travis Jackson
Date: 12 13 21

"""

import os
import requests
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt





#access secure data using "py -m pip install cryptography"


####mini capstone features:
#pull data from website. then edit, then encrypt to document then decrypt.
# include class and methods
#create password, hash to key
#repl to enter data, retrieve data


class User():

  def __init__(self, user_name, password):
    self.user_name = user_name
    self.password = password

#  def __repr__(self):

 #   return self.user_name

  def login(self):
    ...


  def add_user(self):
      ...







class Cryptography():

  def __init__(self, f, key):

    self.key = key      
    self.f = f
    
  def __repr__(self):

      return f"F: {self.f}\n Key: {self.key}"


  def my_encrypt_method(self, input_data):
    """
    Encypt method
    """

    #turns to bytes
    data_to_encrypt = str.encode(input_data) 

    #encrypt data using key
    token = self.f.encrypt(data_to_encrypt)    
    


    #test encrypt print
    print(f" Token: Encrypted data {token}\n") 

    return token



  def my_decrypt(self, data_to_decrypt, test_key):
    """
    decrypt data
    """   
    try:
      kdf.verify(b"test", test_key)
    except:
      print("error")

    decrypt_key_input = test_key

    #turn to bytes

    decrypt_key = str.encode(decrypt_key_input)


    new_f = Fernet(decrypt_key)

    #turns data back to bytes
    test_decrypt = str.encode(data_to_decrypt)

    #prints decrypted data
    return  new_f.decrypt(test_decrypt)
    



#Create cryptography Key "password"
#key = Fernet.generate_key()
#print(f" Key: {key} \n")
##passwords
salt = os.urandom(16)

kdf = Scrypt(
    salt=salt,
    length=32,
    n=2**14,
    r=8,
    p=1,
)

key = kdf.derive(b"test")

# kdf = Scrypt(
#     salt=salt,
#     length=32,
#     n=2**14,
#     r=8,
#     p=1,
# )




#kdf.verify(b"test", key)



f = Fernet(key)

#new instance of Cryptography class
new_crypt = Cryptography(f, key)



# make a repl to search API and enter as many items that user wants
while True:


  ######User Login input

  new_user = User("test", b"pVIU3WJh3DwIbrE6j8F-DpV1pl9peagbzqYW0qy4O1Y=")

  user_login_select = input("What is your username?")


 # if new_user.user_name == user_login_select:
 #   print(f"Welcome {new_user} ")

#    test_key_input = input("Enter your key.")

 #   if new_user.password == str.encode(test_key_input):
#      print("Successful Login")
  #  else:
   #   print("unsucessful login")
  
  test_key_input = b"test"


#####API Search
  #data_to_encypt = input(b"What would you like to encrypt?")
  #search_input = input(f"Enter the type of alcohol you would like to see: ")
  search_input = ("rum")
  response = requests.get(f"http://www.thecocktaildb.com/api/json/v1/1/search.php?i={search_input}")

  data = response.json()

  test_data = data["ingredients"][0]["strIngredient"]
 
  print(f"returned data from API: {test_data}")

   
  #print(response.url)
  #print(response.text)
  #decrypted_output = new_crypt.my_decrypt(secret_lines_str, test_key_input)
 
  #test_key_input = input("Enter your key.")

  test_write = new_crypt.my_encrypt_method(test_data)

  #Add Encrypt to a list so user can encrypt multiple things

  break



#File access
file_location = "C:/Users/robot/pdx_code/bootcamp/class_tardigrade/code/travis/secret-list.txt"


with open(file_location, 'r', encoding="utf-8") as secret_file:
    secret_lines = secret_file.readlines()
  #  print(secret_lines)


    #take items out of returned file
    for items in secret_lines:
      secret_lines_str = items
      print(f" items from doc {secret_lines_str}")



      ##decodes item from document
      try:
        decrypted_output = new_crypt.my_decrypt(secret_lines_str, test_key_input)
        print(decrypted_output.decode())

      except InvalidToken:
        print("Invalid Token")
      except:
        print("error")




with open(file_location, 'w', encoding="utf-8") as secret_file_w:

  

  # test_dict_username = {
  #     "test" : ["", ""],
  #     "testing_user2" : ["encrypted message", ...]
  # }


  #est_dict_username[new_user.user_name][0] = test_write.decode()
  
  #secret_file_w.write(str(test_dict_username))

  try:
    secret_file_w.write(test_write.decode())

  except:
    print("Error in write")






#implement write. tie all input to the users key
