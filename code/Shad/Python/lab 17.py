from collections import Counter
import requests
import json

# BASE_URL = 'https://favqs.com/api/qotd'

# response = requests.get(f"{BASE_URL}/products")
# print(response.json())





# import requests
# from requests.structures import CaseInsensitiveDict

# url = "https://favqs.com/api/qotd"

# headers = CaseInsensitiveDict()
# headers["Accept"] = "application/json"


# resp = requests.get(url, headers=headers)
# print(resp)



# {"qotd_date":"2022-02-14T00:00:00.000+00:00","quote":{"id":58787,"dialogue":false,"private":false,"tags":["truth"],"url":"https://favqs.com/quotes/blaise-pascal/58787-justice-and-t-","favorites_count":0,"upvotes_count":1,"downvotes_count":0,"author":"Blaise Pascal","author_permalink":"blaise-pascal","body":"Justice and truth are too such subtle points that our tools are too blunt to touch them accurately."}}

# headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b'}


# The Favqs Quote API also supports getting a list of quotes associated with a given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>. Prompt the user for a keyword, list the quotes you get in response, and prompt the user to either show the next page or enter a new keyword. You can use string concatenation to build the URL

   


# def quote():
#     # search=input('enter a keyword to search for quotes: ')
#     # page=int(input('enter page number: '))
#     words = search=input('enter a keyword to search for quotes: ')
#     headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

#     params = {'filter': search,
#              'page': 1 }              
#     response = requests.get(f' https://favqs.com/api/quotes?page=page&filter={words}', headers=headers,params=params )
#     # response=requests.get(' https://favqs.com/api/quotes?page=page&filter={words}')




    # url = "https://favqs.com/api/qotd"
    # response=requests.get(url)
#     json_=response.json()
#     results=json_['body']
    
#     for t in results:
        
#         print(t)
    
  
# quote()




# search=input('enter a keyword to search for quotes: ')
# page=input('enter page number: ')




# Counter=0
# Counter=0

# while True:
#     words = search=input('enter a keyword to search for quotes: ')
#     headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    
#     params = {'keyword': search,
#               'page':5  }
#     response = requests.get(f' https://favqs.com/api/quotes?page=page&filter={words}', headers=headers,params=params )
#     # response=requests.get(' https://favqs.com/api/quotes?page=page&filter={words}')
#     json_=response.json()
#     results=json_['quote']['body']
#     print(results)
#     for i, item   in enumerate(results["quotes"]):
#         print(results)





#     if words == 'exit':

#         break


# Parameter	Description
# filter	Type lookup or keyword search
# type	['author', 'tag', 'user']
# private	Get private quotes for the pro user session (e.g., private=true)
# hidden	Get hidden quotes for the user session (e.g., hidden=true)
# page	Page number (25 quotes per page)
# Examples
# Get a random list of quotes:

# GET https://favqs.com/api/quotes/
# Search for quotes containing the word "funny":

# GET https://favqs.com/api/quotes/?filter=funny
# Get quotes that are tagged with "funny":

# GET https://favqs.com/api/quotes/?filter=funny&type=tag
# Get quotes by Mark Twain:

# GET https://favqs.com/api/quotes/?filter=Mark+Twain&type=author
# Get the public quotes favorited by user 'gose':

# GET https://favqs.com/api/quotes/?filter=gose&type=user
# Get the private quotes of the current user (pro session requi





url = ' https://favqs.com/api/qotd'
headers = {
    'accept': 'application/json'
}
params = {
    'limit': 1
}


response = requests.get(url)
response = response.json()

results = response['quote']['body']
print(results)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
