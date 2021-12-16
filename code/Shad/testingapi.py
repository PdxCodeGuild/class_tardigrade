import requests
import json


headers ={'accept': '/cities'}
response = requests.get('http://opentable.herokuapp.com/api', headers = headers)
print(response)

data = response.json()
print(data)