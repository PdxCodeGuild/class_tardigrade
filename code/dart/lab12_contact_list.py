
file_path = "/Users/dartagnanchilders/Desktop/pdx_code/FS_bootcamp/class_tardigrade/code/dart/contacts.csv"
file_path_2 = "/Users/dartagnanchilders/Desktop/pdx_code/FS_bootcamp/class_tardigrade/code/dart/contacts2.csv"
# open the contacts.csv file
with open(file_path, "r") as f:
    lines = f.read().split("\n")
    # print(lines)
def retrieve(user_input):
    # locates a user's information by their name
    for dict in contacts:
        for name in dict:
            if dict[name] == user_input:
                return dict

headers = lines[0].split(",")
# print(headers)
contacts = []

for line in lines:
    values = line.split(",")
    # print(values)
    key_value_pairs = dict(zip(headers, values))
    # print(pairs)
    contacts.append(key_value_pairs)
# create a loop to run thorugh the repl
loop_control = True
while loop_control == True: 
    user_action = input("""\nWhat would you like to do?\
 To create a new contact, enter \"Create\"\
 to retrieve a contact, enter \"Retrieve\"\
 to update a contact, enter \"Update\"\
 or to delete a contact, enter \"Delete\": """)

    if user_action == "Retrieve" or user_action == "retrieve":
        person = input("\nEnter the name of the contact you would like to retrieve and or view: ")
        final = retrieve(person)

        print("\nRetrieving Contact...")
        print(f"\n{final}")

        continuation_answer = input("\nIs there anything else you would like to do while you are here? Enter \"Yes\" or \"No\": ")

        if continuation_answer == "No" or continuation_answer == "no":
            loop_control == False
            break

    elif user_action == "Update" or user_action == "update":
        person = input("\nEnter the name of the contact whose information you would like to update: ")
        attribute = input("\nWould you like to update their name, favorite fruit or favorite color: ")
        value = input("\nWhat would you like to change it to: ")

        selected_dict = retrieve(person)

        selected_dict[attribute] = value
        print("\nUpdating Contact...")
        print(f"\n{selected_dict}")

        continuation_answer = input("\nIs there anything else you would like to do while you are here? Enter \"Yes\" or \"No\": ")

        if continuation_answer == "No" or continuation_answer == "no":
            loop_control == False
            break

    elif user_action == "Delete" or user_action == "delete":
        person = input("\nEnter the name of the contact you would like to delete: ")
        selected_dict = retrieve(person)
        contacts.remove(selected_dict)

        print("\nDeleting Contact...")

        continuation_answer = input("\nIs there anything else you would like to do while you are here? Enter \"Yes\" or \"No\": ")

        if continuation_answer == "No" or continuation_answer == "no":
            loop_control == False
            break

    elif user_action == "Create" or user_action == "create":
        name = input("\nEnter the new contact's name: ")
        fruit = input("\nEnter their favorite fruit: ")
        color = input("\nEnter their favorite color: ")

        contacts.append({
        "name": name,
        "favorite_fruit": fruit,
        "favorite_color": color,
    })
        
        print("\nCreating Contact...")
        print()
        print({"name": name, "favorite_fruit": fruit, "favorite_color": color})

        continuation_answer = input("\nIs there anything else you would like to do while you are here? Enter \"Yes\" or \"No\": ")

        if continuation_answer == "No" or continuation_answer == "no":
            loop_control == False
            break

for contact in contacts:

    keys = list(contact.keys())

names = []

for contact in contacts:
    for key in keys:
        names.append(contact[key])

final = keys + names

final_output = ",".join(final)

words = final_output.split(",")
new_line = ""
word_count = 0

for word in words:
    new_line += word + ","
    word_count += 1
    
    if word_count == 3: 
        new_line += "\n"
        word_count = 0

with open(file_path, "w") as f:
        f.write(new_line)

# final_list = "".join(contacts)

with open(file_path_2, "w") as f:
        f.write(contacts).split("\n")