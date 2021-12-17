"""
Lab 16. Joke API
Author: Travis Jackson
Date: 12/9/21

"""

import requests
import time
import re




#splits joke at puncuation to capture a punchline
def add_suspense(suspense):

    split_suspense = re.split("(?<=[\.\?\!])", suspense)

    for item in split_suspense:

        if item == "" or item == "." or item == " ":
            
            continue

        else:

            print(f" {item.lstrip()}")
            time.sleep(3)
    print(5 * "*")


#version 1 random joke
response = requests.get("https://icanhazdadjoke.com/", headers = {"accept": "application/json"})
data = response.json()

random_joke = data["joke"]

print("----- Dad Jokes-----")
print("--Random Joke of the day:")

add_suspense(random_joke)

#part 2 search and view more pages

page_count = 1
page_num = ""

print("--Joke search: ")
search_input = input('Enter a search term or "q" to quit: ')

#repl
while True:   

    if search_input == "q":
        break

    search_joke = requests.get(f"https://icanhazdadjoke.com/search?term={search_input}{page_num}", headers = {"accept": "application/json"})
    data_search = search_joke.json()

    #check for number of page results
    total_pages = data_search["total_pages"]
    current_page = data_search["current_page"]

    #loop through all returned jokes
    len_results = len(data_search["results"])
    i = 0
    while len_results != i:

        suspense_search = data_search["results"][i]["joke"]

        add_suspense(suspense_search)
        i += 1

    #check for more page results
    if total_pages == current_page:

        search_input = input('Enter a search term or "q" to quit: ')       

    #ask if user would like to view more pages (if more than 1)
    elif total_pages > 1:

        next_page_input = input("Would you like to view the next page of results? (y/n)")

        if next_page_input == "y":

            page_count += 1

            page_num = f"&page={page_count}"

        else:

            search_input = input('Enter a search term or "q" to quit: ')


