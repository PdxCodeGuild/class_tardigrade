
import sys
import csv

i = './contact.csv'
k='contact.csv'

# with open(i, newline='') as file:
# k='contact.csv'

with open('contact.csv', 'r') as f:
    
    read_ = f.read().split('\n')
contact = []
    # reader_obj = csv.DictReader(f)
    # # ames = reader_obj.fieldnames
    # # print(ames)
    # for row in reader_obj:


    #     print(row)
      


rows = read_[1:]

banner = read_[0].split(',')
for row in rows: 
    row = row.split(',') 
    con = {} 
    for i, header in enumerate(banner):
        con[header] = row[0]
        
    for value, header in zip(row, banner):

        con[header] =  value
    con = dict(zip(banner, row))
    contact.append(con) 
    print(contact[-1])


# con = [] 

# for i in range(1,len(lines)):
#     #iterate over the people
#     #make a dictionary for each person
#     contact = {}
#     for h in range(len(headers)):
#         #itereate over person contact details
#         #turn details into a list
#         #match hearder with corresponding details
        
#         person=lines[i].split(',')
#         contact[headers[h]] = person[h]
#     con.append(contact)
        #  print(header[h])

# print(con)
    # print(lines[i])
# for lis in lines:
#     
#     # contact_list=lis.split(',')
#     # print(contact_list[1])
#     # for i, u in enumerate(contact_list):
#     #     print(u,i)
#     # contact_list=lis.split(',')
# print(con)

# print(f'lines{lines}')

# k = 'Lab 12\contact.csv'

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
        name = input('enter nam')
        for con in contact:
            if con['Name'] == name:
                for header in banner:
                    print(f'{header}:{con[header]}', )
        read_file(name)
    elif choice == 2:
        Add_File()
    elif choice == 3:
        name = input(f'enter name ')
        
        
        delete(name)
        
    elif choice == 4:
        sys.exit
    else:
        print("Please try again")
        menu()

def read_file(name):
    
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
     
       
    
    
    
def Add_File():
    
    new = []
    diction = {}
    Names=input('Please enter name: ')
    new.append(Names)    
    Fruits=input('Please enter fruit: ')
    new.append(Fruits)    
    colors=input('Please enter color: ')
    new.append(colors)
    with open("contact.csv", "a+", newline=' ') as p:
        
        wr = csv.writer(p)
        
        wr.writerow(new)
   
         
    # for header in banner:
    #     user = input(f'enter name ')
    #     con[header] = user
    # contact.append(diction)
        
def delete(name):
    
    user2= read_file(name)
    contact.pop(contact.index(user2))

        #iterate over the people
        #make a dictionary for each person
        # contact = {}
    #     for h in range(len(headers)):

    #         person=lines[i].split(',')
    #         contact[headers[h]] = person[h]
    # con.append(contact)
    # d = input('please enter name to delete: ')
    # del contact[ d ]      
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