filepath = '/Users/dartagnanchilders/Desktop/PDXCodeGuild/Bootcamp/class_tardigrade/code/dart/Python/contacts.csv'

with open(filepath, 'r') as f:
    contents = f.read().split('\n')

headers = contents[0].split(',')
rows = contents[1:]
contacts = []

for row in rows:
    row = row.split(',') 
    contact = {}
    contact = dict(zip(headers, row))
    contacts.append(contact)

#-------------------------------------------------------------------------------------------------------     

def create():
    global headers
    global contacts
    contact = {}
    for header in headers:
        prompt = input(f'\nEnter the {header} of the contact: ')
        contact[header] = prompt
    contacts.append(contact)

def retrieve(name):
    global contacts
    for contact in contacts:
        if contact['name'] == name:
            return contact
    
def update(contact):
    global headers
    for header in headers:
        value = input(f'\nEnter the value for {header} (it is currently {contact[header]}): ')
        contact[header] = value

def delete(contact):
    global contacts
    contacts.pop(contacts.index(contact))

#-------------------------------------------------------------------------------------------------------      

while True:
    prompt = input('\nWelcome to the Contacts Database, would you like to [C]reate, [R]etrieve, [U]pdate, [D]elete or [Q]uit: ').lower()
    if prompt not in ['c', 'r', 'u', 'd', 'q']:
        print('\nPlease enter a valid command!')
        continue
    elif prompt == 'q':
        print('\nThanks for using the contacts database!\n')
        break
    elif prompt == 'c':
        create()
    elif prompt == 'r':
        name = input('\nWhich contact would you like to view? ')
        contact = retrieve(name)
        if contact is None:
            print('\nNo such contact in these records.')
            continue
        for header in headers:
            print(f'\n{header}: {contact[header]}')
    elif prompt == 'u':
        name = input('\nWhich contact would you like to update? ')
        contact = retrieve(name)
        if contact is None:
            print('\nNo such contact in these records.')
            continue
        update(contact)
    elif prompt == 'd':
        name = input('\nWhich contact would you like to delete? ')
        contact = retrieve(name)
        if contact is None:
            print('\nNo such contact in these records.')
            continue
        delete(contact)

#-------------------------------------------------------------------------------------------------------          

output = ','.join(headers)
for contact in contacts:
    output += '\n'
    output += ','.join(contact.values())

# print(output)

with open(filepath, 'w') as f:
    f.write(output)