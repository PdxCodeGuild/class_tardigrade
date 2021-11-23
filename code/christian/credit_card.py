

card = [1, 2, 3]  # have a list to store card number

int(input('What are the numbers of your card?: ')) # make user input int

for x in range(16): # range of card number
    user =int(input()) # put user input into variable
    card.append(user) # append to list #this works


check_digit = card.pop()
print(check_digit)

# check_digit = []
# return_value = card.pop(15)
# print(return_value)
  

