


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
    
print(total_histories[0]["country of origin"])

# weather={"fall": "rainy",
#         "winter": "cold/overcast/stormy/dry",  
#         "spring": "rainy/warm",
#         "summer": " very warm" }    
# oregon= ("apples", "cheese", "ducks", "berries",weather)
# print(oregon[4]["winter"])

# def search():
#     """searches for key info"""
#     search_term= input("Which person's travel history would you like? ")
#     for name in total_histories:
#         if search_term in name ['name'].lower():
#             print(f" {name} relation to Vanessa is {relation},from {country of origin}, resides in {country of residence}, has visited {number of countries} and these include the following countries{countries visited}")

# print(search())

print("Welcome to Vanessa's and friend's travel history repository")




# input_name = input("What is your name? ")
# input_relation = input("What is your relation to Vanessa? ")
# input_origin = input("What is your country of origin? ")
# input_number = input("How many countries have you visited? ")
# input_countries = input("Which countries have you visited (including home country if travel has been done domestically)? please separate by comma: ")
