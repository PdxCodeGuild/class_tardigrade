unit_to_meter = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}



unit_from = input('enter unit to convert to meters: ')

units = int(input('enter number to convert: '))

result = units * unit_to_meter[unit_from]
# print(units * unit_to_meter[unit_from])
# print(unit_to_meter[unit_to])
print(result)