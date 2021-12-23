Convert_amount = input("enter a amount: ")
Convert_amount = float(Convert_amount)
print(Convert_amount)


pennies = Convert_amount  * 100
print(pennies, 'pennies')
print(pennies // .01)

dimes = Convert_amount * 40
print(dimes, 'dimes')
print(dimes // .10)

quarters = Convert_amount * 60
print(quarters, 'quarters')
print(quarters // .25)

nickel = Convert_amount * 20
print(nickel, 'nickel')
print(nickel // .5)

half_dollar = Convert_amount * 50
print(half_dollar, 'half dallar')
print(half_dollar // .50)

print(f'{quarters}, quarters')