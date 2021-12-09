# Version 1 of Lab
import requests
url = 'https://icanhazdadjoke.com/'

headers = {
    'accept': 'application/json'
}
response = requests.get(url, headers = headers)
data = response.json()
print(data['joke'])

# Version 2 of Lab
import time

while True:

    user_input = input("Please type a search term to find a specific joke. If you would like to exit type 'quit' ").lower()

    if user_input == 'quit':
        break
    else:
        url = f'https://icanhazdadjoke.com/search?term={user_input}'

        headers = {
            'accept': 'application/json'
        }

        params = {
            'limit': 20,
        }

        response = requests.get(url, headers = headers, params = params)
        data = response.json()
        for i in range(0, len(data['results'])):
            print(data['results'][i]['joke'], end='\n')
            time.sleep(2)