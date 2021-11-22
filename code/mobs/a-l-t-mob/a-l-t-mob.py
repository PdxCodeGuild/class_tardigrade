# Jackalop mob lab

jackalopes = 2 #Have to figure out how to add jackalopes
age = 0
population = []

while jackalopes <= 1000:
    for jackalope in population:
        age +=1
        if age >= 4 and age <= 8:
            jackalopes =  2 + jackalopes
            # print(age)
            population.append(jackalopes) #add 2 0's
            print(jackalopes)
        if age > 9:
            population.pop(jackalope)
            print(population)
# for loop to add new population between correct ages
            # .append(population)
# if # > 9, .remove

# # 
# while population <= 1000:
#     age +=1
#     if age >= 4 and age <= 8:
#         print(age)
#         if age == 10:
#             break