import csv

file_path = r'code/auriel/Python/contactlist_auriel.csv'
fieldnames = ['first_name', 'last_name', 'city', 'favorite_color']

with open(file_path, 'w', newline = '') as csv_file:
    fieldnames = ['first_name', 'last_name', 'city', 'favorite_color']
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'matt', 'last_name': 'jones', 'city': 'baltimore', 'favorite_color': 'blue'})
    writer.writerow({'first_name': 'lisa', 'last_name': 'lowes', 'city': 'chance', 'favorite_color': 'red'})
    writer.writerow({'first_name': 'amber', 'last_name': 'peterson', 'city': 'mitchellville', 'favorite_color': 'purple'})

with open(file_path, 'r') as file:
    lines = file.read().split('\n')
    print(lines)