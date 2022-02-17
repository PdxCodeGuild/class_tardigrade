
import requests



word = input('enter a keyword to search for quotes:  ')
page =1

headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
urlkeyword = f' https://favqs.com/api/quotes?page={page}&filter={word}'
params = {'filter': word }  

response = requests.get(urlkeyword, headers=headers,params=params  )
key = response.json()
pageword = input("enter next page or done:")

while True:

    for i in range(len(key['quotes'])):
        print(key['quotes'][i]['body'])
        print(urlkeyword)
        print('\n \n')
        print(f"{len(key['quotes'])} quotes of word {word} and page {page}")


        
        if pageword=='done':
            break  
        else:
            page = page + 1
            urlkeyword = f' https://favqs.com/api/quotes?page={page}&filter={word}'
            params = {'filter': word }  

            response = requests.get(urlkeyword, headers=headers,params=params  )
            key = response.json()
            # print(f"{len(key['quotes'])} quotes of word {word} and page {page}")
            print(key['quotes'][i]['body'])
            print(urlkeyword)
            print('\n \n')
            print(f"{len(key['quotes'])} quotes of word {word} and page {page}")
