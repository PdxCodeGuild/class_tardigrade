import random

winnings = {1  : 4,
            2  : 7,
            3 : 100,
            4 : 50000,
            5  : 1000000,
            6   : 25000000
}

def winning_numbers():
    '''generate six random winning numbers'''
    results= []
    i = 0
    while i < 6:
        results.append(random.randint(1,99))
        i = i + 1
    return results
print("")
print(f"Winning numbers: {winning_numbers()}")
print("")

print (winning_numbers())






Tickets_bought = 0
while -10 < Tickets_bought :
    def pick6():
        '''generate six random numbers'''
        results6= []
        i = 0
        while i < 6:
            results6.append(random.randint(1,99))
            i = i + 1
        return results6
    
    Tickets_bought = int(Tickets_bought) - 2
    print(f"Ticket numbers: {pick6()}   tickets bought ${Tickets_bought}")

def num_matches(winning_numbers, pick6):
    """return the number of matches between the 2 """
    print(winning_numbers[1] == pick6[1])

print(num_matches(winning_numbers, pick6))


    



