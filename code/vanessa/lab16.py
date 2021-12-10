import requests
import time

url= 'https://icanhazdadjoke.com/'

headers = {
    "accept": "application/json"

}


response = requests.get(url,headers=headers,)
print(response.text)
print(response)
data = response.json()
print(data)
print(data["joke"])
counter = 0
while counter <2:
    counter +=1
    search_term=(input("what would you like to search jokes by? "))
    url2 = 'https://icanhazdadjoke.com/search'
    headers = {
        "accept": "application/json"

    }

    params = {
        'term': search_term
        
    }
    searches = requests.get(url2, headers=headers, params=params)
    data2 = searches.json()
    
    data2 = searches.json()
    output=(data2["results"])
    for item in output:
        print(item["joke"])
        time.sleep(4)