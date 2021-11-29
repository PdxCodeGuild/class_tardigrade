#Credit Card Validation 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5 4556737586899855  

credit_card = input("Please enter credit card number here: ")
listed_numbers = []
for digit in credit_card:
    listed_numbers.append(int(digit))
#slice off last digit 
#listed_numbers.pop(16)
check_digit = listed_numbers.pop()
# print(check_digit)
# print(listed_numbers)
#reverse digits
listed_numbers.reverse()
# print(listed_numbers)
#Double every other element in the reversed list.
doubled=[]
for i in range(len(listed_numbers)):
    #determine if index is even or odd
    #append even numbers w/o change
    #double odds and then append
    if i%2 == 0:
        odds= listed_numbers[i]*2
        doubled.append(odds)      
    if i%2 == 1:
        evens= listed_numbers[i]
        doubled.append(evens)

print(doubled)

#Subtract nine from numbers over nine.
nine_subtracted=[]
for digit in doubled:
    #determine numbers over nine
    #subtract 9
    if digit > 9:
        subtracted= digit-9
        nine_subtracted.append(subtracted)
    if digit <= 9:
        nine_subtracted.append(digit)
print(nine_subtracted)
summed_numbers=0
for digit in nine_subtracted:
    summed_numbers = summed_numbers + digit 
    
print(summed_numbers)
second_digit=slice(summed_numbers[0:1])
print(second_digit)

4556737586899855
#4556737586899855


#Take the second digit of that sum.
#If that matches the check digit, the whole card number is valid.
