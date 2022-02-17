import time
import requests

url = 'https://icanhazdadjoke.com/'
headers = {
    'accept': 'application/json'
}
response = requests.get(url, headers=headers)

data = response.json()
print(data['joke']) # What did the calculator say to the student? You can count on me. # this is the joke

url = 'https://icanhazdadjoke.com/search'
headers = {
    'accept': 'application/json'
}
params = { # here I'm setting the limit param, check out https://icanhazdadjoke.com/api#search-for-dad-jokes to see other params
    'limit': 20
}

print('\n')

response = requests.get(url, headers=headers, params=params)

