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


search_keyword = input("What keyword would you like to search? or (q)uit ")
while True:
    
    if search_keyword == "q":

        print("Bye Bye")
        break   

    response_keyword = requests.get(f"https://favqs.com/api/quotes?page={page_input}&filter={search_keyword}", headers= {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params= "json")
    keyword_data = response_keyword.json()

    for i, item   in enumerate(keyword_data["quotes"]):
        quote_search = keyword_data["quotes"][i]["body"]
 
        try:
            author_search = keyword_data["quotes"][i]["author"]
        except:
            break

        print()
        print(f" - {quote_search}")
        print(f" ------ {author_search}")
        print()
 
        if len(keyword_data["quotes"]) - 1 == i:

            break



    if keyword_data["quotes"][i]["body"] == "No quotes found":

        print("No results found")
        print("Bye Bye")
        break

    elif keyword_data["last_page"] == False:

        page_input_next = input("Would you like to see the next page(y)? or (q)uit? ")

        if page_input_next == "q":

            print("Bye Bye")
            break      

        elif page_input_next == "y":

            page_input += 1

        else:
            break
 


    elif keyword_data["last_page"] == True:

        print("That was the last page")
        print("Bye bye")
        break
          

