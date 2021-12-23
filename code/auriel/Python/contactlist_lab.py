# Version 1 of lab
contact_list = []
file_path = r'code/auriel/Python/contact_list_auriel copy.csv'

with open(file_path, 'r') as csv_file:
    rows = csv_file.read().split('\n')
    headers = rows[0].split(',')
    for r, contact in enumerate(rows):
        split = rows[r].split(',')
        if r > 0:
            entry = {headers[0]: split[0], headers[1]: split[1], headers[2]: split[2]}
            contact_list.append(entry)

# Version 2 and 3 of lab (Create a CRUD REPL)
def create():
    fname = input('Please enter a first name for new record: ').lower()
    lname = input('Please enter a last name for new record: ').lower()
    city = input('Please enter a city for new record: ').lower()

    new_entry = {headers[0]: fname, headers[1]: lname, headers[2]: city}
    contact_list.append(new_entry)

    print(f'''The following contact has been added: \n
    firstname: {fname} lastname: {lname} city: {city}''')


def retrieve():
    ls = []
    retrieve_fname = input('Whos record would you like to retrieve? Please enter a first name: ').lower()
    retrieve_lname = input('Please enter a last name: ').lower()
    with open(file_path, 'r') as csv_file:
        rows = csv_file.read().split('\n')
        headers = rows[0].split(',')
        for r, contact in enumerate(rows):
            split = rows[r].split(',')
            if r > 0:
                entry = {headers[0]: split[0], headers[1]: split[1], headers[2]: split[2]}
                ls.append(entry)
    
    for x in ls:
        if retrieve_fname == x['first_name'] and retrieve_lname == x['last_name']:
            print(f'''Contact information is as follows: \n
            firstname: {x['first_name']} lastname: {x['last_name']} city: {x['city']}''')

def update():
    update_fname = input('Please enter first name of the record you want to update: ').lower()
    update_lname = input('Please enter last name of the record you want to update: ').lower()
    for x in contact_list:
        if update_fname == x['first_name'] and update_lname == x['last_name']:
            new_information = input('What information would you like to update? \nFirst name, last name or city: ').lower()
            
            if new_information  == 'first name' or new_information == 'firstname':
                new_fname = input('What is the new first name?: ').lower()
                x['first_name'] = new_fname
            if new_information  == 'last name' or new_information == 'lastname':
                new_lname = input('What is the new last name?: ').lower()
                x['last_name'] = new_lname
            if new_information  == 'city' or new_information == 'city':
                new_city = input('What is the new city?: ').lower()
                x['city'] = new_city

def delete():
    delete_fname = input('Please enter first name of the record you want to delete: ').lower()
    delete_lname = input('Please enter last name of the record you want to delete: ').lower()
    for c, person in enumerate(contact_list):
        if delete_fname == person['first_name'] and delete_lname == person['last_name']:
            del contact_list[c]

while True:
    user = input('''
Hello, would you like to:
Create, Retrieve, Update or Delete a record?
If you would like to quit, please type 'quit' ''').lower()
    
    if user == 'quit':
        break

    elif user == 'create':
       create()
        
    elif user == 'retrieve':
        retrieve()

    elif user == 'update':
        update()

    elif user == 'delete':
        delete()

    else:
        print('Please enter one of the options listed')

with open(file_path, 'w') as file:
    file.write('first_name,last_name,city')
    for x in contact_list:
        file.write('\n')
        file.write(x['first_name'])
        file.write(',')
        file.write(x['last_name'])
        file.write(',')
        file.write(x['city'])