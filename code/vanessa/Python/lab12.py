
from bokeh.core.has_props import C


with open('Python\contacts2.csv', 'r') as travel_doc:
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
    
    

print("Welcome to Vanessa's and friend's travel history repository")

def create():
    input_name = input("What is your name? ")
    input_relation = input("What is your relation to Vanessa? ")
    input_origin = input("What is your country of origin? ")
    input_number = input("How many countries have you visited? (digit only)")
    input_countries = input("Which countries have you visited (including home country if travel has been done domestically)? please separate by comma: ")
    new_record=(f'{input_name},{input_relation},{input_origin},{input_number},{input_countries}')
    new_record= new_record.split(", \n")
    print(new_record)
    # make_dict = [header[0]]
    # #NEED to turn input into dictionary first before appending to list. Then add to csv w/out spaces.
    # print(new_record.split(", \n"))
    # # total_histories.append(new_record)
    # # print(total_histories)
    # # with open('vanessa\contactupdate.csv','a') as travel_doc:
    # #     travel_doc.write(new_record)

    

def update():
    update_record1= input("Whose record would you like to update? ")
    for person in total_histories:
        if person['name'] == update_record1:
            update= input("What would you like to update? [n]ame, [r]elation, [c]ountry of origin, country of [r]esidence, n[u]mber of countries visited, or countries [v]?').lower() ")
            if update == 'n':
                print("n")
                print(total_histories[4]["name"])
            if update == 'r':
                print("r")
            if update == 'c':
                print("c")
            if update == 'r':
                print("r")
            if update ==  'u':
                print("u")
            if update == 'v':
                print("v")
            print(update)
    print(total_histories(update))

def retrieve():
    print("Options: ")
    for each in total_histories:
        print(each["name"])
    retrieve_record = input("Whose travel history would you like to see? ")
    # print(total_histories)
    for person in total_histories:
        if person['name'] == retrieve_record:
            return person
        elif person['name'] == retrieve_record:
            print("Sorry. Person not found.")

def delete():
    print("Options: ")
    for each in total_histories:
        print(each["name"])
    delete_record= input('Whose travel history do you wish to delete? warning: this will delete entire record... ')
    for each in total_histories:
        if (each["name"]) == delete_record:
          total_histories.pop(delete_record)
        #     print(total_histories)
           
    #         print(total_histories)
    #     if each_person== total_histories[1]:
    #         total_histories.pop(1)
    #         print(total_histories)
    #     if each_person== total_histories[2]:
    #         total_histories.pop(2)
    #         print(total_histories)
    #     if each_person== total_histories[3]:
    #         total_histories.pop(3)
    #         print(total_histories)
    #     if each_person== total_histories[4]:
    #         total_histories.pop(4) 
    #         print(total_histories)       
        
        #     print(total_histories.remove([i[delete_record]])#remove dict from list
        # if delete_record == "vanessa": #might want to try removing by index with another reverse dictionary? 
            # print(i)
            


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
        print(update())
    if command == 'r':
        print(retrieve())
    if command == 'd':
        delete()
    if command == 'q':
        quit()
        break