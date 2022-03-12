# filepath = '/Users/dartagnanchilders/Desktop/PDXCodeGuild/Bootcamp/class_tardigrade/code/dart/Python/contacts.csv'

# with open(filepath, 'r') as f:
#     contents = f.read().split('\n')

# headers = contents[0].split(',')
# rows = contents[1:]
# contacts = []

# for row in rows:
#     row = row.split(',') 
#     contact = {}
#     contact = dict(zip(headers, row))
#     contacts.append(contact)

# #-------------------------------------------------------------------------------------------------------     

# def create():
#     global headers
#     global contacts
#     contact = {}
#     for header in headers:
#         prompt = input(f'\nEnter the {header} of the contact: ')
#         contact[header] = prompt
#     contacts.append(contact)

# def retrieve(name):
#     global contacts
#     for contact in contacts:
#         if contact['name'] == name:
#             return contact
    
# def update(contact):
#     global headers
#     for header in headers:
#         value = input(f'\nEnter the value for {header} (it is currently {contact[header]}): ')
#         contact[header] = value

# def delete(contact):
#     global contacts
#     contacts.pop(contacts.index(contact))

# #-------------------------------------------------------------------------------------------------------      

# while True:
#     prompt = input('\nWelcome to the Contacts Database, would you like to [C]reate, [R]etrieve, [U]pdate, [D]elete or [Q]uit: ').lower()
#     if prompt not in ['c', 'r', 'u', 'd', 'q']:
#         print('\nPlease enter a valid command!')
#         continue
#     elif prompt == 'q':
#         print('\nThanks for using the contacts database!\n')
#         break
#     elif prompt == 'c':
#         create()
#     elif prompt == 'r':
#         name = input('\nWhich contact would you like to view? ')
#         contact = retrieve(name)
#         if contact is None:
#             print('\nNo such contact in these records.')
#             continue
#         for header in headers:
#             print(f'\n{header}: {contact[header]}')
#     elif prompt == 'u':
#         name = input('\nWhich contact would you like to update? ')
#         contact = retrieve(name)
#         if contact is None:
#             print('\nNo such contact in these records.')
#             continue
#         update(contact)
#     elif prompt == 'd':
#         name = input('\nWhich contact would you like to delete? ')
#         contact = retrieve(name)
#         if contact is None:
#             print('\nNo such contact in these records.')
#             continue
#         delete(contact)

# #-------------------------------------------------------------------------------------------------------          

# output = ','.join(headers)
# for contact in contacts:
#     output += '\n'
#     output += ','.join(contact.values())

# # print(output)

# with open(filepath, 'w') as f:
#     f.write(output)



contact_list = []
file_path = r'/Users/dartagnanchilders/Desktop/PDXCodeGuild/Bootcamp/class_tardigrade/code/dart/Python/contacts.csv'

with open(file_path, 'r') as csv_file:
    rows = csv_file.read().split('\n')
    headers = rows[0].split(',')
    for r, contact in enumerate(rows):
        split = rows[r].split(',')
        if r > 0:
            entry = {headers[0]: split[0], headers[1]: split[1], headers[2]: split[2]}
            contact_list.append(entry)

def create():
    name = input("\nEnter new contact's name: ").lower()
    fruit = input(f"\nEnter {name}'s favorite fruit: ").lower()
    color = input(f"\nEnter {name}'s favorite color: ").lower()

    new_entry = {headers[0]: name, headers[1]: fruit, headers[2]: color}
    contact_list.append(new_entry)

    print(f'''\nThe following contact has been added: \n
{name}, whose favorite fruit is {fruit} and favorite color is {color}.''')


def retrieve():
    ls = []
    retrieve_name = input('\nWhose record would you like to retrieve? Enter a name: ').lower()
    with open(file_path, 'r') as csv_file:
        rows = csv_file.read().split('\n')
        headers = rows[0].split(',')
        for r, contact in enumerate(rows):
            split = rows[r].split(',')
            if r > 0:
                entry = {headers[0]: split[0], headers[1]: split[1], headers[2]: split[2]}
                ls.append(entry)
    
    for x in ls:
        if retrieve_name == x['name']:
            print(f'''\nContact information is as follows: \n
name: {x['name']} fruit: {x['fruit']} color: {x['color']}''')

def update():
    update_name = input('\nEnter name of the record you want to update: ').lower()
    for x in contact_list:
        if update_name == x['name']:
            new_information = input('\nWhat information would you like to update? \nname, fruit or color: ').lower()
            
            if new_information  == 'name' or new_information == 'name':
                new_name = input('\nWhat is the new name?: ').lower()
                x['name'] = new_name
            if new_information  == 'fruit' or new_information == 'fruit':
                new_fruit = input('\nWhat is the new fruit?: ').lower()
                x['fruit'] = new_fruit
            if new_information  == 'color' or new_information == 'color':
                new_color = input('\nWhat is the new color?: ').lower()
                x['color'] = new_color

def delete():
    delete_name = input('\nEnter name of the record you want to delete: ').lower()
    for c, person in enumerate(contact_list):
        if delete_name == person['name']:
            contact_list.pop(contact_list.index(contact))

while True:
    user = input('''\nWelcome to the Contacts Database!
\nWould you like to [C]reate, [R]etrieve, [U]pdate, [D]elete or [Q]uit: ''').lower()
    
    if user == 'quit' or user == 'q':
        break

    elif user == 'create' or user == 'c':
       create()
        
    elif user == 'retrieve' or user == 'r':
        retrieve()

    elif user == 'update' or user == 'u':
        update()

    elif user == 'delete' or user == 'd':
        delete()

    else:
        print('\nEnter either [C]reate, [R]etrieve, [U]pdate, [D]elete or [Q]uit.')

with open(file_path, 'w') as file:
    file.write('name,fruit,color')
    for x in contact_list:
        file.write('\n')
        file.write(x['name'])
        file.write(',')
        file.write(x['fruit'])
        file.write(',')
        file.write(x['color'])