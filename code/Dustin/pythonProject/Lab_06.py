"""Why not to invest in the lottery a.k.a. Lab 06"""
"""winning ticket generated"""
import random
winning_ticket = random.sample(range(1, 99), 6)
print(winning_ticket)
attempts = int(input("How many times would you like to play? "))
"""starting cash"""
cash = 0

def play(winner):
    """take winning number and compare to random generated number """
    tries = random.sample(range(1, 99), 6)
    total_matches = 0
    position = 0

    for i in range(6):
        if tries[position] == winner[position]:
            total_matches += 1
        else:
            total_matches += 0
        position += 1


    winnings = [0, 4, 7, 100, 50000, 1000000, 25000000]
    cash = -2 + (winnings[total_matches])


    return cash

for i in range(attempts):
    cash += play(winning_ticket)
print(cash)
expenses = attempts * 2
ROl = cash
print(expenses)





