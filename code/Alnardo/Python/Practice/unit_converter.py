# Unit Converter Optional Lab

measurements = {
    "ft": 0.3048, 
    "mi": 1609.34,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
}

foot = measurements["ft"]
mile = measurements["mi"]
kilometer = measurements["km"]
yard = measurements["yd"]
inch = measurements["in"]

choice = input('What would you like to calculate into meters? \nFoot\nMile\nKilometer\nYard\nInch: ')


# option_A = int(input('What is the distance in feet?: '))
# option_B = int(input('What is the distance in miles?: '))
# option_C = int(input('What is the distance in kilometers?: '))
# option_D = int(input('What is the distance in yards?: ')) 
# option_E = int(input('What is the distance in inches?: '))

  
if choice == 'foot' or choice == 'Foot':
    option_A = 'What is the distance in feet?: '
    foot_to_meters = int(input(option_A))
    total = foot_to_meters * foot
    print(f'Your total is {total} meters!')

elif choice == 'mile' or choice == 'Mile':
    option_B = 'What is the distance in miles?: '
    miles_to_meters = int(input(option_B))
    total = miles_to_meters * mile
    print(f'Your total is {total} meters!')

elif choice == 'kilometer' or choice == 'Kilometer':
    option_C = 'What is the distance in kilometers?: '
    kilometers_to_meters = int(input(option_C))
    total = kilometers_to_meters * kilometer
    print(f'Your total is {total} meters!')

elif choice == 'yard' or choice == 'Yard':
    option_D = 'What is the distance in yards?: '
    yards_to_meters = int(input(option_D))
    total = yards_to_meters * yard
    print(f'Your total is {total} meters!')

elif choice == 'inch' or choice == 'Inch':
    option_E = 'What is the distance in inches?: '
    inches_to_meters = int(input(option_E))
    total = inches_to_meters * inch
    print(f'Your total is {total} meters!')


print('Thank you for using this calculator, come again soon!')