

card = []  # have a list to store card number

user_input = (input('What are the numbers of your card?: ')) #card input

for char in user_input: #for loop to convert to int
    char = int(char)
    card.append(char)
    

check_digit = card.pop() #remove last number
print(check_digit)

card.reverse() # reverse list

card[::2] = [x*2 for x in card[::2]] #split card to get every other element/multiply by 2


# print(card) #test

subtracted = [] #new list of subtracted numbers

for x in (card):   #for loop to subtract from numbers over 9(see my_notes for enumerate version)
    if x > 9:
        x -= 9
        subtracted.append(x)
    else:
     subtracted.append(x) 


sum = (sum(subtracted)) #pull the sum of list after subtracting
print(sum)
digit = sum % 10 #gives us second digit
print(digit)

if digit == check_digit: #final checks
    print('Valid')
else:
    print('Not valid')












  

