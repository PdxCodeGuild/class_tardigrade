import time
name = input("What is your name? ")
time.sleep(3)
print(f"Hello, {name}.")
time.sleep(3)
print(f"{name}, with one being the lowest and ten the highest answer the following questions please: ")
feeling = int(input('On a scale of 1-10, how are you feeling today?'))
if feeling <= 3:
    print(f"I am sorry to hear that, I hope your day gets better {name}.")
elif feeling <= 6:
    print("Better days are on their way!")
else:
    print(f"Your so great, your off on your way, today is your day {name}!")