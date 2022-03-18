"""
Lab 17: Quotes API

For this lab we'll be using the Favqs Quotes API to first get a random quote, and then allow the user to find quotes by ' \
'keyword. To accomplish this we'll be using the requests library.
Version 1: Get a Random Quote

The URL to get a random quote is https://favqs.com/api/qotd, send a request here, parse the JSON in the response into
a python dictionary, and show the quote and the author.
"""
import time
import requests
#Version 1
"""
url = 'https://favqs.com/api/qotd'
headers = {
    'accept': 'application/json'
}

response = requests.get(url, headers=headers)
data = response.json()
quote = data["quote"]
words = quote["body"]
who = quote["author"]

print(f"{who}, once said '{words},' wise words.")
"""
#Version 2

while True:
    user_input = input("Enter a term  for a related quote here or 'stop' to exit: ")
    if user_input == 'stop':
        break
    url = "https://favqs.com/api/quotes?page=<page>&filter=<keyword>"
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    params = {
        "filter": user_input,
        "page": 1,
    }
    response = requests.get(url + f"/search/{user_input}", headers=headers, params=params)
    data = response.json()


    quote = data["quotes"]
    for words in quote:
        print(f'{words["author"]}, once said, "{words["body"]},"'+ "\n")
        time.sleep(2)




