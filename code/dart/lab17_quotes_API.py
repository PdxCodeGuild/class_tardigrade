import requests
import time

""" VERSION 1 """

# response = requests.get("https://favqs.com/api/qotd", headers = {"accept": "application/json"})
# response = response.json()
# response = response["quote"]
 
# quote = response["body"]
# author = response["author"]

# print(f"\n{author} said, \"{quote}\"\n")

""" VERSION 2 """

while True:
    print("\033[1m"+ "\nWelcome to the \"Fav Quotes\" Library!" + "\033[0m")
    user_input = input("\nWhat kind of quotes would you like to see: ").lower()

    url = "https://favqs.com/api/quotes?page=<page>&filter=<keyword>"

    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

    params = {
        "filter": user_input,
        "page": 1,
    }

    response = requests.get(url + f"/search/{user_input}", headers=headers, params=params)
    response = response.json()
    response = response["quotes"]
    for quote in response:
        time.sleep(1)
        print(f"\n" + quote["author"] + " said, " + "\"" + quote["body"] +"\"" + "\n")
    next_page = input("Enter \"Next Page\" or \"Done\" to Quit: ").lower()
    if next_page == "next page".lower():
        params["page"] += 1
    elif next_page == "done".lower():
        print("\033[1m"+ "\nSee ya later!\n" + "\033[0m")
        break