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
#print(f"Winning ticket: {winning_ticket}")

my_tickets = []
Tickets_bought = 0

while -8 < Tickets_bought:
    my_tickets.append(pick6())
    Tickets_bought = Tickets_bought -2   
#print(f"Ticket numbers: {my_tickets}   tickets bought ${Tickets_bought}")




def num_matches(winning_ticket, my_tickets):
    """("return") the number of matches between the 2"""
    #if winning_ticket[0]== my_tickets [0]:
    print (winning_ticket[0])
    print (my_tickets[0])
    # if winning_ticket[1]== my_tickets [1]:
    #         print ("match")
    # if winning_ticket[2]== my_tickets [2]:
    #         print ("match")
    # if winning_ticket[3]== my_tickets [3]:
    #         print ("match")
    # if winning_ticket[4]== my_tickets[4]:
    #         print ("match")
    # if winning_ticket[5]== my_tickets[5]:
    #         print ("match")       
    # else:
    #         print("no match")    
    # print(num_matches(winning_ticket,my_tickets))

num_matches(winning_ticket, my_tickets)


# def num_matches(winner, ticket_list):
#     """
#     return the number of matches between the 2 tickets
#     """
#     ...

# # range(len(winning_ticket)) == range(len(pick6)):
# #         print ("match")
# #print(num_matches(winning_numbers,pick6))"""



    
