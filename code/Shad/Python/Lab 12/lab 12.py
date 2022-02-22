
def read_contact():
    with open('contacts.csv', 'r') as file:
        lines = file.read().split('\n')
    head = lines[0].split(',')
    contact_list = []
    for i in lines[1:]:
        contact_dict = {}
        info = i.split(',')
        if len(info)!=1:
            name = info[0]
            fruit = info[1]
            color = info[2]

            contact_dict[head[0]] = name
            contact_dict[head[1]] = fruit
            contact_dict[head[2]] = color
            contact_list.append(contact_dict)
    return contact_list

def menu():
    
    while True:
        print()

        choice = int(input("""
                          1: Read File
                          2: Add file
                          3: Delete
                          4: Update
                        
                          Please choose: """))

        if choice == 1:
            name = input('enter name: ')
            retrieve(name)
            
        elif choice == 2:
            Add_File()
            
        elif choice == 3:

            delete()

        elif choice == 4:
            update()
        
        select = input('Do you want to continue y/n: ')
        if select.upper() == 'Y':
            continue
        else:
            print('GoodBye')
            break

def update():
    name =  input('Enter the Name: ')
    attrb = int(input("""
                          1: Name
                          2: Fruit
                          3: Color
                        
                          Please choose to update: """))
    
    contact = read_contact()
    indx_update = -1
    for i in range(len(contact)):
        if contact[i]['Name']== name:
            indx_update = i
            break

    if indx_update!=-1:
        if attrb == 1:
            name = input('Enter New Name: ')
            contact[indx_update]['Name'] = name          

        elif attrb==2:
            fruit = input('Enter New fruit: ')
            contact[indx_update]['Fruit'] = fruit
        elif attrb==3:
            color = input('Enter New color: ')
            contact[indx_update]['color'] = color
        else:
            print('Wrong input..')
        
        file = open('contacts.csv','w')
        header = list(contact[0])
        head = header[0] + ',' + header[1] + ',' + header[2]
        file.write(head)
        file.write('\n')
        for info in contact:
            line = info['Name'] +','+info['Fruit'] +','+ info['color']
            file.write(line)
            file.write('\n')
        file.close()
    else:
        print('No Such Name found')

         
def retrieve(name):
    contact = read_contact()
#     print(contact)
    for i in contact:
        if i['Name']==name:
            print(f"Name: {name} Fruit: {i['Fruit']} Color: {i['color']}")
    
def Add_File():

        Names=input('Please enter Name: ')
        Fruit=input('Please enter fruit: ')
        color=input('Please enter color: ')
        diction = {'Name': Names,'Fruit': Fruit,'color': color}

        contact = read_contact()
        contact.append(diction)
        
        file = open('contacts.csv','w')
        header = list(contact[0])
        head = header[0] + ',' + header[1] + ',' + header[2]
        file.write(head)
        file.write('\n')
        for info in contact:
            line = info['Name'] +','+info['Fruit'] +','+ info['color']
            file.write(line)
            file.write('\n')
        file.close()
        
def delete():
    name = input('Enter the Name: ')
    contact = read_contact()
    indx_del = -1
    for i in range(len(contact)):
        if contact[i]['Name']== name:
            indx_del = i
            break
        
    if indx_del!=-1:
        _ = contact.pop(indx_del)
    
        file = open('contacts.csv','w')
        header = list(contact[0])
        head = header[0] + ',' + header[1] + ',' + header[2]
        file.write(head)
        file.write('\n')
        for info in contact:
            line = info['Name'] +','+info['Fruit'] +','+ info['color']
            file.write(line)
            file.write('\n')
        file.close()
    else:
        print('No Such Name found')

menu()






        
# be on your branch git checkout [[branch-name]] to switch between branches
# git pull origin main pulls main and merges it into your branch
# do some stuff (make files, change files, do programming, etc.)
# git add . adds everything in the current directory/folder OR git add code/pete/lab01.py add just one file OR git add -A adds everything in the repo
# git commit -m "commit message!!" make the commit
# git push push to github
# When you’ve completed a lab, go to github and make a pull request to pull your branch into main