"""Crypto buying app
 Idea is to be able to ask the user for a Cyrpto that they are interested in.
 Then the user can set a "buy" price and a sell price.
 The program should notify the user when the Crypto is at their buy or sale price.
 """
import cryptocompare
print("Welcome to the Crypto Currency Buy-And-Sale-A-Tron")
coin = input("Please enter the ticker symbol for the Crypto you are interested in: ")

buy_price = input("At what price would you like to buy? ")
sale_price = input("At what price would you like to sale? ")

price = cryptocompare.get_price('DOGE', 'USD')

print(price)

