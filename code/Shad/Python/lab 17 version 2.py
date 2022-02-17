
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
        urlkeyword 
        key['quotes'][i]['body']
        
        print('\n \n \n')
      


        
        if pageword =='done':
            break  
        else:
            page = page + 1
            urlkeyword = f' https://favqs.com/api/quotes?page={page}&filter={word}'
            params = {'filter': word }  
            
            response = requests.get(urlkeyword, headers=headers,params=params  )
            key = response.json()
            # print(key['quotes'][i]['body'])
            print('\n \n \n')
            print(f"{urlkeyword }\n\n\n {len(key['quotes'])} quotes {word} and page {page}")
            print(key['quotes'][i]['body'])
