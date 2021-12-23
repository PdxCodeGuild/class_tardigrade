#Blackjack
values = {
    "A" : 1,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
}

first = input("What is your first card? ")
second = input("What is your second card? ")
third = input("What is your third card? ")

print(first, second, third)
total = values.get(first) + values.get(second) + values.get(third)
print (total)
if total < 17:
    print ("Hit!")
if 17<= total <21:
    print("Stay!")
if total == 21:
    print("Blackjack! you win.")
elif total > 21:
    print ("Bust! Sorry you lose.")
