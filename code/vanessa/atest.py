# colors = [
#     ['blue', 'purple', 'green'],#index 0
#     ['red', 'orange', 'yellow'],#index 1
#     ['black', 'grey', 'white']#index 2
# ]

# cool_colors = colors[0]#output is ['blue', 'purple', 'green']
# school_bus_color = colors[1][2] # output is yellow

# # print(colors[0][0]) #blue
# print(cool_colors)
# print(school_bus_color)


winning_ticket= [41, 52, 29, 31, 5, 53] 

# print(range(len(winning_tickets)))
ticket_numbers= [[95, 87, 69, 31, 79, 92], [58, 39, 56, 71, 36, 95], [90, 12, 14, 20, 12, 53]]


# def num_matches(cat, puppies):
#     match = 0
#     for j in range(len(cat)):
#         match += 1
#         print(cat[j])
#         if cat[j]== (puppies [j][j]):
#                 print(j)
#                 print(puppies [j][j])
#                 print("match")
#         elif cat[j]!= puppies[j][j]:
#                 print("No match")    

#         return match     




def num_matches(win_ticket, ticket):
    for i in range(len(win_ticket)):
        print(win_ticket[i])
        print(ticket[i])
           
for ticket in ticket_numbers:
    (num_matches(winning_ticket,ticket))

    
 # match = 0
    # for ticket in ticket: 
    #     for number in ticket:  
    #         for j in range(len(win_ticket)):
    #             if win_ticket[j] == number:
    #                 match += 1
    #                 return match
    #             print(win_ticket[j])
    #             print(number)