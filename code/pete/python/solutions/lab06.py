from math import inf
import random

def pick6():
    """
    return a list of 6 random numbers from 0-99
    """
    # # 1. plain old for loop
    # ticket = []
    # for _ in range(6):
    #     ticket.append(random.randint(0, 99)) # randint is upper bound inclusive
    #     # ticket.appned(random.randrange(0, 100)) # randrange is upper-bound exclusive
    #     # both functions will give 99 and not 100
    
    # # 2. list comprehension
    # ticket = [random.randint(0, 99) for _ in range(6)]
    # if len(set(ticket)) < 3:
    #     print(ticket)
    
    ticket = random.sample(range(0, 100), 6)
    # if len(set(ticket)) < 6: print(ticket)
    return ticket


def num_matches(winning_ticket, ticket):
    """
    return the number of matches between the 2 tickets
    """
    # # 1. for i in range loop
    # matches = 0
    # for i in range(len(ticket)):
    #     if winning_ticket[i] == ticket[i]:
    #         matches += 1 # matches = matches + 1 shorthand

    # # 2. for i, element in enumerate(list) loop
    # matches = 0
    # for i, num in enumerate(winning_ticket):
    #     if num == ticket[i]:
    #         matches += 1

    # 3. zip
    matches = 0
    for num1, num2 in zip(winning_ticket, ticket):
        if num1 == num2:
            matches += 1
    return matches

winnings_dict = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50_000,
    5: 1_000_000,
    6: 25_000_000,
}


if __name__ == '__main__': # only runs this block if it is this file that's being run
    # Generate a list of 6 random numbers representing the winning ticket
    winning = pick6()
    # Start your balance at 0
    balance = 0
    earnings  = 0
    expenses = 0
    # Loop 100,000 times, for each loop:
    for _ in range(100_000):
        # Generate a list of 6 random numbers representing the ticket
        ticket = pick6()
        # Subtract 2 from your balance (you bought a ticket)
        balance -= 2 # shorthand for balance = balance -2
        expenses += 2
        # Find how many numbers match
        matches = num_matches(ticket, winning)
        # Add to your balance the winnings from your matches
        balance += winnings_dict[matches]
        earnings += winnings_dict[matches]

    # After the loop, print the final balance
    print(balance)
    print((earnings - expenses) / expenses)
