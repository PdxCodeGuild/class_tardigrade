
# with open('code/pete/python/examples/csv/cities.csv', 'r') as f:
#     lines = f.read().split('\n')
# print(lines)

# cities = [ # you want to build a list of dictionaries (like this)
#            # from the string you get from the csv file
#     {'name': 'portland', 'food': 'jojos', 'climate': 'temperate'},
#     {'name': 'kansas city', 'food': 'bbq', 'climate': 'temperate'},
#     {'name': 'lima', 'food': 'ceviche', 'climate': 'tropical'},
# ]



from sqlite3 import Row
import sys
import csv

# k = 'contact.csv'
# with open('contact.csv', encoding='utf-8') as file:
#     lines = file.read().split('\n')
#     # print(lines)

#     # print('\n')
# print(f'lines{lines}')


# headers = lines[0].split(',')


# con = [] 

# for i in range(1,len(lines)):
#     #iterate over the people
#     #make a dictionary for each person
#     contact = {}
#     # for h in range(len(headers)):
#     #     #itereate over person contact details
#     #     #turn details into a list
#     #     #match hearder with corresponding details
        
#     #     person=lines[i].split(',')
#     #     contact[headers[h]] = person[h]
#     # con.append(contact)
    
#     # print(headers[h])

#     # print(con)
#     # print(lines[i])

# # for lis in lines:
    
#     # contact_list=lis.split(',')
#     # print(contact_list[1])
#     # for i, u in enumerate(contact_list):
#     #     print(u,i)
#     # contact_list=lis.split(',')
# print(con)

# print(f'lines{lines}')

k = 'Python\Lab 12\contact.csv'

def main():
   menu()

def menu():
    print()

    choice = int(input("""
                      1: Read File
                      2: Add file
                      3: Delete
                      4: Quit

                      Please choose: """))

    if choice == 1:
        read_file()
    elif choice == 2:
        Add_File()
    elif choice == 3:
        delete()
    elif choice == 4:
        sys.exit
    else:
        print("Please try again")
        menu()

def read_file():
    """reads .csv-formatted file and returns list of dictionaries
    contacts_list = read_file()"""
    with open(k, 'r',encoding='utf-8') as file:
        lines = file.read().split('\n')
    headers = lines[0].split(',')
    
    con = [] # return con

    for i in range(1,len(lines)):
        #iterate over the people
        #make a dictionary for each person
        contact = {}
        person=lines[i].split(',')
        for h in range(len(headers)):
            #itereate over person contact details
            #turn details into a list
            #match hearder with corresponding details
        
            
            contact[headers[h]] = person[h]
        con.append(contact)
        

        print(con[-1] )
        print('contact.csv')
        
    
    
    
def Add_File():
    
    new = []
    # diction = {}
    # h = open('contact.csv', 'w')
    # nu = csv.writer(h)
    # nu.writerow(Row)


    names=input('Please enter name: ')
    new.append(names)    
    fruits=input('Please enter fruit: ')
    new.append(fruits)    
    colors=input('Please enter color: ')
    new.append(colors)
    for i in range(len(new) + 1):
        print(i)
        new[i]
    
    # new.append(input(f"{names}\n{fruits}\n{colors} "))
    with open("contact.csv", "a", newline='') as p:

        wr = csv.writer(p, dialect='excel')
        wr.writerow(new)

        
        
    # return names and fruits and colors
        
def delete():
    con = []  
    with open(k, 'r',encoding='utf-8') as file:
        lines = file.read().split('\n')
    
    headers = lines[0].split(',')

    for i in range(1,len(lines)):

        #iterate over the people
        #make a dictionary for each person
        contact = {}
        for h in range(len(headers)):

            person=lines[i].split(',')
            contact[headers[h]] = person[h]
    con.append(con)
    d = input('please enter name to delete: ')
    del contact[ d ]      
def update():
    con = []  
    with open(k, 'r',encoding='utf-8') as file:
        lines = file.read().split('\n')
    
    headers = lines[0].split(',')

    for i in range(1,len(lines)):

        #iterate over the people
        #make a dictionary for each person
        contact = {}
        for h in range(len(headers)):

            person=lines[i].split(',')
            contact[headers[h]] = person[h]
    con.append(contact)
    contact.update()


   
   
main()
        



# be on your branch git checkout [[branch-name]] to switch between branches
# git pull origin main pulls main and merges it into your branch
# do some stuff (make files, change files, do programming, etc.)
# git add . adds everything in the current directory/folder OR git add code/pete/lab01.py add just one file OR git add -A adds everything in the repo
# git commit -m "commit message!!" make the commit
# git push push to github
# When you’ve completed a lab, go to github and make a pull request to pull your branch into main