"""Lab 12: Contact List

Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and
go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV, convert the
lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys,
the text in the other lines represent the values.
  """

with open(r"C:\Users\dhols\Documents\GitHub\class_tardigrade\code\Dustin\jedi-sith.txt", "r") as file:
    lines = file.read().split('\n')


headers = lines[0].split(',')
#print(headers)

force_users = lines[1:]

#print(force_users)
for user in force_users:
    user = user.split(',')
    jedi_dict = {}
    for i in range(len(headers)):

        jedi_dict[headers[i]] = user[i]

    print(jedi_dict)

#for line in lines






