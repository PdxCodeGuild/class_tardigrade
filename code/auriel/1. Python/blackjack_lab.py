playing_cards = {
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'J' : 10,
    'Q' : 10,
    'K' : 10
    }

first_card = input('What is your first card?: ')
second_card = input('What is your second card?: ')
third_card = input('What is your third card?: ')

if first_card in playing_cards and second_card in playing_cards and third_card in playing_cards: # If all user inputs are in the 'Playing_Cards' dictionary
    outcome = playing_cards[first_card] + playing_cards[second_card] + playing_cards[third_card] # Add all values of the keys form the dictionary that the user inputs
    
    if outcome < 17:
        print(f'{outcome} Hit')
    elif outcome >= 17 and outcome < 21:
        print(f'{outcome} Stay')
    elif outcome == 21:
        print(f'{outcome} Blackjack!')
    else:
        print(f'{outcome} Already Busted')
else: 
    print('Please choose a correct playing card. You must use capital letters if choosing "A J Q K".')
