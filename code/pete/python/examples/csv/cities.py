with open('code/pete/python/examples/csv/cities.csv', 'r') as f:
    lines = f.read().split('\n')
print(lines)

cities = [ # you want to build a list of dictionaries (like this)
           # from the string you get from the csv file
    {'name': 'portland', 'food': 'jojos', 'climate': 'temperate'},
    {'name': 'kansas city', 'food': 'bbq', 'climate': 'temperate'},
    {'name': 'lima', 'food': 'ceviche', 'climate': 'tropical'},
]

headers = lines[0].split(',')
print(headers)
cities = lines[1:]
print(cities)
for city in cities:
    print(city.split(','))
    city_dict = {}
    # loop over city.split(',') or headers to make key-value pairs for a dictionary