#CSV Lab

relative_path = 'github/class_tardigrade/code/Alnardo/Python/CSV_lab/'


with open('countries.csv', 'r') as f:
    lines = f.read().split('\n')
    # print(lines) #Lines comes back as a list, dont need to .append into a blank list

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

print(countries_list)