import requests

url = 'https://favqs.com/api/qotd'

headers = {'accept': 'application/json'}

response = requests.get(url, headers=headers)

info = response.json()['quote']
print(info['body'])


while True:
    search = input('Enter a keyword to search for quotes: ')
    

    url = 'https://favqs.com/api/qotd'

    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

    param = {'limit': 20,
    'term': search}

    response = requests.get(url, headers=headers)

    info = response.json()['quote']
    print(info['body'])


