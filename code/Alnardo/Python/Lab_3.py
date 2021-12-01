#Lab 3

# x = int(0.75 * 100)
# print(x, type(x))
# Basis for this lab

"""
change = float(input('How much change do you have?: '))
total = 0

change = int(change * 100)
quarters = change // 25
dimes = ((change - (quarters * 25)) // 10) 
# print(dimes)
nickles = ((change - (quarters * 25) - (dimes * 10)) // 5)
pennies = ((change - (quarters * 25) - (dimes * 10) - (nickles * 5) // 1))
# print(pennies)
print(f'You have {quarters} quarters, {dimes} dimes, {nickles} nickles, and {pennies} pennies')
"""


# Version 2
coins = [
    ('quarter', 25),
    ('dime', 10),
    ('nickle', 5),
    ('penny', 1)
]
# print(coins) [('penny', 1), ('nickle', 5), ('dime', 10), ('quarter', 25)]
# print(coins[2][1]) #Calling individual tokens inside tuples!

change = float(input('How much change do you have?: '))
change = int(change * 100)

for coin_tuple in coins:
    coin = coin_tuple[0]
    value = coin_tuple[1]
    amount = change // value
    change = change - (value * amount)
    print(f'there are {amount} {coin}')


# while change > 0:
#     quarters = change // coins[3][1]
#     change = change - (quarters * 25)
#     dimes = change // coins [2][1]
#     change = change - (dimes * 10)
#     nickles = change // coins [1][1]
#     change = change - (nickles * 5)
#     pennies = change // coins [0][1]
#     change = change - pennies


# print(f'You have {quarters} {coins[3][0]}, {dimes} {coins[2][0]}, {nickles} {coins[1][0]}, and {pennies} {coins[0][0]}!')




# print(change // coins[3][1])
# print(coins[3])
# while change > 0:
#     if change % 25 == 0:
# for coin in coins:
#     print(coin[])