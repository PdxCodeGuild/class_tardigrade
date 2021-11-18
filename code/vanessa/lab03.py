dollar_amount=input("what is the amount: ")
dollar_amount = float(dollar_amount)
print(dollar_amount)

every_cent = dollar_amount * 100

quarters = every_cent//25
print(quarters)
quarters_remainder = every_cent % 25

dimes = quarters_remainder//10
print (dimes)
dimes_remainder = quarters_remainder % 10

pennies = dimes_remainder//1
print (pennies)