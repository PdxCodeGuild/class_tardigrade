import random



def winning_numbers():
    '''generate six random winning numbers'''
    results= []
    i = 0
    while i < 6:
        results.append(random.randint(1,99))
        i = i + 1
    return results
    
for i in range(len(winning_numbers)):
        print(winning_numbers[i])
print("")
defined_winnings= (f"Winning numbers: {winning_numbers()}")
print(defined_winnings)
print(defined_winnings [0])