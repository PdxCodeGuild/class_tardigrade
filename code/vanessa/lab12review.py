with open('vanessa\contacts2.csv', 'r') as travel_doc:
    traveler_history = travel_doc.read().split("\n")
    # print(traveler_history[1:])
    header =(traveler_history[0].split(","))
    

total_histories= [] #list for new dictionaries

# run this loop for as many histories as you have
for persons_data in traveler_history[1:]:
    each_list= (persons_data.split(','))
    for j in range(len(header)):       
        profile= {}
                
        profile [header[0]]= each_list[0]
        profile [header[1]]= each_list[1]
        profile [header[2]]= each_list[2]
        profile [header[3]]= each_list[3]
        profile [header[4]]= each_list[4]
        profile [header[5]]= each_list[5]
        
    total_histories.append(profile)
print(total_histories)
    
# for i in range(1,len(lines)):