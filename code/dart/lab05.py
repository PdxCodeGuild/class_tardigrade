card_values = {
    "A": 1,
    "a": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "j": 10,
    "Q": 10,
    "q": 10,
    "K": 10,
    "k": 10
}

print("The cards in Blackjack (Twenty One) are A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q and K.")

first_card = input("What's your first card: ")
second_card = input("What's your second card: ")
third_card = input("What's your third card: ")

card_points = card_values.get(first_card) + card_values.get(second_card) + card_values.get(third_card)

if card_points < 17:
    print(f"That's {card_points} so I advise you to \"Hit\".")

elif card_points >= 17 and card_points < 21:
    print(f"That's {card_points}, so I advise you to \"Stay\".")

elif card_points == 21:
    print(f"{card_points} is Blackjack!")

else:
    print("You already busted. Better luck next time!")

""" VERSION 2 (MAKE ACES ARE WORTH 1 or 11) """
