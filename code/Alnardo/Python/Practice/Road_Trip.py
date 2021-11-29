#Road Trip

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

options = 'Your options are Boston, New York, Albany, Portland, Philadelphia'

print(options)
message = input('What city would you like to go to?: ')
# print(message)

going_to = city_to_accessible_cities[message]
print(f'Cities connected to {message} are {going_to}')

for city in going_to:
    hop2 = city_to_accessible_cities.get(city)
    print(hop2)