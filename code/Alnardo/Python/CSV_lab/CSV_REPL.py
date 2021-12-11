#CSV CRUD REPL
from typing import final


relative_path = 'github/class_tardigrade/code/Alnardo/Python/CSV_lab/'
welcome = 'Welcome to the Countries list!'
print(welcome)
question = input('Would you like to start? (yes/no): ')
# print(welcome)
with open('countries2.csv', 'r') as f:
    lines = f.read().split('\n')
    f.close()
# print(lines)
# print(choice)


countries_list = []
dict_keys = lines[0].split(', ')
# countries_dict = {}
headers = []
for key in dict_keys:
    # print(key)
    headers.append(key)
#     # print(i)
# print(headers)

# print(lines)
for line in lines:
    line = line.split(', ')
    if headers == line:
        continue
    elif headers != line:
        # print(line)
        countries_dict_main = {}
        countries_dict_one = {}
        countries_dict_two = {}
        countries_dict_three = {}
        countries_dict_four = {}
        for i, word in enumerate(line):
            # print(i, word)
            if i == 0:
                countries_dict_one[headers[i]] = line[i]
            elif i == 1:
                countries_dict_two[headers[i]] = line[i]
            elif i == 2:
                countries_dict_three[headers[i]] = line[i]
            elif i == 3:
                countries_dict_four[headers[i]] = line[i]

            countries_dict_main.update(countries_dict_one)
            countries_dict_main.update(countries_dict_two)
            countries_dict_main.update(countries_dict_three)
            countries_dict_main.update(countries_dict_four)
            if i == 3:
                countries_list.append(countries_dict_main)


while question == 'yes':
    choice = input('What would you like to do?: [C]reate, [R]etrieve, [U]pdate, or [D]elete: ').lower()
    if choice == 'create' or choice == 'c':
        created_list = []
        created_main = {}
        created_country = {}
        created_attraction = {}
        created_capital = {}
        created_climate = {}
        while len(created_list) < 4:
            created_choice = input('Please enter the country, attraction, capital and climate in order one at a time: ')
            created_list.append(created_choice)
        for i, word in enumerate(created_list):
            if i == 0:
                created_country[headers[i]] = word
            elif i == 1:
                created_attraction[headers[i]] = word
            elif i == 2:
                created_capital[headers[i]] = word
            elif i == 3:
                created_climate[headers[i]] = word
            created_main.update(created_country)
            created_main.update(created_attraction)
            created_main.update(created_capital)
            created_main.update(created_climate)
            
            if i == 3:
                countries_list.append(created_main)
        # print(countries_list)
        # choice = input('Would you like to continue? (yes/no): ')
    if choice == 'retrieve' or choice == 'r':
        country_key = input("What country would you like to see?: ")
        for i in range(len(countries_list)):
            if country_key != countries_list[i]['country']:
                continue
            else:
                print(countries_list[i])
            # print(countries_list[i]['country']
    if choice == 'update' or choice == 'u':
        country_key = input('What country would you like to update?: ')
        for i in range(len(countries_list)):
            if country_key != countries_list[i]['country']:
                continue
            else:
                key_selection = input('What would you like to change? (country, attraction, capital, climate): ').lower()
                changed_value = input('What would you like to change it to?: ')
                countries_list[i][key_selection] = changed_value
        # print(countries_list)
    if choice == 'delete' or choice == 'd':
        country_key = input('What country would you like to delete?: ')
        for i in range(len(countries_list)):
            if country_key != countries_list[i]['country']:
                continue
            else:
                del countries_list[i]
                break
        # print(countries_list)
    question = input('Would you like to continue? (yes/no): ')

print('Thank you for using this list!\nHave a great day')



final_form = (f'{headers[0]}, {headers[1]}, {headers[2]}, {headers[3]}\n')
# print(final_form)
for lists in countries_list:
    # print(lists)
    country = lists['country']
    # print(country)
    attraction = lists['attraction']
    capital = lists['capital']
    climate = lists['climate']
    list_to_string = (f'{country}, {attraction}, {capital}, {climate}')
    final_form += list_to_string + '\n'



with open('countries3.csv', 'w') as f:
    f.write(final_form)


