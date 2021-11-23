user_money = float(input('Enter a dollar amount: '))
money = user_money / .01

if user_money <= 0:
    print('Error')
else:
    quarters = money // 25 # Divides user input and results in a whole number
    dimes = money % 25 // 10 # Recieves remainder after dividing by 25 and then divides that number by 10 and results a whole number
    nickels = money % 25 % 10 // 5 # Recieves remainder after dividing by 25 and then 10. Then divides that number by 5 and results a whole number
    pennies = money % 25 % 10 % 5 // 1 # Recieves remainder after dividing by 25 and then 10 and then 5. hen divides that number by 1 and results a whole number

print(f'You have {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies')
