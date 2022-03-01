from email.quoprimime import quote
import requests
import time

url= 'https://favqs.com/api/qotd'

headers = {
    "accept": "application/json",
    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'

}


response = requests.get(url,headers=headers,)
# print(response.text)
data = response.json()
print(data["quote"]['body'])
print(data["quote"]["author"])

#-------------------------------------------------------------------------

def get_quotes(quote_type):
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    params = {'quote_type': quote_type}
    page = 1
    response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={quote_type}', headers=headers, params=params)

    data = response.json()
   

    for i, quote in enumerate(data.get('quotes', [])): # person.get('name', 'John Doe') returns the name if it exists as a key, if not returns 'John Doe'
        print(f'\n{i + 1}:')
        print(quote.get('body','author'))


while True:
    quote_type = input('Enter a keyword to search for quotes or type "done" to exit): ')
    if quote_type == 'done':
        break
    get_quotes(quote_type)