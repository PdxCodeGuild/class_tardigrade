"""
Lab 6: Pick 6
Author: Travis Jackson
Date: 11/18/21

"""

import random 

balance = 0
total_matches = 0
earnings = 0
highest_num_matched = 0
random_num_list = []
tickets_bought = 100000

payout_amount_dict = {
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000
}


def pick6():
    """
    returns a list of 6 random numbers
    """

    random_num_list = []

    for ran in range(1,7):

        ran = random.randrange(1,99)
        random_num_list.append(ran)

    return random_num_list


def num_matches(winning_ticket, ticket):
    """
    returns the number of matches between the 2 tickets
    """
    matches = 0

    for match in range(6):

        if winning_ticket[match] == ticket[match]:

            matches += 1

    return matches

#picks the winning ticket
winning_ticket = pick6()

 # draws tickets
for draw in range(1, tickets_bought + 1):

    #subtracts the cost of a ticket $2
    balance -= 2

    #picks ticket  
    ticket = pick6()
    
    #checks matching ticket numbers
    matches = num_matches(winning_ticket, ticket)

    total_matches += matches

    #finds highest match on one ticket
    if highest_num_matched < matches:
        highest_num_matched = matches


    #uses dict to find payout winnings
    for match_count in payout_amount_dict.keys():

        if matches == 0:

            break

        if matches == match_count:

            balance += payout_amount_dict.get(match_count)
            earnings += payout_amount_dict.get(match_count)
            break

roi = (((earnings - tickets_bought) / tickets_bought) * 100)


print(f"Your final balance is {balance} dollars") 
print(f"There were a total of {total_matches} matching numbers.")
print(f"The highest number of matches on one ticket is: {highest_num_matched}")
print(f"Your ROI (return on investment) is {round(roi, 2)} percent")
