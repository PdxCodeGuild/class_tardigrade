import requests
import time

url= 'https://icanhazdadjoke.com/search'

headers = {
    "accept": "application/json"

}


response = requests.get(url,headers=headers, params=params)
# print(response.text)
# print(response)
data = response.json()
# print(data)
print(data["joke"])

url2 = 'https://icanhazdadjoke.com/search'
search_term= ""
params = {
    'term': search_term
    
}
searches = requests.get(url2, headers=headers)

while True:
    search_term=(input("what would you like to search jokes by? "))
    data2 = searches.json()
    time.sleep(2)
    print(data2)
    print(data2["joke"])
