with open('vanessa\contacts.csv','r') as file:
    line = file.read().split('\n')  #getting list of individual lines
    header = (line[0].split(","))
travel_history = []                 #making a list to loop lines for new list of dictionaries
# print(header,type(header))
print(line)

for i in range(1,len(line)):
    profile= {}

    for j in range(len(header)):
        # print(header[j])
        print(line[i],type(line[i]))
# for strings in lines:
    # traveler_data = {}              #dictionary
    # traveler_list = strings.split()
    # traveler_data.keys(strings)
    # print(traveler_data)

#iterate over list of lines to get through each person
#iterate over header list

