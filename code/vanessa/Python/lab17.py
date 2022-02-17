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