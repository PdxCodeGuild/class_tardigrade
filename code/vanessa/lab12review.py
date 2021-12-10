


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
    
# print(total_histories[1])
# print(total_histories[4]["name"])
# print(total_histories[1]["countries visited"])
# print(total_histories[1]["country of origin"])


print("Welcome to Vanessa's and friend's travel history repository")

def create():
    new_record = input("What is your name? What is your relation to Vanessa? What is your country of origin? How many countries have you visited? Which countries have you visited (including home country if travel has been done domestically)? please seperate by comma except for countries visited(x y z): ")
    print(new_record)

def update():
    update_record1= input("Whose record would you like to update? ")
    print(update_record1)
    update_recordpart2= input("What would you like to update? ")
    print(total_histories(update_recordpart2))

def retrieve():
    print("Options: ")
    for each in total_histories:
        print(each["name"])
    retrieve_record = input("Whose travel history would you like to see? ")
    for person in total_histories:
        if person['name'] == retrieve_record:
            return person
        # elif person['name'] != retrieve_record:
        #     print("Sorry. Person not found.")

def delete():
    delete_record= input('Whose travel history do you wish to delete?')
    print(delete_record)

def quit():
    print("Thanks- Safe travels!")
    return

while True:
    command = input('Would you like to [c]reate [u]pdate, [r]etrieve, [d]elete or [q]uit? ').lower()
    if command not in ["c","u","r","d","q"]:
        print("please enter 'c' 'u' 'r' 'd' or 'q' commands only.")
    if command == 'c':
        create()
    if command == 'u':
        update()
    if command == 'r':
        retrieve()
    if command == 'd':
        delete()
    if command == 'q':
        quit()
        break