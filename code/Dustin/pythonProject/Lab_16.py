import time
import requests
""" PART !
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

"""
headers = {
    'accept': 'application/json'
}
while True:

    user_input = input("Enter seaarch for dad joke here or 'stop' to exit: ")

    if user_input == 'stop':
        break
    else:
        url = f'https://icanhazdadjoke.com/search?term={user_input}'
        params = {
            # here I'm setting the limit param, check out https://icanhazdadjoke.com/api#search-for-dad-jokes to see other params
            'limit': 20
        }
        response = requests.get(url, headers=headers, params=params)
        jokes = response.json()
        for joke in range(0, len(jokes["results"])):
            print(jokes["results"][joke]["joke"], end="\n")
            time.sleep(5)