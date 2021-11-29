import random

# Lab version 1
computer_number = random.randint(1, 10)
guesses = 0

while guesses < 10:
    guesses += 1
    user_number = int(input(f'Guess the number: '))

    if user_number == computer_number:
        print(f'Correct! You guessed {guesses} time(s).')
        break
    else:
        print(f'Incorrect, try again!')


# Lab version 2 or 3
computer_number = random.randint(1, 10)
guesses = 0

while True:
    guesses += 1
    user_number = int(input(f'Guess the number: '))

    if user_number == computer_number:
        print(f'Correct! You guessed {guesses} time(s).')
        break
    else:
        print(f'Incorrect, try again!')
        
        if user_number > computer_number:
            print(f'Your guess is too high!')
        else:
            print(f'Your guess is too low!')