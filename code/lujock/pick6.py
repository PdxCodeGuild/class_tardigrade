import random

numbers = ['3', '7', '20', '28', '35', '42']

for i in range (0,6):
      number = random.randint(1,69)
  #Check if this number has already been picked and ...
while number in numbers:
    # ... if it has, pick a new number instead 
    number = random.randint(1,69)
  
  #Now that we have a unique number, let's append it to our list.
numbers.append(numbers)

#Sort the list in ascending order
numbers.sort()

#Display the list on screen:
print(">>> Today's lottery numbers are: ") 
print(numbers)