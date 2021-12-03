# Version 1 of lab

contact_list = []
file_path = r'code/auriel/Python/contact_list_auriel.csv'

with open(file_path, 'r') as csv_file:
    rows = csv_file.read().split('\n')
    headers = rows[0].split(',')
    for r, contact in enumerate(rows):
        split = rows[r].split(',')
        if r > 0:
            entry = {headers[0]: split[0], headers[1]: split[1], headers[2]: split[2]}
            contact_list.append(entry)


print(type(rows))


updated_clist = []

for w, people in enumerate(contact_list):
    print(people)