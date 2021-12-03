from random import randint

# tickets = []
# def pick6():
#     ter = 0
    
#     while ter < 6:
#         ter = ter + 1
#         tick = randint(0,99)
#         tickets.append(tick)
#         if ter == 6:
#             return tickets


ticket = []
def pick6_2():
    

    for _ in range(6):
        ticket.append(randint(1, 99))

    return ticket
            

  

def num_matches():
    for _ in range(100000):
        winning_ticket=entry = pick6_2()
     
        if ticket == winning_ticket:
            return 6

        elif ticket[0:4] == winning_ticket[0:4] or ticket[0][1][2][3][4] == winning_ticket[0][1][2][3][4]:
            print('you win $1000000')
            return 4
        else:
            print('you lose')
        return entry and ticket

num_matches()
    

    # elif ticket[0][1][2][3][4][5] == winning_ticket[0][1][2][3][4][5]:
    #     print('you win $7')

    # elif all_tickets[0:2] == winnning_ticket[0:2]:
    #     print('you win $100')

    # elif all_tickets[0:3] == winnning_ticket[0:3]:
    #     print('you win $50000')



 

  


# Creating the winning ticket and start balance as 0.
winning_ticket = pick6_2()
balance = 0


# Creating and comparing 100,000 tickets with the winning ticket.
for _ in range(100000):
    # Create the entry from the 100,000
    entry = pick6_2()

    # Withdrawing $2 for the ticket.
    balance -= 2

    # Call num_matches(winning_ticket, entry).


#     #

# pick6()
# print(tickets)


#print(winnning_ticket)
# all_tickets = []

# def winning():
#     x = 0
#     r=0
#     while x < 100000:
#         r = r + 1
#         x += 1
#         winnum = random.randint(0,99)
#         all_tickets.append(winnum)
#         if r == 6:      
#             return all_tickets
# winning()
# print(all_tickets)

# if all_tickets[0] == winnning_ticket[0]:
#     print('you win $4')
# if all_tickets[0] == winnning_ticket[0] and all_tickets[1] == winnning_ticket[1]:
#     print('you win $7')
# elif all_tickets[0:2] == winnning_ticket[0:2]:
#     print('you win $100')
# elif all_tickets[0:3] == winnning_ticket[0:3]:
#     print('you win $50000')
# elif all_tickets[0:4] == winnning_ticket[0:4]:
#     print('you win $1000000')
# elif all_tickets[0:5] == winnning_ticket[0:5]:
#     print('you win $25000000') 
#else:
    # print('loser')   

 

# winning = []
# count = 0  
# def Winner():
#     count = 0   
#     while count < 6:
#         count = count + 1
#         win = random.randint(0,99)
#         winning.append(win)
#         #if count == 6:
#             #print(f'Winning list is {winning}')
#     return winning


#def num_matches(a, b):
 
        
       # elif  a != b:
          #  print('Loser')
           # print(f'winning numbers are {winning}')
           # print(f'Your numbers are {ticket_num}') 
        
   # return a and b
    
    
#num_matches(Winner, pick6)