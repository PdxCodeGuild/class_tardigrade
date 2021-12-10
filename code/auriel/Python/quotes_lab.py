# Version 1 of Lab
import requests

url = 'https://favqs.com/api/qotd'
params = {
    'format': 'json'
}
response = requests.get(url, params=params)
data = response.json()
print(data['quote']['author'])
print(data['quote']['body'])