from ast import Index
from typing import Counter


filepath = 'code/lujock/contacts_12.csv'
with open(filepath, 'r') as file:
    lines = file.read().split('\n')
    # print(lines)


friends = []

keys = lines[0].split(',')
name = keys[0]
age = keys[1]
gender = keys[2]
race = keys[3]
# print(keys[1])
# print(keys[2])
# row = lines[1].split(',')
# print(row[1])

counter = 0
for row in lines:
    if counter == 0:
        counter += 1
    else:
        current_list = row.split(',')
        # print(current_list[0])
        name_dict = {name: current_list[0],
                     age: current_list[1],
                     gender: current_list[2],
                     race: current_list[3]
                
                     
                     }
        friends.append(name_dict)
print(friends)
       

    
