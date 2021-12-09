import requests

url = 'https://pokeapi.co/api/v2/pokemon/charizard'

response = requests.get(url)

# print(response.text)
# print(type(response.text)) # <class 'str'>
# print(response.json())
# print(type(response.json())) # <class 'dict'>

data = response.json()
print(data.keys())

print(data.get('species'))