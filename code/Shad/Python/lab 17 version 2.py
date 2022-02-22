
import requests

while True:
    
    word = input('enter a keyword to search for quotes:  ')
    page =1

    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    urlkeyword = f' https://favqs.com/api/quotes?page={page}&filter={word}'
    params = {'filter': word }  

    response = requests.get(urlkeyword, headers=headers,params=params  )
    key = response.json()

    while True:

        print(f"{len(key['quotes'])} quotes associated with {word} - page {page}")

        for i in range(len(key['quotes'])):
            print(key['quotes'][i]['body'])
            print('\n')

        choice = input("enter next page or done:")
        if choice=='done':
            break  
        else:
            page = page + 1
            urlkeyword = f' https://favqs.com/api/quotes?page={page}&filter={word}'
            params = {'filter': word }  

            response = requests.get(urlkeyword, headers=headers,params=params  )
            key = response.json()
