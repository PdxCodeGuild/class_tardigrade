import random

def pick6(): # return a list of 6 random numbers
    return random.sample(range(1, 99), 6)

def num_matches(a, b): 
    matches = 0 # return the number of matches between the 2 tickets
    for x in range(0, 5):
        if a[x] == b[x]:
            matches += 1
    return matches
    
player_balance = 0

print(f"\nPlayer beginning balance = ${player_balance}.")

total_matches = 0

for i in range(100000):
    winning_ticket_nums = pick6()
    print(f"\nThe winning ticket numbers are {winning_ticket_nums}.")

    player_ticket_nums = pick6()
    print(f"\nPlayer ticket numbers are {player_ticket_nums}.")

    player_balance -= 2

    winnings = [0, 4, 7, 100, 50000, 1000000, 25000000]

    matches = num_matches(winning_ticket_nums, player_ticket_nums)

    if matches == 0:
        print(f"\nYou had no matches.")

    else:
        print(f"\nYou matched {matches} time(s).")
    
    total_matches += matches

    player_balance += winnings[matches]

print(f"\n\nTotal matches = {total_matches}")

print(f"\nPlayer ending balance = ${player_balance}.\n")

    # if player_ticket_nums == winning_ticket_nums:
    #     print("\nYou matched the winning ticket numbers and won $25M dollars!")
    #     player_balance += 25000000
    
    # elif player_ticket_nums[0] == winning_ticket_nums[0]:
    #     print("\nYou matched one number and win $4 dollars.")
    #     player_balance += 4

    # elif player_ticket_nums[0] == winning_ticket_nums[0] and player_ticket_nums[1] == winning_ticket_nums[1]:
    #     print("\nYou matched two numbers and win $7 dollars.")
    #     player_balance += 7

    # elif player_ticket_nums[0] == winning_ticket_nums[0] and player_ticket_nums[1] == winning_ticket_nums[1] and player_ticket_nums[2] == winning_ticket_nums[2]:
    #     print("\nYou matched three numbers and win $100 dollars.")
    #     player_balance += 100

    # elif player_ticket_nums[0] == winning_ticket_nums[0] and player_ticket_nums[1] == winning_ticket_nums[1] and player_ticket_nums[2] == winning_ticket_nums[2] and player_ticket_nums[3] == winning_ticket_nums[3]:
    #     print("\nYou matched four numbers and win $50k dollars.")
    #     player_balance += 50000

    # elif player_ticket_nums[0] == winning_ticket_nums[0] and player_ticket_nums[1] == winning_ticket_nums[1] and player_ticket_nums[2] == winning_ticket_nums[2] and player_ticket_nums[4] == winning_ticket_nums[4] and player_ticket_nums[5] == winning_ticket_nums[5]:
    #     print("\nYou matched five numbers and win $1M dollars.")
    #     player_balance += 1000000

    # else:
    #     print("\nNo numbers matched and you lost money, so that sucks.")
    