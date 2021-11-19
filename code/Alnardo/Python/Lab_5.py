#LAB 5

cards = {
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10
}


card_1 = input('What is your first card?: ').upper()
card_2 = input('What is your second card?: ').upper()
card_3 = input('What is your third card?: ').upper()

card_total = cards[card_1] + cards[card_2] + cards[card_3]

# print(card_total)

if card_total == 21:
    print(f'{card_total} Blackjack!')
elif card_total >= 17 and card_total < 21:
    print(f'{card_total} Stay')
elif card_total < 17:
    print(f'{card_total} Hit')
elif card_total > 21:
    print(f'{card_total} Busted!')


