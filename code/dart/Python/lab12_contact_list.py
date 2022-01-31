
file_path = "/Users/dartagnanchilders/Desktop/pdx_code/FS_bootcamp/class_tardigrade/code/dart/contacts.csv"
file_path_2 = "/Users/dartagnanchilders/Desktop/pdx_code/FS_bootcamp/class_tardigrade/code/dart/contacts_2.csv"

with open(file_path, "r") as file: # opens the contacts.csv file
    lines = file.read().split("\n")
    # print(lines)

contacts = []

def convert_csv_file_to_list_of_dicts(): # convert csv to a list of dictionaries
    headers = lines[0].split(",")

    lst_of_lsts = []

    for line in lines:
        values = line.split(",")
        key_value_pairs = dict(zip(headers, values))
        contacts.append(key_value_pairs)
    
    for list in lst_of_lsts:
        contacts.append({
            headers[0]: list[0],
            headers[1]: list[1],
            headers[2]: list[2]
        })
    return contacts

#----------------------------------------------------------------------------------------------------------------#

def view_contact(): # Retrieve a contact's information
    contact_search = input("\nEnter the name of the contact you would like to view: ").lower()
    for contact in contacts:
        if contact["name"] == contact_search:
            print("\nRetrieving Contact...")
            print(f"\n{contact}")
            return contact
        
    print("\nContact not found.")

#----------------------------------------------------------------------------------------------------------------#

def create_contact(): # Create a new contact and add it to the contacts list
    input_name = input("\nEnter new contact's name: ")
    input_fruit = input(f"\nEnter {input_name}'s favorite fruit: ")
    input_color = input(f"\nEnter {input_name}'s favorite color: ")

    contact_dict = {
        "name": input_name, 
        "favorite_fruit": input_fruit, 
        "favorite_color": input_color
    }

    contacts.append(contact_dict)

    print("\nCreating new contact...")
    print()
    print(contact_dict)

#----------------------------------------------------------------------------------------------------------------#

def update_contact(): # Update a contact's information
    record_to_update = view_contact()
    update_question = input(f"\nWould you like to update this record? \"yes\" or \"no\": ")
    if update_question == "yes":
        attribute_to_update = input("\nWhat section would you like to update? Choose \"name\", \"favorite fruit\", or \"favorite color\": ")
        new_attribute = input(f"\nWhat would you like to change the {attribute_to_update} to: ")
        for x in range(len(contacts)):
            if contacts[x] == record_to_update:
                entry = contacts[x]
                entry[attribute_to_update] = new_attribute
                print(f"\n{entry}")
                break
    else:
        print("No new changes made")

#----------------------------------------------------------------------------------------------------------------#

def delete_contact(): # Delete or remove a contact from the contact's list
    record_to_delete = view_contact()
    delete_question = input(f"\nAre you sure you want to delete this record? \"Yes\" or \"No\": ")
    if delete_question == "yes".lower():
        contacts.remove(record_to_delete)
        return contacts
    else:
        print(f"{record_to_delete} was not deleted")

#----------------------------------------------------------------------------------------------------------------#

def convert_list_of_dicts_back_to_csv_file(): # convert list of dictionaries back to csv file
    headers = [key for key in contacts[0]]
    # contact_str = ",".join(headers) + "\n"
    contact_str = ""
    counter = 0
    for contact in contacts:
        counter += 1
        if len(contacts) == counter:
            contact_str += f"{contact[headers[0]]},{contact[headers[1]]},{contact[headers[2]]}"
        else:
            contact_str += f"{contact[headers[0]]},{contact[headers[1]]},{contact[headers[2]]}\n"
    print(contact_str)
    return contact_str

#----------------------------------------------------------------------------------------------------------------#

contacts = convert_csv_file_to_list_of_dicts()

print("\nWelcome to the contacts list!".title())

while True:
    user_action = input("""\nTo view a contact, enter \"View\",\
 to create a new contact, enter \"Create\",\
 to update a contact's information, enter \"Update\",\
 to delete a contact, enter \"Delete\" or to QUIT the program, enter \"Quit\": """).lower()

    if user_action not in ['view', 'create', 'update', 'delete']:
        print("""Please enter \"View\" to view a contact,\
\"Create\" to create a new contact,\
\"Update\" to update a contact's information\
or \"Delete\" to delete a contact.""")

    if user_action == "View".lower():
        view_contact()
    
    if user_action == "Create".lower():
        create_contact()

    if user_action == "Update".lower():
        update_contact()
    
    if user_action == "Delete".lower():
        delete_contact()

    if user_action == "quit".lower():
        break

updated_contacts = convert_list_of_dicts_back_to_csv_file()

with open(file_path_2, "w") as file:
    file.write(updated_contacts)