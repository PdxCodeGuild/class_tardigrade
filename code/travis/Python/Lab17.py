"""
Lab 17
Author: Travis Jackson
Date: 12 17 21

"""

import requests
import json



print("Random Quote!")


response = requests.get("https://favqs.com/api/qotd", params= "json")

data = response.json()

quote = data["quote"]["body"]
author = data["quote"]["author"]


print()
print(f" - {quote}")
print(f" ------ {author}")
print()


page_input = 1
while True:

    search_keyword = input("What keyword would you like to search? ")
    

    response_keyword = requests.get(f"https://favqs.com/api/quotes?page={page_input}&filter={search_keyword}", headers= {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params= "json")
    keyword_data = response_keyword.json()




   #for i in len(keyword_data["quotes"][]):
    #    quote_search = keyword_data["quotes"][i]["body"]
    #     author_search = keyword_data["quotes"][i]["author"]
    
    #     print()
    #     print(f" - {quote_search}")
    #     print(f" ------ {author_search}")
    #     print()



    page_input = input("Would you like to see the next page? ")