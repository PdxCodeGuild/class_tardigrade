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



input_name = input("What is your name? ")
input_relation = input("What is your relation to Vanessa? ")
input_origin = input("What is your country of origin? ")
input_number = input("How many countries have you visited? ")
input_countries = input("Which countries have you visited (including home country if travel has been done domestically)? please separate by comma: ")

