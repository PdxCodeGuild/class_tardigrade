"""Crypto buying app
 Idea is to be able to ask the user for a Cyrpto that they are interested in.
 Then the user can set a "buy" price and a sell price.
 The program should notify the user when the Crypto is at their buy or sale price.
 """
import cryptocompare
import twilio

print("Welcome to the Crypto Currency Buy-And-Sale-A-Tron")
coin = input("Please enter the ticker symbol for the Crypto you are interested in: ")



buy_price = input("At what price would you like to buy? ")
sale_price = input("At what price would you like to sale? ")


account_sid = "AC5ae2b44fa7ea31f4b18474bc353dca6c"
# Your Auth Token from twilio.com/console
auth_token  = "42b451bcb0d49f773160054605bdbbe5"
client = Client(account_sid, auth_token)

buy_message = client.messages \
    .create(
         body=f'The {coin} has reached your specified buying price of {buy_price}.',
         from_='+12184408410',
         to='+18016902294'
     )

sale_message = client.messages \
    .create(
         body=f'The {coin} has reached your specified buying price of {sale_price}.',
         from_='+12184408410',
         to='+18016902294'
     )
price = cryptocompare.get_price('DOGE', 'USD')

print(price)
if buy_price >= price:
    print(print(message.sid))
if sale_price <= price:
    print(sale_message.sid)