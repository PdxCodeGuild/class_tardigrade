"""Crypto buying app
 Idea is to be able to ask the user for a Cyrpto that they are interested in.
 Then the user can set a "buy" price and a "sell" price.
 The program should notify the user when the Crypto is at their buy or sale price.
 """
#import required api

import cryptocompare
from twilio.rest import Client
import time
from secrets import token, sid
#intro

print("Welcome to the Crypto Currency Buy-And-Sale-A-Tron")

#user input, also in the future could get phone number if I wanted others to use it.
#for coin input need to do some safe guarding for people entering non valid options.
coin = input("Please enter the ticker symbol for the Crypto you are interested in: ")
coin = coin.upper()

#also here need to put in some protections if someone enters a non int or float
buy_price = float(input("At what price would you like to buy? "))
sell_price = float(input("At what price would you like to sell? "))


account_sid = sid
# Auth Token from twilio.com/console
auth_token  = token
client = Client(account_sid, auth_token)

price = cryptocompare.get_price( coin, 'USD')
x = price[coin]['USD']

# This section here will be for running the program unitl a text is sent then terminate.

def text_notify (condition, text): #defines function
    text_sent = True
    while text_sent == True:
       if condition: #checks the condition
        text
        text_sent = False
        time.sleep(600) #waits 10 min to run again


#check for price and sends message
#this needs to be timed and then terminated
if buy_price >= x:
    buy_message = client.messages \
        .create(
        body=f'The {coin} has reached your specified buying price of {buy_price}.',
        from_='+12184408410',
        to='+18016902294'
    )

if sell_price <= x:
    sell_message = client.messages \
        .create(
        body=f'The {coin} has reached your specified sellinging price of {sell_price}.',
        from_='+12184408410',
        to='+18016902294'
    )