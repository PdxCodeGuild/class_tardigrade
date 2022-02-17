
amount= float(input('Enter a dollar amount: '))

total_pennies = amount/.01

quarters = total_pennies//25
remaining_pennies= total_pennies%25

dimes= remaining_pennies//10
remaining_pennies= remaining_pennies%10

nickels = remaining_pennies//5
remaining_pennies= total_pennies%5


print(total_pennies, "pennies")
print(quarters, "quarter")
print(dimes, 'dimes')
print(nickels, 'nickels')
print(remaining_pennies, 'pennies')
print(10%2)
print(10%3)