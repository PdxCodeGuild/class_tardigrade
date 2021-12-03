
# with open('code/pete/python/examples/csv/cities.csv', 'r') as f:
#     lines = f.read().split('\n')
# print(lines)

# cities = [ # you want to build a list of dictionaries (like this)
#            # from the string you get from the csv file
#     {'name': 'portland', 'food': 'jojos', 'climate': 'temperate'},
#     {'name': 'kansas city', 'food': 'bbq', 'climate': 'temperate'},
#     {'name': 'lima', 'food': 'ceviche', 'climate': 'tropical'},
# ]



import sys
import csv

i = 'code/Shad/contact.csv'

with open(i, 'r',encoding='utf-8') as file:
    lines = file.read().split('\n')
    print(lines)

    print('\n')



    headers = lines[0].split(',')


con = [] 

for i in range(1,len(lines)):
    #iterate over the people
    #make a dictionary for each person
    contact = {}
    for h in range(len(headers)):
        #itereate over person contact details
        #turn details into a list
        #match hearder with corresponding details
        
        person=lines[i].split(',')
        contact[headers[h]] = person[h]
    con.append(contact)
        # print(headers[h])

print(con)
    # print(lines[i])
# for lis in lines:
#     
#     # contact_list=lis.split(',')
#     # print(contact_list[1])
#     # for i, u in enumerate(contact_list):
#     #     print(u,i)
#     # contact_list=lis.split(',')
# print(con)



# k = 'code/Shad/contact.csv'

def main():
   menu()

def menu():
    print()

    choice = int(input("""
                      1: Read File
                      2: Update the file
                      3: Quit

                      Please choose: """))

    if choice == 1:
        read_file()
    elif choice == 2:
        Update_the_File()
    elif choice == 3:
        sys.exit
    else:
        print("Please try again")
        menu()

def read_file():
    with open(k, "r") as read:
        view = csv.reader(read, delimiter=',')
        for x in view:
            print(x)
        read.close()

    
def Update_the_File():
    
    new = []
    

    with open(k, "w", newline="\n") as read1:
        view1 = csv.writer(read1, delimiter = ",")
        view1.writerow(input(" "))
        
        
        
      
        
   
   
main()
        



# be on your branch git checkout [[branch-name]] to switch between branches
# git pull origin main pulls main and merges it into your branch
# do some stuff (make files, change files, do programming, etc.)
# git add . adds everything in the current directory/folder OR git add code/pete/lab01.py add just one file OR git add -A adds everything in the repo
# git commit -m "commit message!!" make the commit
# git push push to github
# When you’ve completed a lab, go to github and make a pull request to pull your branch into main