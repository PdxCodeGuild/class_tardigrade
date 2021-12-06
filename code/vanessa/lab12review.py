with open('vanessa\contacts2.csv', 'r') as travel_doc:
    traveler_history = travel_doc.read().split("\n")
    header =(traveler_history[0].split(","))
    

total_histories= [] 

for persons_data in traveler_history[1:]:
    each_list= (persons_data.split(','))
    (each_list) #printing out each list
    for j in range(len(header)):       #does it have to be header? yes, because headers are our keys (at least this way?)
        profile= {}       
        profile [header[0]]= each_list[0] 
        profile [header[1]]= each_list[1]
        profile [header[2]]= each_list[2]
        profile [header[3]]= each_list[3]
        profile [header[4]]= each_list[4]
        profile [header[5]]= each_list[5].split()
        
    total_histories.append(profile)
print(total_histories)
    