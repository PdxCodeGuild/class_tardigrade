"""
Python Mini Capstone
Encrypted shopping search and list
Author: Travis Jackson
Date: 12 13 21

"""
import requests
from cryptography.fernet import Fernet

#access secure data using "py -m pip install cryptography"


####mini capstone features:
#pull data from website. then edit, then encrypt to document then decrypt.
# include class and methods
#create password, hash to key
#repl to enter data, retrieve data



class Cryptography():

  def __init__(self,f, key):

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



  def my_decrypt(self, data_to_decrypt):
    """
    decrypt data
    """

    decrypt_key_input = input("What is your key?" )

    #turn to bytes
    decrypt_key = str.encode(decrypt_key_input)


    new_f = Fernet(decrypt_key)

    #turns data back to bytes
    test_decrypt = str.encode(data_to_decrypt)

    #prints decrypted data
    print(f"decrypted data {(new_f.decrypt(test_decrypt))} \n")
    



#Create cryptography Key "password"
key = Fernet.generate_key()
print(f" Key: {key} \n")


f = Fernet(key)

#new instance of Cryptography class
new_crypt = Cryptography(f, key)



# make a repl to search API and enter as many items that user wants
while True:

  #data_to_encypt = input(b"What would you like to encrypt?")
  #search_input = input(f"Enter the type of alcohol you would like to see: ")
  search_input = ("gin")
  response = requests.get(f"http://www.thecocktaildb.com/api/json/v1/1/search.php?i={search_input}")

  data = response.json()

  test_data = data["ingredients"][0]["strIngredient"]
 
  print(f"returned data {test_data}")

   
  #print(response.url)
  #print(response.text)
 
  test_write = new_crypt.my_encrypt_method(test_data)

  #Add Encrypt to a list so user can encrypt multiple things

  break



#File access
file_location = "C:/Users/robot/pdx_code/bootcamp/class_tardigrade/code/travis/secret-list.txt"
with open(file_location, 'r', encoding="utf-8") as secret_file:
    secret_lines = secret_file.readlines()
    print(secret_lines) # ['First line\n', 'Second line\n']

    #take items out of returned file

    for items in secret_lines:
      secret_lines_str = items

      new_crypt.my_decrypt(secret_lines_str)



#implement write. tie all input to the users key

#with open(file_location, 'w', encoding="utf-8") as secret_file_w:
 #   secret_file_w.write(test_write.decode())







