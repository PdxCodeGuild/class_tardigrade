import random

# numbers = ['3', '6', '28', '25', '28', '35'] 
def pick_6():
    output = []
    for i in range(6):
        print()
        lottery = random.randint(1,99)
        output.append(lottery)
    return output
    # create empty list
    # loop six times
    # add a random on each loop
    # return the list from the biggining.
    
print(pick_6()) 
    
# numbers

def winning():
    lottery = random.randint(0,7)
    if lottery < 2:
        return True
    else:
        return False
    
    
    
# numbers = random.randint(1, 69)
# print(numbers)
# print("random lottery number")

# for i in range(6):
#     print(numbers) 