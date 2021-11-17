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


# card_1 = input('What is your first card?: ').upper()
# card_2 = input('What is your second card?: ').upper()
# card_3 = input('What is your third card?: ').upper()

# card_total = cards[card_1] + cards[card_2] + cards[card_3]

# # print(card_total)

# if card_total == 21:
#     print(f'{card_total} Blackjack!')
# elif card_total >= 17 and card_total < 21:
#     print(f'{card_total} Stay')
# elif card_total < 17:
#     print(f'{card_total} Hit')
# elif card_total > 21:
#     print(f'{card_total} Busted!')


#Random Version

import random

options = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

card_4 = random.choice(options)
card_5 = random.choice(options)

dealer_card1 = random.choice(options)
dealer_card2 = random.choice(options)


message = input('Would you like to play a game? y/n: ')

if message == 'y':
    print('Good luck')
elif message == 'n':
    print('Thanks for playing!')

total = cards[card_4] + cards[card_5]
print(f'Your cards are {card_4} and {card_5} for {total} points.')
while total < 21:
    if total < 21:
        message = input('Hit or Stay?: ').title()
        if message == 'Hit':
            new_card = random.choice(options)
            total = total + cards[new_card]
            print(f'Your new card is {new_card} for {total} points')
        elif message == 'Stay':
            break

if total > 21:
    print('Busted, you lost')

dealer_total = cards[dealer_card1] + cards[dealer_card2]
print("Dealer's turn!")
while dealer_total < 21 and total <= 21:
    if dealer_total > 21:
        break
    elif dealer_total == 21:
        break
    elif dealer_total < 21 and dealer_total >= 17:
        break
    elif dealer_total < 21 and dealer_total < 17:
        new_dealer_card = random.choice(options)
        dealer_total = dealer_total + cards[new_dealer_card]

if dealer_total == total:
    print(f'You have {total} points, dealer has {dealer_total} points. You tie!')
elif dealer_total > 21:
    print(f'Dealer has {dealer_total}, Dealer busts, you win!')
elif total > dealer_total:
    print(f'You have {total} points, dealer has {dealer_total} points. You win!')
elif total < dealer_total and dealer_total <= 21:
    print(f'You have {total} points, dealer has {dealer_total} points. You lost.')

print('Thanks for playing!')
