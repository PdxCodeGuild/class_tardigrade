# Version 1 and 2 of Lab
import random

def pick6():
    lottery_numbers = []
    while len(lottery_numbers) < 6:
        lottery_numbers.append(random.randint(1, 99)) # Input random number and insert into list each time until they are six numbers in list
    return lottery_numbers

def num_matches(winning, ticket):
    matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches += 1
    return matches

def money_made(matches):
    prize = 0
    if matches == 1:
        prize += 4
    elif matches == 2:
        prize += 7
    elif matches == 3:
        prize += 100
    elif matches == 4:
        prize += 50000
    elif matches == 5:
        prize += 1000000
    elif matches == 6:
        prize += 25000000
    return prize

winning_ticket = pick6()
earnings_balance = 0
expenses_balance = 0

for i in range(100000) :
    player_ticket = pick6()
    check_tickets = num_matches(winning_ticket, player_ticket)
    expenses_balance -= 2
    prize_money = money_made(check_tickets)
    earnings_balance += prize_money

roi = (earnings_balance - expenses_balance) / expenses_balance
final_balance = earnings_balance + expenses_balance

print(f'Earnings: ${earnings_balance}')
print(f'Expenses: ${expenses_balance}')
print(f'Balance: ${final_balance}')
print(f'ROI:{roi}%')