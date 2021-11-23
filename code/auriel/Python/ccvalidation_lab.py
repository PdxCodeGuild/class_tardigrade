def cc_validation():
    user = input('Please input Credit Card Number: ')
    cc_number = list(user)
    cc_number = [int(i) for i in cc_number]

    if len(cc_number) == 16:
        print(f'You have enetered: {user}')
    else:
        print('Please enter a 16 digit card number.')

    sliced = cc_number[0:15] # Removes last digit og list

    sliced.reverse() #Reverse the order of the list

    sliced[::2] = [n * 2 for n in sliced[::2]] # Double every other number in list. starting with index 0
    
    subtract = [ n - 9 if n > 9 else n for n in sliced] # Subtract 9 for any interger in list that is over 9
    
    sumof_subtract = sum(subtract) # Gets the sum off all the integers in the list of subtract
    
    last_digit = sumof_subtract % 10
    
    if last_digit == cc_number[15]: # If the last digit of the sum is equal to 16th digit of the credit card number entered
        print(f'This IS a valid Credit Card!')
    else:
        print(f'This is NOT a valid Credit Credit! Please try again.')
    

cc_validation()