
cents = int(float(input('Enter a dollar amount: ')) * 100)
# print(cents)

quarters = cents // 25
cents = cents % 25
dimes = cents // 10
cents %= 10
nickles = cents // 5
cents %= 5

print(f'{quarters} quarters, {dimes} dimes,{nickles} nickles,{cents} pennies')


