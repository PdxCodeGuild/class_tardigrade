import requests

url = 'https://icanhazdadjoke.com/'

# make_it_work = {
#     'accept': 'application/json'
# }
# response = requests.get(url, headers=make_it_work)
# print(response.json())

# print(response.text) # {"id":"zkO7wHJmrc","joke":"What did the calculator say to the student? You can count on me.","status":200} # this is a JSON-formatted string
# print(response) # <Response [200]> # this is a response object
# data = response.json() # the .json() method of a response returns a python dictionary if the response text is a JSON-formatted string
# print(data) # {'id': 'zkO7wHJmrc', 'joke': 'What did the calculator say to the student? You can count on me.', 'status': 200} # this is a python dictionary
# print(data['joke']) # What did the calculator say to the student? You can count on me. # this is the joke

url = 'https://icanhazdadjoke.com/search'
headers = {
    'accept': 'application/json'
}
params = {
    'limit': 1
}


response = requests.get(url, headers=headers, params=params)
response = response.json()
results = response['results'][0]
print(results['joke'])