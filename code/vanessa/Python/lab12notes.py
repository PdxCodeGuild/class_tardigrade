with open('Python\contacts2.csv','r') as file:
    line = file.read().split('\n')  #getting list of individual lines
    header = (line[0].split(","))
travel_history = []                 #making a list to loop lines for new list of dictionaries
name=(header[0])
color=(header[1])
fruit=(header[2])
print(name, color, fruit)


first= input("write something: ")
second= input("write something: ")
third= input("write something: ")
new_dict =  {name: first,
            color: second,
            fruit:  third,
                    }
print(new_dict)
travel_history.append(new_dict)
print(travel_history)

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

