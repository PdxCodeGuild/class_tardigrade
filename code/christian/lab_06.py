import random


def pick6():

    new_ticket = []     #empty list to start

    while len(new_ticket) < 6:  #runs loop until 6 numbers generate
        new_ticket.append(random.randint(1,99))  #use random/randint/append to add numbers to list
    return new_ticket



def num_matches(winning, ticket): 
    matches = 0
    for x in range(len(winning)): # range of winning ticket
     
        if winning[x] == ticket[x]:  # checking if matches with ticket
            matches += 1
       
    return matches


     




# list_one = [0,3,2,3,4,5]
# list_two = [0,1,2,3,4,5]
# pick_six = pick6()       #test

# print(random_nums,'randomnums')
# print(num_matches(pick6(),list_two))

balance = 0
pick_six = pick6()

for x in range(100000):   
    ticket_matches = num_matches(pick6(),pick_six) #use our functions to run game
    balance -= 2
    if ticket_matches == 1:
        balance += 4
    if ticket_matches == 2:
        balance += 7
    if ticket_matches == 3:
        balance += 100
    if ticket_matches == 4:
        balance += 50,000
    if ticket_matches == 5:
        balance += 1,000,000
    if ticket_matches == 6:
        balance += 25,000,000
print(f'Your balance is {balance}')

return_of_in = balance / 200000
print(f'Your ROI is {return_of_in}')



            
    
    




            


  





# Generate a list of 6 random numbers representing the winning tickets 
# Start your balance at 0 
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance





