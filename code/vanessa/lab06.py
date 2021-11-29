import random
def pick6():
    '''generate six random winning numbers'''
    results= []
    i = 0
    while i < 6:
        results.append(random.randint(1,99))
        i = i + 1
    return results
winning_ticket = pick6()
print(f"Winning numbers: {winning_ticket}")


my_tickets = []
balance = 0
                                        #expenses = 2 * (len(my_tickets))
while range(len(my_tickets) < 100000):
    my_tickets.append(pick6())
    balance = balance -2  
                                        # print(f"my tickets{my_tickets}")

def num_matches(win_ticket, ticket):
    for i in range(len(win_ticket)):
        match = 0
        if win_ticket[i]== ticket[i]:
            return match
           
for ticket in my_tickets:
    (num_matches(winning_ticket,ticket))

my_match= (num_matches(winning_ticket,my_tickets))
for match in range(len(my_tickets)):
    if my_match == 1:
        balance += 4
    if my_match == 2:
        balance += 7
    if my_match == 3:
        balance += 100
    if my_match == 4:
        balance += 50000
    if my_match == 5:
        balance += 10000000
    if my_match == 6:
        balance += 25000000

print(f'Final Balance: ${balance}',"balance")


