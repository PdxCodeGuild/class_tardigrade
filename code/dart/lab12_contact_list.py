
file_path = "/Users/dartagnanchilders/Desktop/pdx_code/FS_bootcamp/class_tardigrade/code/dart/"

with open(file_path + "contacts.csv", "r") as file:
    lines = file.read().split('\n')
    # print(lines)

# pull index 0 or name, favorite fruit and favorite color
x = lines[0]
# print(x)

# make headers
headers = x.split(", ")
# print(headers)

data = lines[1::]
# print(data)

contact_dictionary = []

for row in data:
    counter = 0
    contact = {}

    row_split = row.split(",")
    # print(row_split)

    for i in row_split:
        contact[headers[counter]] = i
        counter += 1
    contact_dictionary.append(contact)

print(contact_dictionary)