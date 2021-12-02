# Version 1 of lab
contact_list = []
file_path = r'code/auriel/Python/contact_list_auriel.csv'

with open(file_path, 'w') as csv_file:
    csv_file.write('first_name,last_name,city')
    csv_file.write('\njazmin,cofield,baltimore')
    csv_file.write('\nauriel,cofield,atlanta')
    csv_file.write('\nlisa,moore,edgewood')

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
    with open(file_path, 'a') as csv_file:
        csv_file.write('\n')
        fname = input('Please enter a first name for new record: ').lower()
        csv_file.write(f'{fname}')
        lname = input('Please enter a last name for new record: ').lower()
        csv_file.write(f',{lname}')
        city = input('Please enter a city for new record: ').lower()
        csv_file.write(f',{city}')

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

while True:
    user = input('''
Hello, would you like to:
Create, Retrieve, Update or Delete a record?
If you would like to quit, please type 'quit' ''').lower()
    
    if user == 'quit':
        break

    elif user == 'create':
       create()
        
    elif user == 'retrieve' or user == 'Retrieve':
        retrieve()

    elif user == 'update' or user == 'Update':
        update_fname = input('Please enter first name of the record you want to update: ')
        update_lname = input('Please enter last name of the record you want to delete: ')

    elif user == 'delete' or user == 'Delete':
        delete_fname = input('Please enter first name of the record you want to delete: ')
        delete_lname = input('Please enter last name of the record you want to delete: ')

    else:
        print('Please enter one of the options listed')