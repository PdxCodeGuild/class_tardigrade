import random

def pick6():
    ticket = random.sample(range(0, 100), 6)
    return ticket


def num_matches(winning_ticket, ticket):
    matches = 0
    for i in range(len(ticket)):
        if winning_ticket[i] == ticket[i]:
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


winning_ticket_nums = pick6()
balance = 0
earnings  = 0
expenses = 0
    
print(f"\nBeginning balance = ${balance}.")
    
for _ in range(100_000):
        # Generate a list of 6 random numbers representing the ticket
    ticket = pick6()
        # Subtract 2 from your balance (you bought a ticket)
    balance -= 2
    expenses += 2
        # Find how many numbers match
    matches = num_matches(ticket, winning_ticket_nums)
        # Add to your balance the winnings from your matches
    balance += winnings_dict[matches]
    earnings += winnings_dict[matches]

print(f"\nEnding balance = ${balance}.\n")
print("Return on Investment (ROI) is "), print((earnings - expenses) / expenses)
print()