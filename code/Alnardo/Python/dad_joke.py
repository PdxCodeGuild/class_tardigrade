#DAD Joke API

import requests
"""
url = 'https://icanhazdadjoke.com'

header = {
    'accept' : 'application/json'
}

response = requests.get(url, headers=header)

# print(response.text)
# print(response)

dad_joke = response.json()
print(dad_joke['joke'])

"""
#Search Joke

import time

search_url = 'https://icanhazdadjoke.com/search'

header = {
    'accept' : 'application/json'
}

parameters = {
    'page'  : 1,
    'term'  : '',
    'limit' : 20
}
welcome_message = input('Welcome to Dad Jokes API! Would you like to continue? (yes/no): ')

while welcome_message == 'yes':


    parameters['term'] = input("Please enter a search term or leave blank to search all: ")
    parameters['limit'] = int(input("Please enter a number of 1-30 of how many jokes you'd like to see: "))
    search_response = requests.get(search_url, headers=header, params=parameters)

    search_dad_joke = search_response.json()


    if search_dad_joke['total_pages'] > 1:
        print(f"There are {search_dad_joke['total_pages']} total pages.")
        parameters['page'] = int(input('Which page would you like to view?: '))
    else:
        parameters['page'] = 1
        
    search_response = requests.get(search_url, headers=header, params=parameters)

    search_dad_joke = search_response.json()

    num = 0
    for i in search_dad_joke['results']:
        print(search_dad_joke['results'][num]['joke'])
        print('')
        time.sleep(1)
        num += 1


    welcome_message = input('Would you like to go again? (yes/no): ')

print('Thanks for your time!')
