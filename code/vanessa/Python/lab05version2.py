"NOT FINISHED/ IN PROGRESS"
#Blackjack with A = 1/11
#want to create 3/4(?) tables dependent on whether an A appears in inputs or not. ie if no "A" appear
# reference table one ("values"). If A appears once reference table two etc. if two aces appear then reference table 2 
# or 3 etc...
"""STATUS:"""
# code not working as planned so first step is create tables with values. 
values = {
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
one_ace = {}
two_ace = {}
three_ace = {}

first = input("What is your first card? ")
second = input("What is your second card? ")
third = input("What is your third card? ")



total = values.get(first) + values.get(second) + values.get(third)
print (total)
while not first == "A" and not second == "A" and not third == "A":
    print(first, second, third)
    if total < 17:
        print ("Hit!")
    if 17<= total <21:
        print("Stay!")
    if total == 21:
        print("Blackjack! you win.")
    elif total > 21:
        print ("Bust! Sorry you lose.")
    break

#AAA=33-Bust
#AAA=23-Bust
#AAA=13-hit
#AAA=3 -hit
#AA(any other card) = Bust (11+11+ _) 
#AA (any other card) = hit    (1+1+ _<=12)
#A(K+Q, OR J) = blackjack (1+10+10)
#A(K+Q, OR J) = Bust (11+10+10= 31)
"""total_aces = {""}if first or second or third == "A":
    total_aces= aces.get(first) + aces.get(second) + aces.get(third)
     print (total)"""