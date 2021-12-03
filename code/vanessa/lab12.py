with open('vanessa\contacts.csv','r') as file:
    line = file.read().split('\n')  #getting list of individual lines
    header = (line[0].split(","))
travel_history = []                 #making a list to loop lines for new list of dictionaries
name=(header[0])
color=(header[1])
fruit=(header[2])


profile=[]

counter = 0
for row in line:
    if counter == 0:
        counter +=1
    else:
        current_row= row.split(",")
        
        name_dict= {name: current_row[0],
                    color: current_row[1],
                    fruit: current_row[2]
                    }
        profile.append(name_dict)
print(profile)


# for i in range(1,len(line)):
#     print(i[1])
#     profile= {}
#     for j in range(len(header)):                       
#         (header[0])

# for strings in lines:
#     traveler_data = {}              #dictionary
#     traveler_list = strings.split()
#     traveler_data.keys(strings)
#     print(traveler_data)

# #iterate over list of lines to get through each person
# #iterate over header list

