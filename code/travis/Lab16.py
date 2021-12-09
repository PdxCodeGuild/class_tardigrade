"""
Lab 16. Joke API
Author: Travis Jackson
Date: 12/9/21

"""

import requests
import time
import re

response = requests.get("https://icanhazdadjoke.com/", headers = {"accept": "application/json"})
data = response.json()


joke = data["joke"]

#splits joke at puncuation to capture a punchline
suspense = re.split("(?<=[\.\?\!])", joke )


# prints 
for item in suspense:

    if item == "" or item == "." or item == " ":
        
        continue

    else:

        print(item.lstrip())
        time.sleep(3)

#part 2

#ask to search
#repl

while True:

    search_joke = requests.get("https://icanhazdadjoke.com/search", 
    ...





