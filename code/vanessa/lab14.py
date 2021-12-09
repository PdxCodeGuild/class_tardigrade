import requests

url= 'https://icanhazdadjoke.com/'

headers = {
    "accept": "application/json"
    
}

response = requests.get(url,headers=headers)

print(response.text)

