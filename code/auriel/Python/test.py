
import requests

# Version 2 of Lab
while True:
    user_input = input("Enter a keyword to search for quotes or enter 'done' to quit: ").lower()

    if user_input == 'done':
        break
    else: 
        page = 1
        num_quotes = 0
        keyword_url = f'https://favqs.com/api/quotes?page={page}&filter={user_input}'
        headers = {
        'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
    }
        response = requests.get(keyword_url, headers = headers)
        data = response.json()

        for i in range(0, len(data['quotes'])):
            num_quotes += 1
        print(f'{num_quotes} quotes associated with {user_input} - page {page}')
        
        for quote in data['quotes']:
            print(quote['body'])
        
        next_page = input("Enter 'next page' or 'done': ")