"""
Lab 12 Contact list
Author: Travis Jackson
Date: 12/1/21

"""

line_items_list = []
contact_list = []
contacts_dict = {}

#read csv
with open("C:/Users/robot/pdx_code/bootcamp/class_tardigrade/code/travis/contacts.csv", "r") as file:
    lines = file.read().split("\n")

#split lines by commas
for i, line in enumerate(lines):

    line_items_list.append(lines[i].split(","))

#add line items to dictionary
for item in line_items_list:
    contacts_dict = {}

    contacts_dict["Name"] = item[0]
    contacts_dict["Favorite food"] = item[1]
    contacts_dict["Favorite color"] = item[2]
    contacts_dict["Pet"] = item[3]
    contact_list.append(contacts_dict)


def create (name, food, color, pet):
    contacts_dict = {}

    contacts_dict["Name"] = name
    contacts_dict["Favorite food"] = food
    contacts_dict["Favorite color"] = color
    contacts_dict["Pet"] = pet
    contact_list.append(contacts_dict)
    print(name, " has been added.")



#Version 2

testfind = {}

while True:

    print("What would you like to do to the contact list?: ")
    user_input = input("Create, Retrieve, Update, Delete, or quit? ")

    user_input.lower()

    #create
    if user_input == "c":
        print("Create:")
        
        create_name = input("Enter a name: ")
        create_food = input("Enter a favorite food: ")
        create_color = input("Enter a favorite color: ")
        create_pet = input("Enter a pet: ")

        create(create_name, create_food, create_color, create_pet)
        print(contact_list)

    #retrieve
    if user_input == "r":

        print("Retrieve")

        retrieve_input = input("Who do you want to find? ")

        for i, entry in enumerate(contact_list):
        
            testfind = contact_list[i]
            teststring = testfind.get("Name")

            if teststring == retrieve_input:
                print(contact_list[i])
                break
            
            
    #Update record



    #Delete a record
    

    #end repl

    if user_input == "q":
        break