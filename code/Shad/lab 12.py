import csv

i = 'code/Shad/contact.csv'
contact = {}
with open(i, 'r',encoding='utf-8') as file:
    lines = file.read().split('\n')
    print(lines)

    # with open(i, 'w',newline='') as row:
    #     title =['name','fruit','color']
        
    #     write1= csv.DictWriter(row, title = title )
    #     write1.writeheader( )
    #     write1.writerow({'name': 'mike','fruit': 'apple','color': 'blue'})
    #     write1.writerow({'name': 'ike','fruit': 'pear','color': 'red'})
    #     write1.writerow({'name': 'tanjiro','fruit': 'passionfruit','color': 'green'})
    #     print(write1)


    with open("contact.csv", "w", newline="\n") as read1:
        view1 = csv.writer(read1, delimiter = ",")
        view1.writerow(input(" "))
        


