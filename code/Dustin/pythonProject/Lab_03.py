print("Make Change")

user_input = float(input("Enter dollar amount: "))
user_input = int(user_input /.01)
quarters = user_input//25
user_input = user_input%25
dimes = user_input//10
user_input = user_input%10
nickels = user_input//5
user_input = user_input%5
pennies = user_input

print(quarters, dimes, nickels, pennies)

"""Below is dictionary for version 2 assuming i get back to it"""

coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]
# print(coins[2][1])

