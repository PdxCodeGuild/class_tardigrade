from math import exp, pi
import random

def pick6():
    """creates a list of 6 random numbers and returns it"""
    tickets = []
    ter =0
    
    while ter < 6:
        ter = ter + 1
        tick = random.randint(0,99)
        tickets.append(tick)
        if ter == 6:
            return tickets
        

pick6()

def num_match(winning_ticket, ticket):
    """compare 1 random ticket to the winning ticket. return the number of matches"""

    match = 0 
    for i, num in enumerate(winning_ticket):
        if num == ticket[i]:
            match += 1
    return match
            
   
winning_ticket = pick6()
ticket_cost = 2
total_tickets = 100000
all_tickets= []

for i in range(total_tickets):
    ticket = pick6()
    all_tickets.append(ticket)
    match = num_match(winning_ticket,ticket)


expenses = ticket_cost * total_tickets   
earn = 0 
# print(all_tickets)
for ticket in all_tickets:
    match = 0
    for i, num in enumerate(winning_ticket):
        if winning_ticket[i] == ticket[i]:
            match += 1
    if match == 1:
        earn += 4
    if match == 2:
        earn += 7
    if match == 3:
        earn += 100
    if match == 4:
        earn += 50000
    if match == 5:
        earn += 1000000
    if match == 6:
        earn += 25000000


print(f' it costed {expenses}')
results = (earn - expenses) / expenses
print(results)
print(f'You earned {earn}')
   