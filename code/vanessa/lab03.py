dollar_amount=input("what is the amount: ")
dollar_amount = float(dollar_amount)
print(dollar_amount)

every_cent = dollar_amount * 100

quarters = every_cent//25
print(f"{quarters} quarters")
quarters_remainder = every_cent % 25

dimes = quarters_remainder//10
print (f"{dimes} dimes")
dimes_remainder = quarters_remainder % 10


nickels = dimes_remainder//5
print (f'{nickels} nickels')
nickels_remainder = dimes_remainder%5

pennies = nickels_remainder//1
print (f'{pennies} pennies')
pennies_remainder = nickels_remainder%5