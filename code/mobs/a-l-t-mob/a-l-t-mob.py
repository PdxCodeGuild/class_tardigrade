# Jackalop mob lab

jackalopes = 0 #Have to figure out how to add jackalopes
year = 0
population = [0, 0]


while len(population) < 1000:

    for i, jackalope in enumerate(population):
                
        
        population[i] = jackalope + 1
        
        #checks breeding age
        if jackalope >= 4 and jackalope <= 8:

            population.append(jackalopes) #add 2 0's


        #jackalope dies
        if jackalope > 9:

            population.pop(i)
            

    year += 1

    print(population)
    print(year)
