import random

cards = {
    'a': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'j': 10,
    'q': 10,
    'k': 10
    
}

cards_list = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']
total = 0
user_card = 0
while True:
    total = total + user_card
    print(total)
    if total == 21:
        print("blackjack")
    elif total > 21:
        print("bust")
        break
    user = input("please hit or stay")
    if user == "hit":
        cards_keys = (random.choice(cards_list))
        user_card = cards[cards_keys]
        print(f"you have {user_card}")

    elif user == "stay":
        print(f" you have {total}")
        