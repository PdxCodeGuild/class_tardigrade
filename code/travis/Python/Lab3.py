"""
Lab3: Make change
Author: Travis Jackson
Date: 11/16/21

"""
coins = [
    ('quarters', 'quarter', 25),
    ('dimes', 'dime', 10),
    ('nickels', "nickel", 5),
    ('pennies', "penny", 1)
]

total_coin = []
list_output = []
output = " "
x = 0


money_input = input("Enter a dollar amount: ")
total_remaining = float(money_input) * 100


#fills list with the coin amount. Uses floor division
for coin in coins:

    coin_plural, coin_name, coin_value = coin 

    coin_amount = total_remaining  // coin_value 

    total_remaining = total_remaining - (coin_amount * coin_value)
    total_coin.append(int(coin_amount))
    

#display, checks for coin plurality
for amount in total_coin:

    if amount == 0:
        x += 1

    #accesses single coin name index
    elif amount == 1:
                    
        list_output.append(f"{amount} {coins[x][1]}")
        x += 1

    #accesses plural index
    elif amount > 1:

        list_output.append(f"{amount} {coins[x][0]}")
        x += 1


print(output.join(list_output)) 

