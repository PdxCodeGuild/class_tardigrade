import random
all_tickets = []
t = 0
p=0
tickets = []
def pick6():
    ter =0

    
    while ter < 6:
        ter = ter + 1
        p=0
        tick = random.randint(0,99)
        tickets.append(tick)
        if ter == 6:
            return tickets
        

pick6()

y = 0

for i in range(100000):
    y = y + 1
    all_tickets.append( tickets ) 
    return all_tickets
    print(all_tickets)




# all_tickets=[]

# win=0
# while win < 100000:
#     win = win +1
#     all_tickets.append(pick6())
    
#     if win == 100000:
#          print(all_tickets)


