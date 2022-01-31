"""Why not to invest in the lottery a.k.a. Lab 06"""
"""winning ticket generated"""
import random
winning_ticket = random.sample(range(1, 99), 6)
attempts = int(input("How many times would you like to play? "))
print(f"the winning ticket was: {winning_ticket}")

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

expenses = attempts * 2
earnings = cash + attempts * 2
return_on_investment = cash / expenses

print(f"Your expenses were: {expenses}\n"
      f"Your earnings were: {earnings}\n"
      f"Your Return on investment was: {return_on_investment}\n")







