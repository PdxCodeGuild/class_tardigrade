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
