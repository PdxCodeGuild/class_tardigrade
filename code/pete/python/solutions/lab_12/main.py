filepath = 'code/pete/python/solutions/lab_12/cities.csv'
# test = 'code/pete/python/solutions/lab_12/cities_test.csv'
with open(filepath, 'r') as f:
    contents = f.read().split('\n')

# headers is the first line of the .csv file, split into a list
headers = contents[0].split(',')
# rows is a list of the 2nd to last lines of the .csv file
rows = contents[1:]
# start off with an empty list to add the dictionaries to
cities = []

for row in rows: # loop over the rows
    row = row.split(',') # each row, a string, is split into another list
    city = {} # an empty dictionary to start the  city
    # for i, header in enumerate(headers): # loop over headers and indicies of headers
    #     # add the key/value pair to the dictionary
    #     city[header] = row[i]
    # for value, header in zip(row, headers): # zip creates an iterator of tuples to give access ot value and header
    #     city[header] = value
    city = dict(zip(headers, row))
    cities.append(city) # add city to cities list

def create():
    """creates a new city and appends it to the list"""
    global headers
    global cities
    city = {}
    for header in headers:
        prompt = input(f'Enter the {header} of the city: ')
        city[header] = prompt
    cities.append(city)

def retrieve(name):
    """given a city's name, returns that city's dictionary, if it exists"""
    global cities
    for city in cities:
        if city['name'] == name:
            return city
    
def update(city):
    """given a city, loops over the values and asks the user for new ones"""
    global headers
    for header in headers:
        value = input(f'Enter the value for {header} (currently {city[header]}): ')
        city[header] = value

def delete(city):
    """given a city, pops it from the cities list"""
    global cities
    cities.pop(cities.index(city))


while True:
    prompt = input('Welcome to the cities database, would you like to [C]reate, [R]etrieve, [U]pdate, [D]elete or [Q]uit: ').lower()
    if prompt not in ['c', 'r', 'u', 'd', 'q']:
        print('Please enter a valid command!')
        continue
    elif prompt == 'q':
        print('Thanks for using the cities database.  Have an okay day.')
        break
    elif prompt == 'c':
        create()
    elif prompt == 'r':
        name = input('Which city would you like to view? ')
        city = retrieve(name)
        if city is None:
            print('No such city in these records.')
            continue
        for header in headers:
            print(f'{header}: {city[header]}')
    elif prompt == 'u':
        name = input('Which city would you like to update? ')
        city = retrieve(name)
        if city is None:
            print('No such city in these records.')
            continue
        update(city)
    elif prompt == 'd':
        name = input('Which city would you like to delete? ')
        city = retrieve(name)
        if city is None:
            print('No such city in these records.')
            continue
        delete(city)


output = ','.join(headers) # start with the csv-formatted headers
for city in cities: # and for every city...
    output += '\n' # add a new line
    output += ','.join(city.values()) # and add the values joined as a csv string

print(output)

with open(filepath, 'w') as f:
    f.write(output)