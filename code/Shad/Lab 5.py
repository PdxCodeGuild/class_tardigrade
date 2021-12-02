cards = {'A':1,'2':2,'3':3,'4':4,'5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10,'K':10}

user1 = input("What's your first card?\nChoose letter cards by captial abreviation")
user2 = input("What's your second card?\nChoose letter cards by captial abreviation")
user3 = input("What's your third card?\nChoose letter cards by captial abreviation" )

sum = cards.get(user1) + cards.get(user2) + cards.get(user3)

print(sum)

if sum < 17:
    print(f'{sum} Hit')
elif sum >= 17 and sum < 21:
    print(f'{sum} Stay')
elif sum == 21:
    print(f'{sum} Blackjack!')
else:
    print("Already Busted")
