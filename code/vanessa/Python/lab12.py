
with open('contacts2.csv', 'r') as travel_doc:
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
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Welcome to Vanessa's and friend's travel history repository")

def create():
    input_name = input("What is your name? ")
    input_relation = input("What is your relation to Vanessa? ")
    input_origin = input("What is your country of origin? ")
    input_residence = input("What is the country of residence? ")
    input_number = input("How many countries have you visited? (digit only) ")
    input_countries = input("Which countries have you visited (including home country if travel has been done domestically)? please separate by comma: ")
    
    # created_record=(f'{input_name},{input_relation},{input_origin},{input_number},{input_countries}')
    
    # created_record= created_record.split(", \n")
    created_record= {
                'name': input_name,
                'relation': input_relation,
                'country of origin': input_origin,
                'country of residence': input_residence,
                'number of countries visited': input_number,
                'countries visited': input_countries
                }
                   # use total_histories.update()???
    total_histories.append(created_record)
    print(total_histories)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def update():
    update_record1= input("Whose record would you like to update? ")
    for person in total_histories:
        if person['name'] == update_record1:
            update= input("What would you like to update? [n]ame, [r]elation, [c]ountry of origin, country of r[e]sidence, n[u]mber of countries visited, or countries [v]?').lower() ")
            if update == 'n':
                new_name= input('please enter replacement name: ')
                person['name']= new_name
                print(person['name'])
                print(person)
                break

            if update == 'r':
                new_relation= input('please enter relationship type: ')
                person['relation']= new_relation
                print(person['relation'])
                print(person)
                break

            if update == 'c':
                new_origin= input('please enter new country of origin: ')
                person['country of origin']= new_origin
                print(person['country of origin'])
                print(person)
                break
            if update == 'e':
                new_residence= input('please enter new country of residence: ')
                person['country of residence']= new_residence
                print(person['country of residence'])
                print(person)
                break
            if update ==  'u':
                new_number= input('please enter new number of countries visited: ')
                person['number of countries visited']= new_number
                print(person['number of countries visited'])
                print(person)
                break
            if update == 'v':
                country = input('please enter correct country/ies visited. Seperate by comma: ')
                person['countries visited']= country
                print(person['countries visited'])
                print(person)
                break
            # print(update)
            # print(total_histories(update))

def print_all():
    for each in total_histories:
        print(each['name'], each ['relation'], each['country of origin'], each['country of residence'], each['number of countries visited'], each ['countries visited'])
        

def retrieve():
    print("Options: ")
    for each in total_histories:
        print(each["name"])
    retrieve_record = input("Whose travel history would you like to see? ")
    for person in total_histories:
        if person['name'] == retrieve_record:
            return person
        elif person['name'] == retrieve_record:
            print("Sorry. Person not found.")

def delete_items():
    print("Options: ")
    for each in total_histories:
        print(each["name"])
    delete_record= input('Whose travel history do you wish to delete? warning: this will delete entire record... ')
    for each in total_histories:
        if each["name"] == delete_record:
            total_histories.pop((total_histories.index(each)))

def save():
    string = ''.join([str(item) for item in total_histories])
    print('converting list to string')
    print(string)

    with open('contacts2.csv','w') as travel_doc:
        travel_doc.write(string)

    with open('contacts2.csv', 'r') as travel_doc:
        test = travel_doc.read().split("\n")
    print(test)
    return

      
def quit():
    
    print("Thanks- Safe travels!")
    return

while True:
    command = input('Would you like to [c]reate [u]pdate, [r]etrieve individual record, [p]rint all, [d]elete, [s]ave or [q]uit? ').lower()
    if command not in ["c","u","r","d","q"]:
        print("please enter 'c' 'u' 'r' 'd' 'p' 'q' 's' commands only.")
    if command == 'c':
        create()
    if command == 'u':
        update()
        print(" update complete")
    if command == 'r':
        print(retrieve())
    if command == 'p':
        print_all()
    if command == 'd':
        delete_items()
    if command == 's':
        save()
        print("changes saved")
    if command == 'q':
        quit()
        break