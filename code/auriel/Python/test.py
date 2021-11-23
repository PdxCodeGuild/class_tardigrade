def cc_validation():
    user = input('Please input Credit Card Number: ')
    cc_number = list(user)
    cc_number = [int(i) for i in cc_number]

    if len(cc_number) == 16:
        print(f'You have enetered: {user}')
    else:
        print('Please enter a 16 digit card number.')

    sliced = cc_number[0:15] # Removes last digit og list
    print(sliced)
    sliced.reverse() #Reverse the order of the list
    print(sliced)
    sliced[::2] = [n * 2 for n in sliced[::2]] # Double every other number in list. starting with index 0
    print(sliced)
    subtract = [ n - 9 if n > 9 else n for n in sliced] # Subtract 9 for any interger in list that is over 9
    print(subtract)
    sumof_subtract = sum(subtract) # Gets the sum off all the integers in the list of subtract
    print(sumof_subtract)
    last_digit = sumof_subtract % 10
    print(last_digit)
    if last_digit == cc_number[15]:
        print(f'This is a valid Credit Card!')
    else:
        print(f'This is NOT a valid Credit Credit! Please try again.')
    
cc_validation()