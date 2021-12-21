import requests
import time

while True:
    print("\033[1m"+ "\nWelcome to \"icanhazdadjoke\" Dad Joke Library!" + "\033[0m")
    word = input("\nWhat subject would you like your dad jokes to be about (or enter \"exit\" to Exit): ").lower()
    if word == "exit".lower():
                print("\nThanks for listening to our dad jokes, goodbye!\n")
                break

    headers = {"accept": "application/json"}

    params = {"term": word, "limit": 5}

    response = requests.get("https://icanhazdadjoke.com/search", headers=headers, params=params)
    response = response.json()
    response = response["results"]

    for joke in response:
        time.sleep(3)
        print("\n" + joke["joke"])
    another_joke = input("\nWould you like to hear another dad joke (\"Yes\" or \"No\"): ").lower()
    if another_joke not in ["yes", "no"]:
        print("\nResponse must either be \"Yes\" or \"No\"")
    elif another_joke != "yes".lower():
        print("\nFine, Goodbye!\n")
        break

