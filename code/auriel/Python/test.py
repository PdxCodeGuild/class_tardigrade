import csv
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
    contact_1 = rows[1].split(',')
    contact_2 = rows[2].split(',')
    contact_3 = rows[3].split(',')
    
    entry_1 = {headers[0]: contact_1[0], headers[1]: contact_1[1], headers[2]: contact_1[2]}
    contact_list.append(entry_1)
    entry_2 = {headers[0]: contact_2[0], headers[1]: contact_2[1], headers[2]: contact_2[2]}
    contact_list.append(entry_2)
    entry_3 = {headers[0]: contact_3[0], headers[1]: contact_3[1], headers[2]: contact_3[2]}
    contact_list.append(entry_3)

# Version 2 and 3 of lab (Create a CRUD REPL)
while True:
    user = input('''
    Hello, would you like to:
    Create, Retrieve, Update or Delete a record?
    If you would like to quit, please type 'quit' ''')
    
    if user == 'quit' or user == 'Quite':
        break

    elif user == 'create' or user == 'Create':
        with open(file_path, 'a') as csv_file:
            csv_file.write('\n')
            fname = input('Please enter a first name for new record: ')
            csv_file.write(f'{fname}')
            lname = input('Please enter a last name for new record: ')
            csv_file.write(f',{lname}')
            city = input('Please enter a city for new record: ')
            csv_file.write(f',{city}')
           
    elif user == 'retrieve' or user == 'Retrieve':
        retrieval_list = []
        retrieve_fname = input('Whos record would you like to retrieve? Please enter a first name: ')
        retrieval_list.append(retrieve_fname)
        retrieve_lname = input('Please enter a last name: ')
        retrieval_list.append(retrieve_lname)
            


    elif user == 'update' or user == 'Update':
        update_fname = input('Please enter first name of the record you want to update: ')
        update_lname = input('Please enter last name of the record you want to delete: ')

    elif user == 'delete' or user == 'Delete':
        delete_fname = input('Please enter first name of the record you want to delete: ')
        delete_lname = input('Please enter last name of the record you want to delete: ')

    else:
        print('Please enter one of the options listed')