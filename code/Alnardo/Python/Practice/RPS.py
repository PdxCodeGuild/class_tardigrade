#Lab_4

import random

welcome = 'Welcome to Rock, Paper, Scissors!'
message = input('Would you like to play? yes/no: ')
options = 'Your options are as follows: '
print(welcome)
print(options)
rps = ['Rock', 'Paper', 'Scissors']
print(rps)

while message == 'yes':
    random_choice = random.choice(rps)
    computer = (f'Computer plays {random_choice}')

    for answer in rps:
        print(answer)
        
    choice = input('What would you like to play?: ').title()
    print(choice and computer)
    if choice == 'Rock' and computer == 'Computer plays Rock':
        print('You tied!')

    elif choice == 'Rock' and computer == 'Computer plays Scissors':
        print('Rock smashes scissors, you win!')
            
    elif choice == 'Rock' and computer == 'Computer plays Paper':
        print('Oh no, you lost!')

    if choice == 'Scissors' and computer == 'Computer plays Scissors':
        print('You tied!')

    elif choice == 'Scissors' and computer == 'Computer plays Rock':
        print('Rock smashes scissors, you lost!')

    elif choice == 'Scissors' and computer == 'Computer plays Paper':
        print('Scissors cut paper, you win!')

    if choice == 'Paper' and computer == 'Computer plays Paper':
        print('You tied!')

    elif choice == 'Paper' and computer == 'Computer plays Rock':
        print('Paper covers Rock, you win!')

    elif choice == 'Paper' and computer == 'Computer plays Scissors':
        print('Scissors cuts Paper, you lost!')
    message = input('Would you like to play again? yes/no: ')


print('Thanks for playing!')