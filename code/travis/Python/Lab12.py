"""
Lab 12 Contact list
Author: Travis Jackson
Date: 12/3/21

"""
line_items_list = []
contact_list = []
contacts_dict = {}

#read csv
with open("./code/travis/contacts.csv", "r") as file:
    lines = file.read().split("\n")

#split lines by commas
for i, line in enumerate(lines):

    line_items_list.append(lines[i].split(","))


#add line items to dictionary adds to list
for i, item in enumerate(line_items_list):

    #skips headers
    if i == 0:
        pass

    else:
        contacts_dict = {}

        contacts_dict["name"] = item[0]
        contacts_dict["favorite food"] = item[1]
        contacts_dict["favorite color"] = item[2]
        contacts_dict["pet"] = item[3]

        contact_list.append(contacts_dict)



def create (name, food, color, pet):
    """
    creates a new entry in the dictionary
    """
    contacts_dict = {}

    contacts_dict["name"] = name
    contacts_dict["favorite food"] = food
    contacts_dict["favorite color"] = color
    contacts_dict["pet"] = pet
    contact_list.append(contacts_dict)
    print(name, " has been added.")



def retrieve(retrieve_input):
    """
    retrieves data based on user entry of a name
    
    """
    for i, item in enumerate(contact_list):
        
        search_dict = contact_list[i]           
            
        name = search_dict.get("name")

        if name == retrieve_input:
            print(contact_list[i])
            break
        

def update(name, attribute, new_value ):
    """
    update users entry
    
    """
    for i, entry in enumerate(contact_list):
    
        search_dict = contact_list[i]
        name = search_dict.get("name")

        if name == update_name:

            search_dict.update({attribute: new_value})
            print("The value has been updated")


def delete(delete_name):
    """
    Delete an entry
    """

    for i, entry in enumerate(contact_list):
    
        search_dict = contact_list[i]           
        
        name = search_dict.get("name")

        if name == delete_name:

            #delete whole list entry

            contact_list.pop(i)

            print(contact_list)
            break



### Version 3 ###

#Save list to CSV file
def save(contact_list):
    """
    Saves final file to CSV

    """
    #adds headers
    lines = "name,favorite food,favorite color,pet\n"
    testcount = len(contact_list)

    for i in range(testcount):
        
        test = contact_list.pop(0)
        testname = test.get("name")
        testfood = test.get("favorite food")
        testcolor = test.get("favorite color")
        testpet = test.get("pet")

        line = f"{testname},{testfood},{testcolor},{testpet}"


        if i < testcount - 1:
            lines += line + "\n"

        else:           
            lines += line
      
    with open("./code/travis/contacts.csv", "w") as write_contact_file:

        write_contact_file.write(lines)


###Version 2###

# REPL
while True:

    print("What would you like to do to the contact list?: ")
    user_input = input(" (c)reate, (r)etrieve, (u)pdate, (d)elete, or (q)uit and save? ")
    user_input.lower()

    #create
    if user_input == "c":
        print("Create:")
        
        create_name = input("Enter a name: ")
        create_food = input("Enter a favorite food: ")
        create_color = input("Enter a favorite color: ")
        create_pet = input("Enter a pet: ")

        create(create_name, create_food, create_color, create_pet)
        

    #retrieve
    elif user_input == "r":

        print("Retrieve")

        retrieve_input = input("Who do you want to find? ")
        retrieve_input.lower()

        retrieve(retrieve_input)       
            
            
    #Update record
    elif user_input == "u":
        print("Update:")

        update_name = input("Who do you want to update: ")
        update_name.lower()

        update_attribute = input("What would you like to change? ")
        update_attribute.lower()

        update_value = input("what is the new entry? ")
        update_value.lower()

        update(update_name, update_attribute, update_value)


    #Delete a record
    elif user_input == "d":
        print("Delete")

        delete_name = input("Who would you like to delete? ")
        delete_name.lower()

    
        delete(delete_name)

    #end repl and saves
    elif user_input == "q":

        print("Saving to CSV file")

        save(contact_list)
        break

    else:
        print('Please enter a "c" to create. "r" to retrieve. "u" to update. "d" to delete and a "q" to quit')

