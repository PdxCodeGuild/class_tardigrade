from numpy import save


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
        
    for people, header in zip(row, banner):

        con[header] =  people
    con = dict(zip(banner, row))
    contact.append(con) 
    print(contact[-1])

# con = []      
#     # contact_list=lis.split(',')
#     # print(contact_list[1])
#     # for i, u in enumerate(contact_list):
#     #     print(u,i)
#     # contact_list=lis.split(',')


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
        name = input('enter name: ')
        for con in contact:
            if con['Name'] == name:
                for header in banner:
                    print(f'{header}:{con[header]}', )
        read_file(name)
    elif choice == 2:
        Add_File(contact)
    elif choice == 3:
                    
        delete()
        
    # elif choice == 4:

    #     Quit()
    else:
        print("goodbye")
        menu()

def read_file(name):
    
    with open(k, 'r',encoding='utf-8') as file:
        lines = file.read().split('\n')
    headers = lines[0].split(',')
    
    con = [] # return con

    
        #iterate over the people
        #make a dictionary for each person
        
       #itereate over person contact details
            #turn details into a list
            #match hearder with corresponding details 

    
    rows = read_[1:]

    banner = read_[0].split(',')
    for row in rows: 
        row = row.split(',') 
        con = {} 
        for i, header in enumerate(banner):
            con[header] = row[0]
            
        for people, header in zip(row, banner):

            con[header] =  people
        con = dict(zip(banner, row))
        contact.append(con) 
             
    
def Add_File(contact):

    
     

    # contact = []
      
    # Fruits=input('Please enter fruit: ')
    # contact.append(Fruits)    
    # colors=input('Please enter color: ')
    # contact.append(colors)


    # with open('contact.csv', 'r') as f:
    
    #         read_ = f.read().split('\n')

    

    # reader_obj = csv.DictReader(f)
    # # ames = reader_obj.fieldnames
    # # print(ames)
    # for row in reader_obj:
    #     print(row)

    # rows = read_[1:]

    # banner = read_[0].split(',')
    
    # for head in header: 
    #     # row = row.split(',') 
    #     con = {} 
        
        # for i, header in enumerate(banner):
        #     con[header] = row[0]

           
        # for people, header in zip(row, banner):
        Names=input('Please enter contact info: ')
        Fruit=input('Please enter contact fruit: ')
        color=input('Please enter contact color: ')
        diction = {'Name': Names,'Fruit': Fruit,'color': color}

      
        #     con = dict(zip(banner, row))
        
        contact.append(diction)
        print(diction)
        
        print(contact[-1])
            
        # for header in banner:
       
        
def delete():

    Name = input('enter nam')
    with open('contact.csv', 'r') as readFile:

        reader = csv.reader(readFile)
        for row in reader:
            contact.append(row)
            for field in row:
                if field == Name:
                    contact.remove(row)

                         
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