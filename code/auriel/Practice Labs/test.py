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
    print(rows)
    for r, contact in enumerate(rows):
        split = rows[r].split(',')
        print(r, split)