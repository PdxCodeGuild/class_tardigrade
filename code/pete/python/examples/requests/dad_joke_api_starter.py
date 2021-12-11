import requests

url = 'https://icanhazdadjoke.com/'

headers = {
    'accept': 'application/json'
}
response = requests.get(url, headers=headers)

print(response.text) # {"id":"zkO7wHJmrc","joke":"What did the calculator say to the student? You can count on me.","status":200} # this is a JSON-formatted string
print(response) # <Response [200]> # this is a response object
data = response.json() # the .json() method of a response returns a python dictionary if the response text is a JSON-formatted string
print(data) # {'id': 'zkO7wHJmrc', 'joke': 'What did the calculator say to the student? You can count on me.', 'status': 200} # this is a python dictionary
print(data['joke']) # What did the calculator say to the student? You can count on me. # this is the joke

url = 'https://icanhazdadjoke.com/search'
headers = {
    'accept': 'application/json'
}
params = { # here I'm setting the limit param, check out https://icanhazdadjoke.com/api#search-for-dad-jokes to see other params
    'limit': 1
}

print('\n')

response = requests.get(url, headers=headers, params=params)

print(response.json())