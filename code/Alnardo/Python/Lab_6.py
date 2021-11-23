#LAB 6 Pick 6

import random


# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance

def pick6():
    pick6_length = []
    while len(pick6_length) < 6:
        new_number = random.randint(1, 99)
        pick6_length.append(new_number)
    return pick6_length


winning_ticket = pick6()
ticket_cost = 2
run = 0
balance = 0
prize_money = 0


# print(pick6_ticket)
# while len(winning_ticket) < 6:
#     ticket_number = random.randint(1, 99)
#     winning_ticket.append(ticket_number)

def num_matches(winning_ticket, pick6_ticket):
    matches = 0
    for i in range(6):
        if winning_ticket[i] == pick6_ticket[i]:
            matches = matches + 1
        elif winning_ticket[i] != pick6_ticket[i]:
            matches = matches + 0
    return matches
print(winning_ticket)

while run < 100000:
    run = run + 1
    balance = balance - ticket_cost
    pick6()
    pick6_ticket = pick6()
    num_matches(winning_ticket, pick6_ticket)
    if num_matches(winning_ticket, pick6_ticket) == 1:
        prize_money = prize_money + 4
    elif num_matches(winning_ticket, pick6_ticket) == 2:
        prize_money = prize_money + 7
    elif num_matches(winning_ticket, pick6_ticket) == 3:
        prize_money = prize_money + 100
    elif num_matches(winning_ticket, pick6_ticket) == 4:
        prize_money = prize_money + 50000
    elif num_matches(winning_ticket, pick6_ticket) == 5:
        prize_money = prize_money + 1000000
    elif num_matches(winning_ticket, pick6_ticket) == 6:
        prize_money = prize_money + 25000000
    else:
        prize_money = prize_money + 0

roi = (prize_money - balance) / balance
print(roi)

balance = prize_money + balance
print(balance)


#     for i in range(6):

    # while len(pick6) < 6:
    #     new_number = random.randint(1, 99)
    #     pick6.append(new_number)
    # if pick6 == ticket:
    #     print(f'You win attempt #{run}!')
    # elif pick6 != ticket:
    #     print(f'You lost attempt #{run}')

# print(pick6())

# for i in range(6): #THIS WORKS!!!! Had help from Lisa
#     print(ticket[i], pick6[i])
"""
while len(ticket) < 6:
    num_choice = int(input('Enter a number: '))
    ticket.append(num_choice)


while len(pick6_pool) < 3:
    pick6_pool.append(pick6)
    while len(pick6) < 6:
        new_number = random.randint(1, 99)
        pick6.append(new_number)

for i in range(6):
    print(ticket[i], pick6_pool[i][i])

"""


"""
while run < 100000:
    run = run + 1
    while len(pick6) < 6:
        new_number = random.randint(1, 99)
        pick6.append(new_number)
    if pick6 == ticket:
        print(f'You win attempt #{run}!')
    elif pick6 != ticket:
        print(f'You lost attempt #{run}')

"""

# print(ticket)


# if pick6 == ticket:
#     print('You win')
# else:
#     print('You lost')