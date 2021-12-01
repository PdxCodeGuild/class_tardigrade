
file_path = "/Users/dartagnanchilders/Desktop/pdx_code/FS_bootcamp/class_tardigrade/code/dart/"

with open(file_path + "contacts.csv", "r") as file:
    lines = file.read().split('\n')

contact_list = []

key_list = lines[0].split(",")
# print(key_list)

for i in range (1, len(lines), 1):
    lines[i] = lines[i].split(",")

for i in range(1, len(lines)):
    entry = dict(zip(key_list, lines[i]))
    contact_list.append(entry)
# print(contact_list, "contact dictionary")

# make a new record
def new_record():
    add_name = input("\nWhat is the name: ")
    add_fav_fruit = input("\nWhat is their favorite fruit: ")
    add_fav_color = input("\nWhat is their favorite color: ")

    contact_list.append({"name": add_name, "favorite_fruit": add_fav_fruit, "favorite_color": add_fav_color})

    print(f"\nNew record: {add_name, add_fav_fruit, add_fav_color}")
    print(f"\n{contact_list}")

    return add_name, add_fav_fruit, add_fav_color
