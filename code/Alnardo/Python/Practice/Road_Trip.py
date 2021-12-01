#Road Trip

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philly'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philly': {'New York'}
}
hop1 = ''
listed_hop1 = []
hop2 = ''
listed_hop2 = []
options = 'Your options are Boston, New York, Albany, Portland, Philly'

print(options)
message = input('What city would you like to start?: ')
# print(message)

going_to = city_to_accessible_cities[message]
# print(going_to)
for city in going_to:
    hop1 = hop1 + ', ' + city
    listed_hop1.append(city)
if hop1.startswith(', '):
        hop1 = hop1.strip(', ')
print(f"Cities connected to {message} are \n{hop1}")


# for city in listed_hop1:
#     hop2 = city_to_accessible_cities[city]
#     print(hop2)

print(f"Cities connected to {hop1} are:")


for city in listed_hop1:
    hop2 = city_to_accessible_cities.get(city)
    print(hop2)

