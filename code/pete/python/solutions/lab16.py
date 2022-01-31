import requests
from pprint import pprint

"""Part 1"""

headers = {'Accept': 'application/json'} # telling the server to give us back the json response
response = requests.get('https://icanhazdadjoke.com/', headers=headers) # pass in the headers as kwarg (keyword argument)

data = response.json()

print(data.get('joke'))


"""Part 2"""
def get_dad_jokes(term):
    headers = {'Accept': 'application/json'}
    params = {'term': term}
    response = requests.get('https://icanhazdadjoke.com/search', headers=headers, params=params)

    data = response.json()
    # pprint(data)

    for i, joke in enumerate(data.get('results', [])): # person.get('name', 'John Doe') returns the name if it exists as a key, if not returns 'John Doe'
        print(f'\n{i + 1}:')
        print(joke.get('joke'))



while True:
    term = input('What dad jokes do you want to see (or type "done" to exit): ')
    if term == 'done':
        break
    get_dad_jokes(term)