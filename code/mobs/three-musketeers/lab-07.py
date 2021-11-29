"""Jackalopes"""

repoduction = [0, 0, 0, 2, 2, 2, 2, 2, 0, 0]

"""Each number represents how old each jackalope is"""
jackalopes = [0,0]
years = 0
while len(jackalopes) < 1000:
    for i in range(len(jackalopes)):
        jackalopes[i] += 1
        if jackalopes[i] >= 4 and jackalopes[i] < 9:
            jackalopes.append(0)
    counter = len(jackalopes) -1
    while counter >= 0:
        jackalope = jackalopes[counter]
        if jackalope == 10:
            jackalopes.pop(counter)
        counter -= 1
    years += 1

print(years)


    #print(jackalopes)
"""
single set of jackalopes lifetime reperduction
[1,1] 0
[2,2] 0
[3,3] 0
[4,4,0,0] 2
[5,5,1,1,0,0] 6
[6,6,2,2,1,1,0,0] 8
[7,7,3,3,2,2,1,1,0,0] 10
[8,8,4,4,3,3,2,2,1,1,0,0,0,0] 10
[9,9,5,5,4,4,3,3,2,2,1,1,1,1,0,0,0,0] 
[10,10,6,6,5,5,4,4,3,3,2,2,2,2,1,1,1,1,0,0,0,0,0,0] -22 jackalopes

other variable:
11 pairs produced per lifetime
Jackalopes are reproductive from ages 4-8 and die at age 10.
Gestation is instantaneous. Each gestation produces two offspring.
Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do

"""