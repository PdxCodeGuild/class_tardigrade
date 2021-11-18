#blackjack

cards = {
'2':2,
'3':3,
'4':4,
'5':5,
'6':6,
'7':7,
'8':8,
'9':9,
'10':10,}

face = {'A':1,
'J':10,
'Q':10,
'K':10}



choice =  input('What is your first card?: ')
choice_2 = input('What is your second card?: ')
choice_3 = input('What is your third card?: ')

total = 0

if choice in face:
    first_card = face[choice]
else:
    first_card = cards[choice]

if choice_2 in face:
    second_card = face[choice_2]
else:
    second_card = cards[choice_2]

if choice_3 in face:
    third_card = face[choice_3]
else:
    third_card = cards[choice_3]

result = (first_card + second_card + third_card)

if result < 17:
    print('Hit')
if result == 17 < 21:
    print('Stay')
if result == 21:
    print('Blackjack!')
if result > 21:
    print('Already busted')





# add up value of the three choices
# analize value to Blackjack criteria
# determine if choice is face card or not

# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"





